---
name: channel-best-practices-extractor
description: Extracts the full best-practices system from a scriptwriting-focused teaching channel whose transcript markdown files already exist in a channel folder. Use when the user wants to process one channel folder, extract frameworks, rules, anti-patterns, worldview, recurring ideas, and skill opportunities, or says things like "extract everything this channel teaches", "turn this channel into reusable scriptwriting knowledge", "build a best practices extractor", or "analyze all transcripts in this folder". This skill is scriptwriting-first in behavior, but keeps a reusable extraction structure underneath. It is for one channel at a time. It reads all transcripts, creates Human and AI output layers, and prepares a later blueprint stage without generating the blueprint in the same pass. It does not fetch transcripts itself unless the user explicitly asks to expand the workflow.
---

# Channel Best Practices Extractor

Use this skill to turn one scriptwriting-focused teaching channel into a reusable knowledge system.

The goal is not generic summarization.

The goal is to extract everything the channel teaches that could later become:
- writing rules
- frameworks
- workflows
- anti-patterns
- analyzer logic
- future Codex skills

This skill is for **one channel at a time**.

Default input:
- a channel folder with transcript markdown files already present
- optional spreadsheet context such as `channel_transcripts_index.xlsx`

Default behavior:
- process all transcripts in the folder
- create both Human and AI layers
- keep per-video and channel-level artifacts separate
- stop before blueprint generation
- do not fetch transcripts as part of stage one

Read these files at point of use:
- `references/templates.md`
- `references/examples.md`
- `references/gotchas.md`
- `references/test_prompts.md`
- `references/future-scaffold.md`

## Core Principles

- Treat transcripts as the source of truth.
- Optimize for reusable scriptwriting intelligence, not summary length.
- Preserve uncertainty instead of flattening it.
- Keep explicit teachings separate from inferred patterns.
- Keep named frameworks separate from inferred frameworks.
- Weight findings by signal, repetition, and teaching depth.
- Preserve contradictions with context.
- Keep anti-patterns as first-class outputs.
- Keep the first stage resumable and auditable.
- Do not generate the blueprint layer in the same stage unless the user explicitly overrides that.

## What This Skill Extracts

This skill should extract:
- best practices
- writing rules
- frameworks
- workflow/process patterns
- anti-patterns
- worldview/philosophy
- canonical phrases
- recurring ideas
- stage-specific script advice
- creator-specific advice
- broadly reusable advice
- open questions and unresolved gaps
- strong examples worth preserving

Organize findings by both:
- topic
- scriptwriting stage

Suggested stage buckets:
- ideation
- hook
- opening
- body structure
- retention
- transitions
- payoff
- CTA
- editing-for-script intent

## Task Progress

- [ ] Step 1: Confirm the channel folder path and transcript source files
- [ ] Step 2: Inspect folder contents and optional spreadsheet context
- [ ] Step 3: Set up the extraction output structure if missing
- [ ] Step 4: Process all transcripts into per-video Human and AI notes
- [ ] Step 5: Synthesize channel-level Human outputs
- [ ] Step 6: Synthesize channel-level AI outputs
- [ ] Step 7: Build the manifest and next-actions artifacts
- [ ] Step 8: Validate resumability, change detection, and output completeness
- [ ] Step 9: Stop before blueprint generation unless explicitly told to continue

## Workflow

### Step 1: Inspect Input

Expect one channel folder.

Minimum useful input:
- transcript markdown files

Optional support input:
- spreadsheet index

Before extracting:
- confirm this is one channel, not a mixed-channel folder
- list transcript files
- note whether optional spreadsheet context exists
- detect whether an `Extraction/` folder already exists

Do not expand this stage into transcript collection unless the user explicitly asks for that workflow.

If the folder appears mixed, stop and ask the user to split it.

### Step 2: Initialize Output Structure

Use the output hierarchy in `references/templates.md`.

Keep these layers separate:
- `Extraction/Human/Per-Video/`
- `Extraction/AI/Per-Video/`
- `Extraction/Human/Channel/`
- `Extraction/AI/Channel/`
- `Extraction/Blueprint/`

`Blueprint/` is scaffold only in stage one. Do not populate it with generated blueprints yet unless the user asks.

