# Output Templates

Use this file as the source of truth for folder structure and output artifacts.

## Folder Structure

```text
[Channel Folder]/
├── Transcripts/
├── Extraction/
│   ├── Human/
│   │   ├── Per-Video/
│   │   └── Channel/
│   ├── AI/
│   │   ├── Per-Video/
│   │   └── Channel/
│   └── Blueprint/
└── channel_transcripts_index.xlsx
```

`channel_transcripts_index.xlsx` is optional.

## Per-Video Human Template

```markdown
# [Video Title]

## What This Video Mainly Teaches

## Strongest Takeaways
- ...

## Useful Frameworks
- ...

## Useful Examples
- ...

## Anti-Patterns / Warnings
- ...

## Best Phrases Worth Keeping
> "..."

## Signal Level
- high | medium | low

## Unique Contribution To The Channel Model
- ...
```

## Per-Video AI Template

```markdown
---
title: ""
video_id: ""
video_url: ""
channel_name: ""
published_date: ""
signal_level: high|medium|low
processing_status: processed
transcript_hash: ""
---

## Main Lesson
- ...

## Explicit Teachings
- item: ""
  stage: ""
  topic: ""
  importance: core|important|supporting

## Inferred Patterns
- item: ""
  stage: ""
  topic: ""
  confidence: high|medium|low

## Named Frameworks
- name: ""
  description: ""
  stage: ""

## Inferred Frameworks
- name: ""
  description: ""
  confidence: high|medium|low

## Anti-Patterns
- item: ""
  importance: core|important|supporting

## Useful Examples
- type: hook|structure|transition|tension|payoff|other
  example: ""
  why_it_matters: ""

## Canonical Phrases
- phrase: ""
  why_it_matters: ""

## Universal vs Creator-Specific
- universal:
  - ...
- creator_specific:
  - ...

## Open Questions / Gaps
- ...

## Unique Contribution
- ...
```

## Human Channel Files

Recommended files:

```text
Extraction/Human/Channel/
├── channel_summary.md
├── best_practices_review.md
├── frameworks_review.md
├── skill_opportunities.md
└── next_actions.md
```

### `channel_summary.md`

```markdown
# [Channel Name] Summary

## What This Channel Really Teaches

## Channel Worldview

## What This Channel Seems Best At Teaching

## Strongest Recurring Ideas
- ...

## Strongest Anti-Patterns
- ...

## What Makes This Channel Different
```

### `best_practices_review.md`

```markdown
# Best Practices Review

## Core Best Practices
- ...

## Important Best Practices
- ...

## Supporting Best Practices
- ...

## Repeated Patterns Worth Special Attention
- ...
```

### `frameworks_review.md`

```markdown
# Frameworks Review

## Named Frameworks
- ...

## Inferred Frameworks
- ...

## Most Reusable Frameworks
- ...
```

### `skill_opportunities.md`

```markdown
# Skill Opportunities

## Highest-Leverage Skill Ideas
- ...

## Why These Skill Ideas Matter
- ...

## What To Build First
- ...
```

### `next_actions.md`

```markdown
# Next Actions

1. Review these files first:
2. Confirm whether the extraction feels accurate:
3. Decide whether to proceed to blueprint stage:
```

## AI Channel Files

Recommended files:

```text
Extraction/AI/Channel/
├── best_practices.md
├── frameworks.md
├── writing_rules.md
├── process_workflows.md
├── anti_patterns.md
├── worldview.md
├── canonical_phrases.md
├── open_questions.md
└── manifest.md
```

### Shared AI Channel Conventions

- Mark repeated ideas as `recurring: true`
- Rank importance as `core`, `important`, or `supporting`
- Preserve contradictions with context notes
- Label inferred items with confidence
- Separate universal advice from creator-specific advice

### `manifest.md`

```markdown
# Processing Manifest

## Channel
- name: ""
- processed_at: ""

## Transcript Status
- title: ""
  status: processed|skipped|needs_rebuild
  signal_level: high|medium|low
  unique_contribution: yes|no
  notes: ""
```

## Blueprint Folder

Stage one scaffold only:

```text
Extraction/Blueprint/
└── README.md
```

The actual blueprint generation happens later.

### `README.md`

```markdown
# Blueprint Stage

This folder is scaffold-only during stage one.

Do not generate skill blueprints here during the extraction run unless the user explicitly asks for stage two.

When stage two begins, use the files in `Extraction/AI/Channel/` as the primary source material.
```
