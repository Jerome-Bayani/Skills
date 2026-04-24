# Examples

## Example Input

```text
H:/Downloads/George Blackman/
├── Transcripts/
│   ├── Video A.md
│   ├── Video B.md
│   └── Video C.md
└── channel_transcripts_index.xlsx
```

## Example User Request

```text
Use the channel-best-practices-extractor on H:/Downloads/George Blackman and extract everything useful for scriptwriting.
```

## Example User Request: Resume

```text
Continue the extractor on H:/Downloads/George Blackman and skip anything already processed.
```

## Example User Request: Small Batch

```text
Use the extractor on H:/Downloads/George Blackman but process only the first 3 transcripts so I can review them.
```

## Example Outcome

```text
H:/Downloads/George Blackman/
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

## Example Judgment Calls

### Repeated Advice

If the creator emphasizes curiosity-driven openings across many videos:
- mark it recurring
- rank it `core`
- preserve strongest examples

### Contradictory Advice

If one video says to get to the point fast, but another uses long scene-setting:
- keep both
- explain likely context
- do not force one universal rule

### Low-Signal Video

If a transcript is shallow overall but includes one strong hook insight:
- mark signal level as low
- keep the one strong insight
- down-weight the rest
