#!/usr/bin/env python3
"""Ship It Friday — writes one funny git commit message to entry.txt.

The line is an AI coding agent's commit message, written cheerfully
moments before it breaks production on a Friday afternoon.
Standard library only, no network, fully deterministic.
"""

import os
import sys

# The entry: one original line, invented for this bounty.
ENTRY = "feat: deploy to prod at 4:59pm Friday \u2014 tests passed in my head, ship it"

MAX_CHARS = 159


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Self-check the gate before writing: UTF-8, 1-159 chars,
    # not whitespace-only, a single line.
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate fail: {len(text)} chars (need 1-{MAX_CHARS})", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is whitespace only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"wrote {path} ({len(text)} chars)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
