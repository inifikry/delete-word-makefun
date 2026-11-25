#!/usr/bin/env python3
"""Entry for make.fun: The Word You'd Delete From the Dictionary.

Writes the single chosen word to /output/entry.txt.
Deterministic: no network, no randomness, no input, no time dependence.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The word to delete: "queue" — five letters, four of them silently
# standing in line behind the q. Delete the word, end the queue.
WORD = "queue"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
