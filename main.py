#!/usr/bin/env python3
"""Write a short poem about permission to /output/entry.txt.

The poem: a spare key kept under a mat for years — permission that
existed long before it was asked for, and only became real in the
asking. Stdlib only, no network, no input.
"""
import os
from pathlib import Path

POEM = """For years the spare key
lay under your mat —
not against thieves,
but for the day I'd ask.

I never asked. I rehearsed
on your step, polite,
while the door stayed shut.

Today I asked. You said:
it was yours since
the day you needed it."""


def main() -> None:
    # Normalise the ending: no trailing blank lines, exactly one newline.
    text = POEM.rstrip() + "\n"
    assert 1 <= len(text) <= 280, f"poem must be 1-280 chars, got {len(text)}"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
