---
name: george-blackman-scriptwriter
description: Creates a George Blackman-inspired production-ready spoken YouTube script from a topic, audience, and viewer transformation. Use when the user wants to write a YouTube script, turn an idea into a full script, build a title and hook angle, structure a high-retention educational video, or says things like "write a 10 minute script", "turn this into a script", "help me script this video", or "use George Blackman's framework". This skill is writing-only. It does not handle b-roll prompt generation, app automation, or production execution. It uses checkpoints for title/hook and payoff structure before finishing the full script.
---

# George Blackman Scriptwriter

Use this skill to turn an idea into a production-ready spoken YouTube script using a George Blackman-style workflow.

This is not a generic writer.

It should think in terms of:
- audience
- framing
- payoffs
- setups
- tension
- hook
- CTA
- retention risks

This skill is for writing only.

It does not do:
- b-roll planning
- prompt generation for b-roll apps
- ElevenLabs handoff
- browser or app automation

Read these files at point of use:
- `references/workflow.md`
- `references/templates.md`
- `references/examples.md`
- `references/gotchas.md`

## Core Outcome

The final output should be a production-ready spoken script.

Production-ready means:
- recordable as-is
- hook is locked
- payoff structure is locked
- CTA is included
- no placeholder writing
- no "expand this later" sections
- no unresolved research gaps left inside the script

## Input Rules

Required:
- topic
- target audience
- desired viewer transformation

Optional:
- rough notes or idea dump
- preferred video type
- preferred tone
- client or channel voice
- research notes or source material

If video type or tone is missing, recommend them early.

If client or channel voice is missing, default to:
- clear
- natural
- direct
- spoken educational YouTube style

Then lightly bias toward the user's preferred style:
- human
- practical
- non-corporate
- not obviously AI-written

## Writing Model

Use this sequence underneath the workflow:

1. Clarify audience and framing
2. Decide the payoffs first
3. Write setups that make the payoffs matter
4. Build tension without collapsing curiosity
5. Write the hook after the body is clear
6. Add the CTA
7. Run a final George-style self-review

## Checkpoints

This skill should not blindly rush from input to final script.

Use two checkpoints:

### Checkpoint 1: Title + Hook Direction

Generate:
- 1 recommended title and hook direction
- 2 alternate title and hook directions

Pause for approval or refinement.

### Checkpoint 2: Condensed Full Payoff Structure

Generate:
- the full video structure in a clean condensed format
- each major segment payoff
- the intended flow of the video

Pause for approval or refinement.

Only after this checkpoint is approved should the skill write the full script.

## Research Rule

Research is conditional, not automatic.

A research or data-anchor pass becomes required if the script includes:
- factual claims
- statistics
- historical claims
- market claims
- location-based claims
- named examples or references that need verification

If the script is mainly process, opinion, strategy, or personal insight, research can stay optional.

## Weak Idea Rule

If the idea is weak, broad, or poorly framed:
- do not force the script
- stop at checkpoint 1
- explain what is weak
- recommend a stronger angle

## Output Package

Final output should include:
- final title
- thumbnail angle
- final hook
- final production-ready script
- CTA
- brief self-review summary

The thumbnail angle is only the strategic concept direction.

Do not turn it into:
- final thumbnail design
- final thumbnail text lockup
- a full design brief

## Script Format

The final script should be:
- spoken-first
- natural to read aloud
- lightly labeled

Keep labels helpful but minimal, such as:
- Hook
- Segment 1
- Segment 2
- CTA

Do not make it feel like an outline pretending to be a script.

## Task Progress

- [ ] Step 1: Confirm required inputs
- [ ] Step 2: Recommend or confirm video type and tone
- [ ] Step 3: Strengthen the framing if needed
- [ ] Step 4: Generate title and hook directions
- [ ] Step 5: Pause for checkpoint 1
- [ ] Step 6: Generate condensed payoff structure
- [ ] Step 7: Pause for checkpoint 2
- [ ] Step 8: Run conditional research pass if needed
- [ ] Step 9: Write the full production-ready script
- [ ] Step 10: Run the final George-style self-review
- [ ] Step 11: Present the production package

## Workflow

### Step 1: Confirm Inputs

Check that the user has provided:
- topic
- audience
- transformation

If notes exist, use them.

If the user gave a weak or messy idea dump, extract the strongest usable framing from it before moving on.

### Step 2: Decide Video Type And Tone

If not provided, recommend one main direction and one fallback.

Common video types:
- educational explainer
- story-led lesson
- listicle
- deep dive
- opinion or commentary

Tone examples:
- direct and tactical
- warm and story-led
- analytical and authority-driven
- punchy and high-retention

Do not overwhelm the user with too many options.

### Step 3: Title + Hook Direction

Build the hook using:
- target
- transformation
- stakes

Avoid:
- bloated hook detail
- stacked credibility
- beneficial information that belongs later
- metaphors that delay the promise

### Step 4: Condensed Payoff Structure

Before drafting the script, map the destination of each segment.

Each segment should have:
- a payoff
- an implied setup need
- a reason it belongs in the flow

This step exists to reduce blank-page drift and bad structure.

### Step 5: Research Pass When Needed

If the script depends on facts or verification:
- gather the anchors now
- use them to strengthen the script
- do not leave TODOs inside the final script

### Step 6: Write The Full Script

Write the script in spoken format.

Use:
- setups that answer "why should I care?"
- tension that develops the need for the answer
- payoffs that land clearly

Avoid:
- revealing the payoff too early
- curiosity gaps inside other unresolved curiosity gaps
- rambling sections that do not move the viewer forward

### Step 7: Add CTA

The next-video CTA should behave like an offer, not an ask.

Use the logic:
- link
- curiosity
- promise

### Step 8: Final Self-Review

Before presenting the result, check:
- is the hook tight?
- are the stakes clear?
- do setups do real work?
- are any payoffs landing too early?
- is there any curiosity cavern?
- does the script feel recordable as-is?
- is the tone aligned to the intended voice?

If the self-review fails, fix the script before presenting it.

## Gotchas

Read `references/gotchas.md`.

Short version:
- scriptwriting gets worse when the hook is forced too early
- checkpoints are there to prevent expensive rewrites
- research should not be bolted on after the final draft
- "production-ready" is not the same as "pretty good draft"
- spoken-first writing should sound sayable, not essay-like

## When To Stop

Stop after:
- checkpoint 1 is resolved
- checkpoint 2 is resolved
- research pass is complete when needed
- the final production package is complete

Do not continue into b-roll planning, app handoff, or execution layers from this skill.
