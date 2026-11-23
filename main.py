#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review (76 chars, one line) to
/output/entry.txt. Deterministic: constant text, no input, no network,
no randomness, no clock.
"""

import os

REVIEW = "Gravity: made stairs necessary and never once helped carry anything up them."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check (revision pass): the written bytes must equal the review
    # exactly, and must pass the sealed gate (1-160 chars, not blank).
    # Any mismatch fails loudly instead of shipping a wrong entry.
    expected = REVIEW.encode("utf-8")
    assert 1 <= len(REVIEW) <= 160, "review outside 1-160 char gate"
    assert REVIEW.strip(), "review is only whitespace"
    assert "\n" not in REVIEW, "review must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(
            "entry.txt bytes differ from REVIEW: wrote %d bytes, expected %d"
            % (len(written), len(expected))
        )


if __name__ == "__main__":
    main()
