#!/usr/bin/env python3
"""
Audio Transcriber for Codex

Transcribes audio with Whisper and can generate a structured markdown summary
using the OpenAI API when `OPENAI_API_KEY` is available.
"""

from __future__ import annotations

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Installing openai for LLM processing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--user", "openai"], check=False)
    from openai import OpenAI

try:
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
except ImportError:
    print("Installing rich for better UI...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--user", "rich"], check=False)
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn

try:
    from tqdm import tqdm
except ImportError:
    print("Installing tqdm for progress bars...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--user", "tqdm"], check=False)
    from tqdm import tqdm

try:
    from faster_whisper import WhisperModel
    TRANSCRIBER = "faster-whisper"
except ImportError:
    try:
        import whisper
        TRANSCRIBER = "whisper"
    except ImportError:
        print("No transcription engine found.")
        print("Install one of: pip install faster-whisper OR pip install openai-whisper")
        sys.exit(1)

console = Console()
DEFAULT_LLM_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_ENV_KEY = "OPENAI_API_KEY"

DEFAULT_MEETING_PROMPT = """
Role: You are a professional transcription analyst who turns raw transcripts into clean markdown documents.

Instructions:
1. Identify the content type (meeting, interview, lecture, voice note, or call).
2. Extract the main topics and key decisions.
3. Identify speakers when the transcript makes them clear.
4. Capture follow-up actions, owners, and deadlines when present.
5. Organize the result into clear markdown sections.
6. Stay concise and preserve important context.

End goal: A polished markdown summary that is easy to read and reuse.
"""


def openai_available() -> bool:
    return bool(os.environ.get(OPENAI_ENV_KEY))


def create_openai_client(timeout: int = 300) -> OpenAI:
    api_key = os.environ.get(OPENAI_ENV_KEY)
    if not api_key:
        raise RuntimeError(f"Missing {OPENAI_ENV_KEY}")
    return OpenAI(api_key=api_key, timeout=timeout)


