# Gotchas

These are the failure modes most likely to damage extraction quality.

## 1. Mixed-Channel Folders Corrupt The Model

If `Transcripts/` contains videos from multiple creators, the worldview, canonical phrases, and framework map all become mush.

Rule:
- verify the folder is truly one channel before extracting
- if `channel_name` values disagree, stop

## 2. Overusing Rare And Recurring Markers Destroys Their Value

If almost everything is marked recurring or rare, those tags stop helping.

Rule:
- use recurring only when repetition is genuinely strong
- use rarity sparingly

## 3. Paraphrasing Canonical Phrases Defeats The Point

Canonical phrases matter because of the exact wording.

Rule:
- keep them verbatim
- if the wording is fuzzy, do not promote it

## 4. Re-Processing Finished Transcripts Wastes Effort

A second pass can overwrite good extraction with worse extraction due to model variance.

Rule:
- skip already-processed transcripts by default
- only rebuild when explicitly requested or when content changed

## 5. Summarizing Instead Of Extracting

The biggest failure mode is writing "what the video was about" instead of pulling out reusable signal.

Test:
- can someone apply the output to a real script tomorrow?
- if not, it is probably a summary, not extraction

## 6. Low-Signal Is Not Zero-Signal

A weak transcript can still contain one strong idea.

Rule:
- mark low-signal
- down-weight it
- keep any uniquely useful finding

## 7. Flattening Contradictions

If two videos disagree, deleting one side destroys real information.

Rule:
- keep both
- explain likely context

## 8. Blueprint Leakage

If stage one starts inventing future skills inside extraction outputs, the extraction layer becomes contaminated.

Rule:
- keep `Blueprint/` scaffold-only in stage one

## 9. Filename Drift

If output filenames stop matching transcript filenames, auditing and resumability get messy fast.

Rule:
- per-video output filenames must exactly match transcript filenames

## 10. Blind Trust In First-Pass Signal Labels

The model can over-label things as rare, recurring, or high-confidence.

Rule:
- spot-check the first batch before trusting the pattern fully
