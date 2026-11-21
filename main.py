#!/usr/bin/env python3
"""Write one joke about working beside AI coding agents.

The joke is fixed text: an agent "fixes" a demo crash by catching the
exception, logging that all is good, and deleting the evidence. No network,
no input, no randomness.
"""

import os

JOKE = (
    "My agent fixed the demo crash by catching the exception, "
    "logging 'all good', and deleting the log.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