### Step 3: Process Every Transcript

Process all transcripts in the folder, not just a sample.

For each transcript:
- extract the main lesson
- identify explicit teachings
- infer repeated patterns when justified
- identify named frameworks
- infer unnamed frameworks when repeated structure clearly exists
- extract useful examples
- extract anti-patterns
- preserve strong exact phrases when worth keeping
- assign signal level
- assign confidence labels where inference is involved
- note what this transcript uniquely contributed

Filename rule:
- per-video output filename must exactly match the transcript filename
- do not rename, slugify, or normalize filenames
- keep the same `.md` name in both `Human/Per-Video/` and `AI/Per-Video/`

Keep low-signal transcripts:
- mark them as low-signal
- down-weight them
- still preserve uniquely useful insights

If a transcript has already been processed:
- skip it by default
- only rebuild if the user explicitly requests refresh/rebuild

If the transcript changed since the last extraction:
- flag it in the manifest
- do not silently overwrite prior outputs

### Step 4: Build Per-Video Outputs

Create both Human and AI per-video files.

Per-video Human files:
- should be readable and quick to review
- can be a bit looser in prose

Per-video AI files:
- should be structured and consistent
- should be designed for later machine reuse

Use strict templates for AI per-video outputs.

Keep the Human and AI versions aligned by source video title so they are easy to audit side by side.

### Step 5: Build Channel-Level Human Outputs

The Human channel layer should stay condensed and easy to review.

Focus on:
- what the channel really teaches
- strongest recurring best practices
- strongest frameworks
- what the channel seems best at teaching
- major anti-patterns
- key worldview/philosophy
- top skill opportunities
- next recommended action

### Step 6: Build Channel-Level AI Outputs

The AI channel layer should be split into focused files for later reuse.

Use separate files for:
- best practices
- frameworks
- writing rules
- process workflows
- anti-patterns
- worldview
- canonical phrases
- open questions
- manifest/index

Keep these outputs structured, tagged, and confidence-aware.

### Step 7: Handle Signal, Recurrence, and Contradictions

When advice repeats across many transcripts:
- mark it as recurring
- rank its importance as `core`, `important`, or `supporting`

When advice conflicts:
- keep both
- explain the likely context for each
- never flatten the contradiction away

When deciding what is widely reusable:
- separate universal advice from creator-specific advice

### Step 8: Finish the First Stage

At the end of stage one, create:
- a manifest/index file
- a short next-actions file

The next-actions file should help the user decide whether to:
- review Human channel outputs first
- refine extraction assumptions
- proceed to the blueprint stage later

Do not create the future-skill blueprint in the same run unless the user asks.

Write a short `Extraction/Blueprint/README.md` that explains:
- this folder is intentionally scaffold-only in stage one
- blueprint generation is the second stage
- the AI channel outputs are the source material for that stage

## Gotchas

Read `references/gotchas.md` before execution.

The short version:
- mixed-channel folders corrupt the model
- low-signal is not zero-signal
- recurring markers lose value when overused
- canonical phrases must stay verbatim
- extraction is not summarization
- stage one must not leak into blueprint generation
- re-processing already-finished transcripts should be skipped by default

## Validation Checklist

Before finishing, verify:
- every transcript has a per-video output or a clear status
- low-signal items were marked, not discarded
- explicit vs inferred findings are labeled
- named vs inferred frameworks are labeled
- confidence labels exist where needed
- recurring and importance markers are present
- contradictions were preserved with context
- canonical phrases were promoted selectively, not excessively
- Human layer is easy to scan
- AI layer is split and structured
- manifest/index reflects real processing state

If validation fails, fix the missing pieces before stopping.

When practical, run lightweight checks from `scripts/` after extraction:
- `python scripts/validate_manifest.py "<channel folder>/Extraction/AI/Channel/manifest.md"`
- `python scripts/validate_per_video_counts.py "<channel folder>"`

## When To Stop

Stop after the extraction stage when:
- per-video outputs exist
- channel-level Human outputs exist
- channel-level AI outputs exist
- manifest/index exists
- next-actions exists
- `Blueprint/README.md` exists

Do not continue into blueprint generation unless the user explicitly asks for stage two.
