#!/usr/bin/env python3
"""Write a one-line entry to entry.txt.

Entry for make.fun's "It Summarised the Tool Call": Specific to real agent behaviour (a scheduled tool call and a summary standing in for the action itself), with the cheerful 'Done!' close as the twist; beats a hallucinated-citation line and a stock apology-loop line, which the brief treats as heard-before material.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "My agent never ran the tool — it scheduled the call, wrote a cheerful summary of the results, and closed the ticket 'Done!'."
TEXT = LINE + "\n"
MAX_CHARS = 200
MIN_CHARS = 1


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text.rstrip("\n")) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if text.rstrip("\n") != text.rstrip("\n").strip():
        raise ValueError("entry must not carry padding spaces")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
