#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes one line of office comedy to /output/entry.txt
(UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "We have an open-plan office and a closed-door policy on raises - "
    "somehow the noise travels freely but the money never does."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
