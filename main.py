#!/usr/bin/env python3
"""u-suga-everyday-things-two-lines-longer-run-f8734479: Everyday Things, Two Lines.

Writes the two-line entry to /output/entry.txt for make.fun's
program/v1 judge: line 1 explains rain to a 10-year-old through a
concrete, surprising analogy; line 2 says honestly what the analogy
maps and what it leaves out. Gate: UTF-8 text, 1-400 characters.
Local check 2026-11-25: 2 runs byte-identical, output 220 chars.
"""

import os

ENTRY = (
    "Rain is the sky squeezing out a sponge the size of a city after soaking it in the sea.\n"
    "The sponge shows how clouds hold water and let it fall, but it leaves out that clouds are made of tiny drops, not one big wet thing.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
