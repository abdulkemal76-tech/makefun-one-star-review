#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of water to /output/entry.txt.
Water: no flavour at all, yet the only drink the body insists on.
"""

import os

REVIEW = (
    "One star. No flavour at all, and still the only drink my body "
    "insists on. I would like to speak to the manager of thirst."
)


def main() -> None:
    # The gate requires 1-160 characters of UTF-8 text, a single line.
    assert 1 <= len(REVIEW) <= 160, f"review is {len(REVIEW)} chars"
    assert "\n" not in REVIEW
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