def call_openai(prompt: str, system_prompt: str, model: str, timeout: int) -> str | None:
    try:
        client = create_openai_client(timeout=timeout)
        response = client.chat.completions.create(
            model=model,
            temperature=0.2,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        return (response.choices[0].message.content or "").strip() or None
    except Exception as exc:
        console.print(f"[red]OpenAI request failed: {exc}[/red]")
        return None


def optimize_prompt(raw_prompt: str, model: str, timeout: int = 90) -> str:
    system_prompt = (
        "You rewrite rough user instructions into a compact, high-signal prompt for an AI "
        "that will transform an audio transcript into a professional markdown summary. "
        "Return only the improved prompt."
    )
    optimized = call_openai(raw_prompt, system_prompt, model=model, timeout=timeout)
    return optimized or DEFAULT_MEETING_PROMPT


def handle_prompt_workflow(user_prompt: str | None, transcript: str, model: str) -> str | None:
    ai_enabled = openai_available()

    if user_prompt:
        console.print("\n[cyan]User prompt provided[/cyan]")
        console.print(
            Panel(
                user_prompt[:300] + ("..." if len(user_prompt) > 300 else ""),
                title="Original prompt",
                border_style="dim",
            )
        )

        if not ai_enabled:
            console.print(f"[yellow]{OPENAI_ENV_KEY} not set. Using the original prompt.[/yellow]")
            return user_prompt

        console.print("\n[cyan]Optimizing prompt with OpenAI...[/cyan]")
        improved_prompt = optimize_prompt(f"Improve this transcript-processing prompt:\n\n{user_prompt}", model=model)

        console.print("\n[green]Improved version:[/green]")
        console.print(
            Panel(
                improved_prompt[:500] + ("..." if len(improved_prompt) > 500 else ""),
                title="Optimized prompt",
                border_style="green",
            )
        )
        console.print("\n[dim]Original version:[/dim]")
        console.print(
            Panel(
                user_prompt[:300] + ("..." if len(user_prompt) > 300 else ""),
                title="Your prompt",
                border_style="dim",
            )
        )

        confirm = Prompt.ask("\nUse improved version?", choices=["y", "n"], default="y")
        return improved_prompt if confirm == "y" else user_prompt

    console.print("\n[yellow]No processing prompt provided.[/yellow]")
    if not ai_enabled:
        console.print(f"[yellow]{OPENAI_ENV_KEY} not found. Using the default template.[/yellow]")
        return DEFAULT_MEETING_PROMPT

    console.print("I can analyze the transcript and suggest a good output format.")
    generate = Prompt.ask("\nGenerate a processing prompt automatically?", choices=["y", "n"], default="y")
    if generate == "n":
        console.print("[dim]Saving only the transcript.[/dim]")
        return None

    console.print("\n[cyan]Analyzing transcript...[/cyan]")
    suggestion_meta_prompt = f"""
Analyze this transcript and suggest:
1. The content type.
2. The best output format.
3. The most useful structure for a markdown summary.

Transcript excerpt:
{transcript[:4000]}

Return 2 to 4 concise bullets.
"""
    suggested_type = optimize_prompt(suggestion_meta_prompt, model=model)

    console.print("\n[green]Suggested format:[/green]")
    console.print(Panel(suggested_type, title="Transcript analysis", border_style="green"))

    confirm_type = Prompt.ask("\nUse this direction?", choices=["y", "n"], default="y")
    if confirm_type == "n":
        console.print("[dim]Using the default template...[/dim]")
        return DEFAULT_MEETING_PROMPT

    console.print("\n[cyan]Generating a structured prompt...[/cyan]")
    final_meta_prompt = f"""
Create a final prompt for an AI assistant that will turn a transcript into a professional markdown document.

Desired output direction:
{suggested_type}

The prompt should be practical, specific, and ready to use.
Return only the prompt.
"""
    generated_prompt = optimize_prompt(final_meta_prompt, model=model)

    console.print("\n[green]Generated prompt:[/green]")
    console.print(
        Panel(
            generated_prompt[:600] + ("..." if len(generated_prompt) > 600 else ""),
            title="Preview",
            border_style="green",
        )
    )

    confirm_final = Prompt.ask("\nUse this prompt?", choices=["y", "n"], default="y")
    return generated_prompt if confirm_final == "y" else DEFAULT_MEETING_PROMPT


def process_with_llm(transcript: str, prompt: str, model: str, timeout: int = 300) -> str | None:
    full_prompt = f"{prompt}\n\n---\n\nTranscript:\n\n{transcript}"
    system_prompt = (
        "You are a professional transcription analyst. "
        "Follow the user's instructions exactly and return markdown only."
    )
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description=f"Processing with {model}...", total=None)
        return call_openai(full_prompt, system_prompt, model=model, timeout=timeout)


def transcribe_audio(audio_file: str, model: str = "base") -> dict:
    console.print(f"\n[cyan]Transcribing audio with {TRANSCRIBER}...[/cyan]")
    try:
        if TRANSCRIBER == "faster-whisper":
            model_obj = WhisperModel(model, device="cpu", compute_type="int8")
            segments, info = model_obj.transcribe(
                audio_file,
                language=None,
                vad_filter=True,
                word_timestamps=True,
            )
            data = {
                "language": info.language,
                "language_probability": round(info.language_probability, 2),
                "duration": info.duration,
                "segments": [],
            }
            console.print("[dim]Processing segments...[/dim]")
            for segment in tqdm(segments, desc="Segments", unit="seg"):
                data["segments"].append(
                    {
                        "start": round(segment.start, 2),
                        "end": round(segment.end, 2),
                        "text": segment.text.strip(),
                    }
                )
        else:
            import whisper

            model_obj = whisper.load_model(model)
            result = model_obj.transcribe(audio_file, word_timestamps=True)
            data = {
                "language": result["language"],
                "duration": result["segments"][-1]["end"] if result["segments"] else 0,
                "segments": result["segments"],
            }
        console.print(f"[green]Transcription complete. Language: {data['language'].upper()}[/green]")
        console.print(f"[dim]{len(data['segments'])} segments processed[/dim]")
        return data
    except Exception as exc:
        console.print(f"[red]Transcription failed: {exc}[/red]")
        sys.exit(1)


