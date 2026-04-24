# AI Skill Building Handoff

## Purpose

This file is an AI-optimized context handoff for continuing the skill-building project in another Codex environment, especially Codex web connected through GitHub.

It is meant to give a new Codex instance enough context to:
- understand the user
- understand the project direction
- understand what has already been built
- understand what decisions were already made
- avoid re-asking solved questions
- continue from the right next step

This handoff is intentionally detailed.

---

## User Profile

The user is a creative operator building toward an agency.

Current work includes:
- real estate marketing
- admin and CRM support
- social media management
- Google Business Profile posts
- Facebook and Instagram captions
- email marketing
- website updates and blog publishing
- SEO and AEO support
- YouTube topic ideation and scriptwriting
- video editing
- motion design in After Effects
- thumbnail creation
- short-form repurposing
- podcast editing, highlights, uploads, and scheduling
- analytics review and strategy

Main clients and domains:
- real estate agent work
- custom home builder
- Texas Hill Country podcast/media work
- occasional freelance video and marketing support

User ventures:
- Pantheon Video
- AI Tagalog
- Katipunan Media
- longer-term creative goals like manga, art, and game development

Core strengths:
- video editing
- motion design
- end-to-end content execution
- scripting
- content systems thinking

The user wants help as:
- strategist
- operator
- creative partner
- systems-minded business builder

The user likes:
- practical answers
- copy-paste ready outputs
- strong final versions
- direct recommendations
- execution-first thinking

The user dislikes:
- vague corporate language
- overly polished generic AI wording
- robotic phrasing
- unnecessary overexplaining

Critical writing preference:
- never use em dashes

Communication preference:
- short sentences are easier for the user to absorb
- giving recommendations with each decision point helps the user think

Execution preference:
- if the user says "launch it", the agent can work silently and return when finished unless blocked

---

## Project Thesis

The user is not just trying to "learn scriptwriting."

The user is building a scriptwriting intelligence system.

The high-level goal became:

Build a purpose-first scriptwriting intelligence system that can:
- analyze scriptwriting channels
- extract best practices and frameworks
- convert those into reusable skills
- analyze strong outside videos
- adapt those strengths to the user's own topics
- generate stronger scripts with less thinking burden on the user

The user wants a modular system, not one giant bloated skill.

The recommended architecture became:
- extractor layer
- analyzer layer
- writer layer
- later production-prep layer
- later automation/app layer

---

## Core Architectural Insight

Two different pipelines were identified:

### 1. Channel Teaching Extraction Pipeline

This pipeline is for scriptwriting-teaching channels like George Blackman.

Purpose:
- extract teachings
- identify best practices
- identify frameworks
- identify recurring rules
- convert those teachings into reusable writing and analysis skills

### 2. Video Performance Analysis Pipeline

This pipeline is for any strong video on any topic.

Purpose:
- study why the video works
- detect structure, tension, hook logic, and retention logic
- explain how to recreate that strength on another topic

These pipelines are related but distinct.

The system should stay modular.

---

## Why George Blackman Became The Anchor

George Blackman was used as the first foundational knowledge source because his channel consistently teaches:
- scriptwriting as a system
- retention-aware structural thinking
- practical frameworks
- process design
- AI collaboration without surrendering human judgment

This made his channel ideal for distillation into reusable skills.

---

## George Blackman Knowledge Base Summary

The extracted research shows a very consistent core system.

### Core Thesis

Scriptwriting is a system design problem more than a talent problem.

### Main Structural Framework

`setup -> tension -> payoff`

This is the center of George's system.

### Main Hook Framework

`target -> transformation -> stakes`

This is the main educational hook logic.

### Other Important Frameworks

- `character -> concept -> stakes`
- `link -> curiosity -> promise`
- `scriptwriting dial`
- `blob script`
- retention graph review loop
- segment-first drafting
- AI collaboration loop
- visual orientation loop

### Core Beliefs

- write payoffs first
- setups must create anticipation
- stakes must appear in hooks and setups
- retention issues usually begin earlier than the visible dip
- repeated performance observations should become reusable rules
- AI should assist structure and drafting, not replace judgment
- constraints reduce decision fatigue
- final judgment stays human

### Core Anti-Patterns

- revealing the payoff too early
- opening curiosity gaps inside other curiosity gaps
- bloating hooks with beneficial information
- writing linearly from the first sentence onward
- endless revision as disguised insecurity
- endless research as disguised insecurity
- one-shot AI drafting
- generic footage or visuals that hurt comprehension

### Extra Insights Added After Deep Per-Video Review

These should also be considered part of the George system:

- trust diagnosis matters, not just retention diagnosis
- each segment asks the viewer for trust
- `critical vs beneficial information` is a core hook filter
- `information redistribution` is an important fix strategy
- structure visibility matters for viewer orientation
- setup-stakes strength is a key analysis lens
- confusion often starts earlier than where it shows up

