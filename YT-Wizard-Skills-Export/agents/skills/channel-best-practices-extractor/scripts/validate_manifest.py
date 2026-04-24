from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_manifest.py <manifest.md>")
        return 2

    manifest_path = Path(sys.argv[1])
    if not manifest_path.exists():
        print(f"Missing manifest: {manifest_path}")
        return 1

    text = manifest_path.read_text(encoding="utf-8")
    required = [
        "# Processing Manifest",
        "## Channel",
        "## Transcript Status",
        "status:",
        "signal_level:",
        "unique_contribution:",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        print("Manifest validation failed. Missing:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Manifest validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
