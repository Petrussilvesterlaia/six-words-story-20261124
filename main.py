#!/usr/bin/env python3
"""Six Words, One Story -- make.fun entry.

Writes one complete six-word story to /output/entry.txt.

The story: a man who wronged people, was forgiven, and then lived
longer than every person who forgave him -- a whole life, its turn,
and what he did, all left in six words.
"""

import os


STORY = "He outlived everyone who forgave him."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