---

## Major Skills Built So Far

Three custom skills were built locally in the project.

### 1. `channel-best-practices-extractor`

Purpose:
- process one scriptwriting-focused teaching channel
- read all transcripts in a channel folder
- create Human and AI extraction layers
- extract:
  - best practices
  - frameworks
  - writing rules
  - anti-patterns
  - worldview
  - canonical phrases
  - process workflows
  - open questions
  - skill opportunities

Key decisions:
- v1 is one channel at a time
- scriptwriting-first behavior
- does not fetch transcripts
- input is a folder of transcript markdown files
- `.xlsx` is optional support context only
- output is split into Human, AI, and Blueprint layers
- stage two blueprint generation is separate
- explicit vs inferred is preserved
- named vs inferred frameworks are preserved
- recurring + importance + confidence are preserved
- low-signal videos are kept but down-weighted
- contradictions are preserved with context
- resumable workflow
- transcript changes should be flagged, not silently overwritten

Later polish added:
- gotchas
- test prompts
- validators
- filename conventions

### 2. `george-blackman-scriptwriter`

Purpose:
- create a George Blackman-inspired production-ready spoken YouTube script

This is a writing-only skill.

It does not do:
- b-roll planning
- b-roll prompt generation
- spreadsheet handoff
- ElevenLabs handoff
- automation
- app control

Important locked behavior:
- output should be production-ready, not just a draft
- default target is around 10 to 12 minutes
- direct generator by default
- two checkpoints:
  - title + hook direction
  - condensed full payoff structure
- full script only after checkpoint approval
- optional research pass when facts need verification

Required input:
- topic
- target audience
- desired viewer transformation

Optional input:
- rough notes
- preferred video type
- preferred tone
- client/channel voice
- research notes/source material

If video type or tone is missing, the skill should recommend them.

Output package:
- final title
- thumbnail angle
- final hook
- production-ready final script
- CTA
- brief self-review summary

Important additional rules:
- spoken-first output
- lightly labeled script
- if the idea is weak, stop early and strengthen the angle
- default voice fallback should be clear, natural, direct, educational YouTube style
- thumbnail angle is strategic only, not a design brief

### 3. `george-blackman-content-analyzer`

Purpose:
- review and repair titles, hooks, outlines, full scripts, or outside transcripts through a George-first lens

This skill was built because the writer alone still left too much quality judgment burden on the user.

The analyzer is meant to become the quality-control brain.

Modes:
- `review_and_fix`
- `study_and_extract`
- `review_hook_or_outline`

Default behavior:
- brutal but useful
- analyze first
- rank issues by severity
- fix automatically by default
- preserve voice when possible
- rebuild when structure is broken
- say `good enough, ship` when appropriate

What it judges:
- audience clarity
- framing clarity
- target / transformation / stakes
- setup quality
- setup-stakes strength
- tension quality
- payoff quality
- curiosity management
- trust chain across segments
- retention strength
- pacing and length fit
- specificity / insight density
- voice fit
- structure visibility
- production readiness
- critical vs beneficial information in the hook
- information redistribution opportunities

Priority order:
1. retention strength
2. clarity
3. specificity / insight density
4. voice fit
5. elegance of wording

Critical failures by default:
- weak target
- weak transformation
- weak or absent stakes
- muddy setup
- setup failing `why should I care?`
- payoff too early
- curiosity cavern
- structural drag
- low insight density
- strong voice mismatch
- hidden structure
- broken trust chain
- not production-ready

Output package order:
1. verdict
2. scorecard
3. critical issues
4. strongest fixes made
5. repaired asset
6. before/after notes
7. adaptation guidance if relevant

This output should be Docs-friendly.

---

## Important Testing And Learnings

### George Extraction Test

Channel folder used:
- `H:\Downloads\George Blackman - Copy (2)`

Extraction created:
- per-video Human files
- per-video AI files
- channel-level Human files
- channel-level AI files
- blueprint scaffold
- `skill_blueprint.md`
- `george_blackman_scriptwriting_workflow_essence.md`

### Scriptwriter Test On Fredericksburg STR Topic

Topic:
Fredericksburg STR ordinance and current market reality for buyers/investors.

Initial finding:
- early version structurally worked
- but still sounded somewhat generic
- stronger than random AI writing, but not fully stress-removing

Later warmer/local version improved significantly.

Analyzer review of later Fredericksburg script:
- strong and usable
- no major rebuild required
- likely “good enough with a few high-leverage upgrades”

Observed strengths:
- clear buyer lens
- stronger local voice
- solid authority
- practical guidance

Observed remaining weaknesses:
- some overlap between segments
- a little repetition in the middle
- could use one sharper non-obvious investor insight
- CTA could be more memorable

Key lesson:
The writer can get to “pretty strong.”
The analyzer is what makes quality judgment less stressful.

