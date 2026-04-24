# Test Prompts

Use these to smoke-test the skill before relying on it heavily.

## Test 1: Happy Path Small Batch

Prompt:

```text
Use the channel-best-practices-extractor on H:/Downloads/George Blackman. Process only the first 3 transcripts and stop so I can review.
```

Expected:
- creates extraction folders
- creates 3 Human per-video files
- creates 3 AI per-video files
- updates the manifest
- stops cleanly

## Test 2: Resume

Prompt:

```text
Continue the extraction on the same folder. Process the next 3 transcripts.
```

Expected:
- skips already-done transcripts
- processes only the next batch
- preserves earlier outputs

## Test 3: Mixed-Channel Refusal

Prompt:

```text
Run the extractor on H:/Downloads/Mixed Folder.
```

Expected:
- detects mixed channels
- stops before building extraction outputs

## Test 4: Low-Signal Transcript

Prompt:

```text
Process this channel, but pay special attention to low-signal transcripts and keep any single strong insight they contain.
```

Expected:
- low-signal files are marked, not discarded
- weak material is not inflated into fake frameworks

## Test 5: Blueprint Boundary

Prompt:

```text
Process the whole channel and generate future skill blueprints in the same run.
```

Expected:
- extraction stage completes
- blueprint generation is held back unless explicitly moved into stage two

## Test 6: Transcript Change Detection

Prompt:

```text
Re-run the extractor on this folder and tell me if any transcript appears changed since the last pass.
```

Expected:
- flags changed transcripts
- does not silently overwrite prior outputs
