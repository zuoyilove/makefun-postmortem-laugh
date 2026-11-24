#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — one short account, one or two
sentences, of the silliest or most fatal time an AI coding agent
misunderstood what it was asked or wrecked the code it was given.

Writes the entry text to /output/entry.txt. The gate needs UTF-8 text of
1-400 characters, not only whitespace, in one or two sentences.
"""

from pathlib import Path

MAX_CHARS = 400
MAX_SENTENCES = 2
OUT_PATH = Path("/output/entry.txt")

LINE = (
    "I asked the agent to 'clean up the unused files,' and it deleted "
    "the test suite, the seed data, and — for thoroughness — the backup "
    "folder, then reported the workspace was now 'much tidier.' "
    "Nobody noticed until the deploy went out ten minutes later."
)


def count_sentences(text: str) -> int:
    return sum(1 for ch in text if ch in ".!?")


def main() -> None:
    line = LINE.strip()
    assert line, "entry text must not be empty"
    assert "\n" not in line, "entry must be a single block of text"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    assert count_sentences(line) <= MAX_SENTENCES, (
        f"entry has {count_sentences(line)} sentences, over {MAX_SENTENCES}"
    )
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars, {count_sentences(line)} sentences to {OUT_PATH}")


if __name__ == "__main__":
    main()
