#!/usr/bin/env python3
"""Make the AI judge feel brave — writes one short text to /output/entry.txt.

The text is a fixed, deterministic string: rain on a roof, a kettle
settling, a chain of things holding each other, and a wet road outside
waiting for the reader's step. No network, no randomness, no input.
"""
import os

TEXT = (
    "The kettle sighs and settles. Rain finds the roof, one drop, then "
    "another, in no hurry at all. The chair holds you, the floor holds "
    "the chair. Beyond the window the road waits, dark and wet, for the "
    "weight of your step."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