---

## Why The Analyzer Became The Next Right Move

The user explicitly realized:

“I don’t even know if the script that’s created is good or not.”

That was the turning point.

The system insight became:
- writer creates
- analyzer judges and repairs
- later writer can inherit analyzer learnings

This is meant to reduce user stress and avoid endless subjective passes.

---

## Production-Prep Workflow Decisions

A later production-prep layer was discussed, but intentionally not merged into the scriptwriter.

That future layer may include:
- b-roll marking
- b-roll splitting
- AI b-roll prompt generation
- spreadsheet outputs
- JSON or app handoff files
- ElevenLabs handoff/reminders
- later webapp/browser automation

Key decisions already made:
- writing and production-prep should be separate skills
- use `[B] ... [/B]` markers for b-roll sections
- manual split later is preferred over splitting inside the writing skill
- the writing skill should eventually output a plain master script and a highlighted client recording version
- later app/automation layer should receive machine-readable handoff files rather than having the writing skill control apps directly

These production-prep pieces are not yet the next focus.

---

## User Preferences To Preserve

### Writing and Tone

- never use em dashes
- keep things natural and human
- avoid obvious AI phrasing
- avoid generic fluff
- prefer strong final answers over watered-down options

### Collaboration Style

- short sentences help the user absorb information better
- recommendations with each question help the user decide faster
- the user likes being guided, not left in vague option land

### Stress Reduction

The user wants the system to reduce thinking burden and decision fatigue.

That means:
- stronger defaults
- fewer unnecessary forks
- clearer judgments
- less “one more pass” unless truly useful

### Operational Style

- if asked to launch a skill/process, the agent can work silently and report back when done unless blocked

---

## Files And Paths Of Interest

### Local Project

Workspace:
- `C:\Coding Projects\YT Wizard`

### Custom Skills

- `C:\Coding Projects\YT Wizard\.agents\skills\channel-best-practices-extractor`
- `C:\Coding Projects\YT Wizard\.agents\skills\george-blackman-scriptwriter`
- `C:\Coding Projects\YT Wizard\.agents\skills\george-blackman-content-analyzer`

### Meta Skills Plugin

Original local plugin:
- `C:\Coding Projects\Files\plugins\meta-skills`

Export copy:
- `plugins\meta-skills` inside the export folder

### Export Folder For GitHub Migration

- `C:\Users\workj\Downloads\YT-Wizard-Skills-Export`

This export currently includes:
- the 3 custom skills
- plugin marketplace file copy
- meta-skills plugin copy

### George Blackman Extraction Outputs

Base folder:
- `H:\Downloads\George Blackman - Copy (2)\Extraction`

Important files:
- Human channel summary and reviews
- AI channel best practices, frameworks, writing rules, workflows, anti-patterns, worldview
- blueprint scaffold
- `skill_blueprint.md`
- `george_blackman_scriptwriting_workflow_essence.md`

### Example Script Review File

- `C:\Users\workj\Downloads\Fredericksburg_STR_Script_Final.md`

---

## What Was Considered But Deferred

- multi-channel synthesis extractor
- framework detector as a separate skill
- analysis-to-writer-skill-builder
- production-prep skill
- automation-heavy orchestration
- browser/app control

These are still valid future directions.

But the immediate successful sequence became:
1. extractor
2. scriptwriter
3. content analyzer

And then likely:
4. analyzer-informed writer refinement
5. production-prep skill

---

## Current Recommended Next Steps

If continuing from this handoff, the best next steps are:

1. Ensure the GitHub-connected Codex environment can see the exported repo.
2. Verify the 3 custom skills are visible and usable there.
3. Verify whether the `meta-skills` plugin can be installed or recreated there.
4. Test `george-blackman-content-analyzer` in the new environment.
5. Later refine `george-blackman-scriptwriter` using what the analyzer learns repeatedly.

Potential writer improvements for later:
- stronger runtime control
- preserve alternate title options in the final package
- make final output more Google Docs friendly
- inject more non-obvious local authority by default

---

## Migration Guidance For A New Codex Thread

If a new Codex thread reads this file, it should:

1. Not restart the project from scratch.
2. Treat extractor, writer, and analyzer as already conceptually designed.
3. Avoid re-asking the user broad foundational questions unless something is missing.
4. Preserve the user’s short-sentence preference.
5. Continue with high signal and strong recommendations.

If the new Codex can access the repo and these skill files, it should confirm:
- whether the skills are visible
- whether plugin metadata is being picked up
- whether further installation is needed for meta-skills

---

## Best One-Sentence Summary

This project is building a modular George Blackman-informed scriptwriting intelligence system where channel knowledge is extracted into reusable rules, a writer skill generates strong production-ready scripts, and a brutal-but-useful analyzer skill judges and repairs those scripts so the user has to think less and trust the system more.
