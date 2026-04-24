"""MCP Server Evaluation Harness for Codex/OpenAI."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

try:
    from openai import OpenAI
except ImportError as exc:
    raise SystemExit("Missing dependency: openai. Install it with `pip install openai`.") from exc

from connections import create_connection

DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_ENV_KEY = "OPENAI_API_KEY"

EVALUATION_PROMPT = """You are an AI assistant with access to tools.

When given a task, you MUST:
1. Use the available tools to complete the task
2. Provide summary of each step in your approach, wrapped in <summary> tags
3. Provide feedback on the tools provided, wrapped in <feedback> tags
4. Provide your final response, wrapped in <response> tags

Summary Requirements:
- In your <summary> tags, explain:
  - The steps you took to complete the task
  - Which tools you used, in what order, and why
  - The inputs you provided to each tool
  - The outputs you received from each tool
  - How you arrived at the final response

Feedback Requirements:
- In your <feedback> tags, provide constructive feedback on the tools:
  - Tool naming clarity
  - Input parameter quality
  - Tool description quality
  - Any tool execution errors or awkward UX
  - Specific improvements and why they would help

Response Requirements:
- The response should be concise and directly address the task
- Always wrap the final response in <response> tags
- If you cannot solve the task return <response>NOT_FOUND</response>
- For numeric responses, provide just the number
- For IDs, provide just the ID
- For names or text, provide the exact text requested
- Put the final response last
"""


def parse_evaluation_file(file_path: Path) -> list[dict[str, Any]]:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        evaluations = []
        for qa_pair in root.findall(".//qa_pair"):
            question_elem = qa_pair.find("question")
            answer_elem = qa_pair.find("answer")
            if question_elem is not None and answer_elem is not None:
                evaluations.append(
                    {
                        "question": (question_elem.text or "").strip(),
                        "answer": (answer_elem.text or "").strip(),
                    }
                )
        return evaluations
    except Exception as exc:
        print(f"Error parsing evaluation file {file_path}: {exc}")
        return []


def extract_xml_content(text: str | None, tag: str) -> str | None:
    if not text:
        return None
    pattern = rf"<{tag}>(.*?)</{tag}>"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches[-1].strip() if matches else None


def ensure_openai_api_key() -> str:
    api_key = os.environ.get(OPENAI_ENV_KEY)
    if not api_key:
        raise SystemExit(f"Missing {OPENAI_ENV_KEY}. Set it before running the evaluator.")
    return api_key


def json_safe(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if hasattr(value, "model_dump"):
        return json_safe(value.model_dump())
    if hasattr(value, "__dict__"):
        return json_safe(vars(value))
    return str(value)


def serialize_tool_result(result: Any) -> str:
    return json.dumps(json_safe(result), ensure_ascii=False, indent=2)


def mcp_tools_to_openai_tools(tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
    openai_tools: list[dict[str, Any]] = []
    for tool in tools:
        parameters = tool.get("input_schema") or {"type": "object", "properties": {}}
        openai_tools.append(
            {
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool.get("description") or "",
                    "parameters": parameters,
                },
            }
        )
    return openai_tools


async def request_completion(
    client: OpenAI,
    model: str,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]],
):
    return await asyncio.to_thread(
        client.chat.completions.create,
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0,
    )


async def agent_loop(
    client: OpenAI,
    model: str,
    question: str,
    tools: list[dict[str, Any]],
    connection: Any,
) -> tuple[str | None, dict[str, Any]]:
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": EVALUATION_PROMPT},
        {"role": "user", "content": question},
    ]

    tool_metrics: dict[str, dict[str, Any]] = {}
    for _ in range(20):
        response = await request_completion(client, model, messages, tools)
        message = response.choices[0].message

        assistant_entry: dict[str, Any] = {
            "role": "assistant",
            "content": message.content or "",
        }
        if message.tool_calls:
            assistant_entry["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in message.tool_calls
            ]
        messages.append(assistant_entry)

        if not message.tool_calls:
            return message.content, tool_metrics

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            raw_arguments = tool_call.function.arguments or "{}"
            try:
                tool_input = json.loads(raw_arguments)
            except json.JSONDecodeError:
                tool_input = {}

            tool_start_ts = time.time()
            try:
                tool_result = await connection.call_tool(tool_name, tool_input)
                tool_response = serialize_tool_result(tool_result)
            except Exception as exc:
                tool_response = f"Error executing tool {tool_name}: {exc}\n{traceback.format_exc()}"
            tool_duration = time.time() - tool_start_ts

            if tool_name not in tool_metrics:
                tool_metrics[tool_name] = {"count": 0, "durations": []}
            tool_metrics[tool_name]["count"] += 1
            tool_metrics[tool_name]["durations"].append(tool_duration)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_response,
                }
            )

    raise RuntimeError("Agent loop exceeded maximum tool-call iterations.")


async def evaluate_single_task(
    client: OpenAI,
    model: str,
    qa_pair: dict[str, Any],
    tools: list[dict[str, Any]],
    connection: Any,
    task_index: int,
) -> dict[str, Any]:
    start_time = time.time()
    print(f"Task {task_index + 1}: Running task with question: {qa_pair['question']}")
    response, tool_metrics = await agent_loop(client, model, qa_pair["question"], tools, connection)

    response_value = extract_xml_content(response, "response")
    summary = extract_xml_content(response, "summary")
    feedback = extract_xml_content(response, "feedback")
    duration_seconds = time.time() - start_time

    return {
        "question": qa_pair["question"],
        "expected": qa_pair["answer"],
        "actual": response_value,
        "score": int(response_value == qa_pair["answer"]) if response_value else 0,
        "total_duration": duration_seconds,
        "tool_calls": tool_metrics,
        "num_tool_calls": sum(len(metrics["durations"]) for metrics in tool_metrics.values()),
        "summary": summary,
        "feedback": feedback,
    }


REPORT_HEADER = """
# Evaluation Report

