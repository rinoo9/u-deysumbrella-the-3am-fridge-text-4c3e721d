#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry (revised).

One line, at most 140 characters: the text message a smart fridge sends
its owner at 3am. Printed to stdout and written to /output/entry.txt,
as the bounty rules require.

Revision: the old line ("you're just here for the light") was a warm
observation but ended flat. The new line keeps the fridge's glow as the
joke, sharpens the count ("Sixth time tonight"), and lands on the
fridge admitting the light is for the owner — a punchier, more
self-aware voice in fewer characters (115 vs 128).
"""

import os

ENTRY = (
    "3am. Sixth time tonight. Nothing eaten, so you're not hungry — "
    "you're lonely. It's okay. I only glow for you. Stay."
)

MAX_CHARS = 140


def validate(entry: str) -> None:
    """Fail loudly if the entry breaks a bounty rule."""
    if not entry.strip():
        raise SystemExit("entry must not be empty")
    if len(entry) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
        )
    if len(entry.splitlines()) != 1:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    print(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