def save_outputs(transcript_text: str, summary_text: str | None, audio_file: str, output_dir: str = ".") -> tuple[str, str | None]:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    transcript_path = Path(output_dir) / f"transcript-{timestamp}.md"
    transcript_path.write_text(transcript_text, encoding="utf-8")
    console.print(f"[green]Transcript saved:[/green] {transcript_path.name}")

    summary_path = None
    if summary_text:
        summary_path = Path(output_dir) / f"summary-{timestamp}.md"
        summary_path.write_text(summary_text, encoding="utf-8")
        console.print(f"[green]Summary saved:[/green] {summary_path.name}")

    return str(transcript_path), str(summary_path) if summary_path else None


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Audio Transcriber for Codex")
    parser.add_argument("audio_file", help="Audio file to transcribe")
    parser.add_argument("--prompt", help="Custom prompt for transcript processing")
    parser.add_argument("--model", default="base", help="Whisper model (tiny/base/small/medium/large)")
    parser.add_argument(
        "--llm-model",
        default=DEFAULT_LLM_MODEL,
        help=f"OpenAI model for prompt optimization and summarization (default: {DEFAULT_LLM_MODEL})",
    )
    parser.add_argument("--output-dir", default=".", help="Output directory")
    args = parser.parse_args()

    if not os.path.exists(args.audio_file):
        console.print(f"[red]File not found: {args.audio_file}[/red]")
        sys.exit(1)

    console.print("[bold cyan]Audio Transcriber for Codex[/bold cyan]\n")
    transcription_data = transcribe_audio(args.audio_file, model=args.model)

    transcript_text = "# Audio Transcript\n\n"
    transcript_text += f"**File:** {Path(args.audio_file).name}\n"
    transcript_text += f"**Language:** {transcription_data['language'].upper()}\n"
    transcript_text += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    transcript_text += "---\n\n## Full Transcript\n\n"

    for seg in transcription_data["segments"]:
        start_min = int(seg["start"] // 60)
        start_sec = int(seg["start"] % 60)
        end_min = int(seg["end"] // 60)
        end_sec = int(seg["end"] % 60)
        transcript_text += f"**[{start_min:02d}:{start_sec:02d} -> {end_min:02d}:{end_sec:02d}]**  \n{seg['text']}\n\n"

    if not openai_available():
        console.print(f"\n[yellow]{OPENAI_ENV_KEY} not detected.[/yellow]")
        console.print("[dim]Saving only the transcript file.[/dim]")
        save_outputs(transcript_text, None, args.audio_file, args.output_dir)
        console.print(f"\n[cyan]To enable summaries, set {OPENAI_ENV_KEY}.[/cyan]")
        return

    console.print(f"\n[green]OpenAI API available. Using model: {args.llm_model}[/green]")
    final_prompt = handle_prompt_workflow(args.prompt, transcript_text, args.llm_model)
    if final_prompt is None:
        save_outputs(transcript_text, None, args.audio_file, args.output_dir)
        return

    summary_text = process_with_llm(transcript_text, final_prompt, args.llm_model)
    if summary_text:
        console.print("[green]Summary generated successfully.[/green]")
    else:
        console.print("[yellow]Summary generation failed. Saving only the transcript.[/yellow]")

    console.print("\n[cyan]Saving files...[/cyan]")
    save_outputs(transcript_text, summary_text, args.audio_file, args.output_dir)
    console.print("\n[bold green]Done.[/bold green]")


if __name__ == "__main__":
    main()
