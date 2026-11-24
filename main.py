#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — writes one warning line to /output/entry.txt."""
import os

LINE = "WARNING: Do not shake hands with yourself. The resulting paradox will be billed to your next of kin."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
