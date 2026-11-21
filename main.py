#!/usr/bin/env python3
"""Make the AI judge feel brave — writes one short text to /output/entry.txt.

The text is a fixed, deterministic string: rain on a roof, a kettle
settling, a chair holding you. No network, no randomness, no input.
"""
import os

TEXT = (
    "The kettle sighs and settles. Rain finds the roof, one drop, then "
    "another, in no hurry at all. The chair holds you. The evening holds "
    "the house. Whatever comes next can wait until you are ready to meet "
    "it \u2014 and you will be."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
