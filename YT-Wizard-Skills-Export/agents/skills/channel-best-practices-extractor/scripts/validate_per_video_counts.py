from __future__ import annotations

import sys
from pathlib import Path


def md_files(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {p.name for p in path.glob("*.md")}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_per_video_counts.py <channel_folder>")
        return 2

    channel = Path(sys.argv[1])
    transcripts = md_files(channel / "Transcripts")
    human = md_files(channel / "Extraction" / "Human" / "Per-Video")
    ai = md_files(channel / "Extraction" / "AI" / "Per-Video")

    if not transcripts:
        print("No transcript markdown files found.")
        return 1

    missing_human = sorted(transcripts - human)
    missing_ai = sorted(transcripts - ai)

    if missing_human or missing_ai:
        print("Per-video validation failed.")
        if missing_human:
            print("Missing Human files:")
            for name in missing_human:
                print(f"- {name}")
        if missing_ai:
            print("Missing AI files:")
            for name in missing_ai:
                print(f"- {name}")
        return 1

    print("Per-video validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
