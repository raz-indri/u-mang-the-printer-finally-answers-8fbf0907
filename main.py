#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line, in the office printer's own voice, to entry.txt.
Deterministic: the same text on every run.
"""

import os

MAX_CHARS = 240

# Duel winner (7-0 across 8 drafts): weary, literal, faintly passive-aggressive,
# one specific absurd detail (87-page email thread, printed twice).
TEXT = "I am not broken. I am refusing to print your 87-page email thread twice."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-240 characters.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-240 chars, got {len(TEXT)}"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the bytes exactly TEXT: no trailing newline, no translation.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to {path}")


if __name__ == "__main__":
    main()
