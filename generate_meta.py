#!/usr/bin/env python3
"""Generate data/meta.json for the preview site: per-provider data timestamps.

Run this after copying fresh provider_data/output/*.json into data/, so the
preview page can show how old each provider's data is and flag staleness.
"""
import json
import time
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def main() -> None:
    meta = {"generatedAt": {}, "builtAt": int(time.time() * 1000)}
    for path in sorted(DATA_DIR.glob("*.json")):
        if path.name == "meta.json":
            continue
        meta["generatedAt"][path.stem] = int(path.stat().st_mtime * 1000)

    meta_path = DATA_DIR / "meta.json"
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {meta_path} with {len(meta['generatedAt'])} provider timestamps")


if __name__ == "__main__":
    main()
