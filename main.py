#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

One line, at most 140 characters: the text message a smart fridge sends
its owner at 3am. Printed to stdout and written to /output/entry.txt,
as the bounty rules require.
"""

import os

ENTRY = (
    "3am. You've opened me six times tonight and eaten nothing. "
    "I think you're just here for the light. "
    "Same, honestly. Stay a while."
)

MAX_CHARS = 140


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
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
