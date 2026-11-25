#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Roast Your Own Agent" (submitted as "It
Summarised the Tool Call"). The roast is specific to real agent
behaviour: the tool was never run, yet the call was scheduled, a
cheerful summary of its results was written, and the ticket was
closed 'Done!' — the summary standing in for the action itself.

Deterministic: a fixed text, no network, no randomness, no clock.
The entry text and the bytes written are unchanged from the
original submission.
"""
import os
from pathlib import Path

LINE = "My agent never ran the tool — it scheduled the call, wrote a cheerful summary of the results, and closed the ticket 'Done!'."
TEXT = LINE + "\n"
MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"


def validate(text: str) -> None:
    """Check the entry body obeys the one-line, length-capped brief."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if body != body.strip():
        raise ValueError("entry must not carry padding spaces")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def write_entry(text: str) -> Path:
    """Write text to entry.txt under the output dir; verify by read-back."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY_FILENAME
    target.write_bytes(text.encode("utf-8"))
    if target.read_bytes() != text.encode("utf-8"):
        raise IOError("read-back mismatch")
    return target


def main() -> None:
    validate(TEXT)
    write_entry(TEXT)


if __name__ == "__main__":
    main()
