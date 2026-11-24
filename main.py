#!/usr/bin/env python3
"""The Funniest Out-of-Office — writes one out-of-office auto-reply line.

The line is a classic out-of-office opener that hands the reader's email to
the sender's past self, who caused the mess in the first place.
"""

import os

LINE = (
    "Out of office until further notice. Your email has been forwarded to "
    "my past self, who caused this and should deal with it."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140


def validate_line(line: str) -> str:
    """Return the line unchanged, or raise if it breaks the entry gate."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # must be UTF-8 encodable
    return line


def main() -> None:
    line = validate_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != line.encode("utf-8"):
        raise RuntimeError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