## Summary

- **Accuracy**: {correct}/{total} ({accuracy:.1f}%)
- **Average Task Duration**: {average_duration_s:.2f}s
- **Average Tool Calls per Task**: {average_tool_calls:.2f}
- **Total Tool Calls**: {total_tool_calls}

---
"""

TASK_TEMPLATE = """
### Task {task_num}

**Question**: {question}
**Ground Truth Answer**: `{expected_answer}`
**Actual Answer**: `{actual_answer}`
**Correct**: {correct_indicator}
**Duration**: {total_duration:.2f}s
**Tool Calls**: {tool_calls}

**Summary**
{summary}

**Feedback**
{feedback}

---
"""


async def run_evaluation(eval_path: Path, connection: Any, model: str = DEFAULT_MODEL) -> str:
    print("Starting evaluation")
    client = OpenAI(api_key=ensure_openai_api_key())

    raw_tools = await connection.list_tools()
    tools = mcp_tools_to_openai_tools(raw_tools)
    print(f"Loaded {len(tools)} tools from MCP server")

    qa_pairs = parse_evaluation_file(eval_path)
    print(f"Loaded {len(qa_pairs)} evaluation tasks")

    results = []
    for i, qa_pair in enumerate(qa_pairs):
        print(f"Processing task {i + 1}/{len(qa_pairs)}")
        result = await evaluate_single_task(client, model, qa_pair, tools, connection, i)
        results.append(result)

    correct = sum(r["score"] for r in results)
    accuracy = (correct / len(results)) * 100 if results else 0
    average_duration_s = sum(r["total_duration"] for r in results) / len(results) if results else 0
    average_tool_calls = sum(r["num_tool_calls"] for r in results) / len(results) if results else 0
    total_tool_calls = sum(r["num_tool_calls"] for r in results)

    report = REPORT_HEADER.format(
        correct=correct,
        total=len(results),
        accuracy=accuracy,
        average_duration_s=average_duration_s,
        average_tool_calls=average_tool_calls,
        total_tool_calls=total_tool_calls,
    )

    report += "".join(
        [
            TASK_TEMPLATE.format(
                task_num=i + 1,
                question=qa_pair["question"],
                expected_answer=qa_pair["answer"],
                actual_answer=result["actual"] or "N/A",
                correct_indicator="✅" if result["score"] else "❌",
                total_duration=result["total_duration"],
                tool_calls=json.dumps(result["tool_calls"], indent=2),
                summary=result["summary"] or "N/A",
                feedback=result["feedback"] or "N/A",
            )
            for i, (qa_pair, result) in enumerate(zip(qa_pairs, results))
        ]
    )
    return report


def parse_headers(header_list: list[str]) -> dict[str, str]:
    headers = {}
    if not header_list:
        return headers
    for header in header_list:
        if ":" in header:
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()
        else:
            print(f"Warning: Ignoring malformed header: {header}")
    return headers


def parse_env_vars(env_list: list[str]) -> dict[str, str]:
    env = {}
    if not env_list:
        return env
    for env_var in env_list:
        if "=" in env_var:
            key, value = env_var.split("=", 1)
            env[key.strip()] = value.strip()
        else:
            print(f"Warning: Ignoring malformed environment variable: {env_var}")
    return env


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate MCP servers using test questions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python evaluation.py -t stdio -c python -a my_server.py eval.xml
  python evaluation.py -t sse -u https://example.com/mcp -H "Authorization: Bearer token" eval.xml
  python evaluation.py -t http -u https://example.com/mcp -m gpt-4.1-mini eval.xml
        """,
    )

    parser.add_argument("eval_file", type=Path, help="Path to evaluation XML file")
    parser.add_argument("-t", "--transport", choices=["stdio", "sse", "http"], default="stdio", help="Transport type (default: stdio)")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL, help=f"OpenAI model to use (default: {DEFAULT_MODEL})")

    stdio_group = parser.add_argument_group("stdio options")
    stdio_group.add_argument("-c", "--command", help="Command to run MCP server (stdio only)")
    stdio_group.add_argument("-a", "--args", nargs="+", help="Arguments for the command (stdio only)")
    stdio_group.add_argument("-e", "--env", nargs="+", help="Environment variables in KEY=VALUE format (stdio only)")

    remote_group = parser.add_argument_group("sse/http options")
    remote_group.add_argument("-u", "--url", help="MCP server URL (sse/http only)")
    remote_group.add_argument("-H", "--header", nargs="+", dest="headers", help="HTTP headers in 'Key: Value' format (sse/http only)")

    parser.add_argument("-o", "--output", type=Path, help="Output file for evaluation report (default: stdout)")
    args = parser.parse_args()

    if not args.eval_file.exists():
        print(f"Error: Evaluation file not found: {args.eval_file}")
        sys.exit(1)

    headers = parse_headers(args.headers) if args.headers else None
    env_vars = parse_env_vars(args.env) if args.env else None

    try:
        connection = create_connection(
            transport=args.transport,
            command=args.command,
            args=args.args,
            env=env_vars,
            url=args.url,
            headers=headers,
        )
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print(f"Connecting to MCP server via {args.transport}...")
    async with connection:
        print("Connected successfully")
        report = await run_evaluation(args.eval_file, connection, args.model)
        if args.output:
            args.output.write_text(report)
            print(f"\nReport saved to {args.output}")
        else:
            print("\n" + report)


if __name__ == "__main__":
    asyncio.run(main())
