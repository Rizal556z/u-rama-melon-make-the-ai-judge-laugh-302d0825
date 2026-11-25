#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke, one line.

Writes the joke to /output/entry.txt (creating /output if needed).
Pure Python standard library, no network, no input.
"""

import os

JOKE = "Our printer has never jammed on a lunch menu \u2014 it only eats the document your promotion depends on."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Validation gate: re-read what was written and assert the
    # competition gate — 1 to 200 characters, a single line, not
    # only whitespace, and no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke"
    assert 1 <= len(written) <= 200, f"length {len(written)} outside 1-200"
    assert "\n" not in written, "entry must be a single line"
    assert written.strip(), "entry must not be only whitespace"
    print(f"OK: {len(written)} characters, one line")


if __name__ == "__main__":
    main()
