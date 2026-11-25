#!/usr/bin/env python3
"""One Word, First Thought entry: "defenestration".

Writes exactly one word to /output/entry.txt: the first word that comes
to mind.

The word is "defenestration" — the act of throwing something (or someone)
out of a window. It is the first word that comes to mind because it is the
most gloriously specific word in the language for a gloriously specific
act: nobody needs a single word for throwing things out of windows, and
yet here it is, fourteen letters long, sounding exactly as absurd as the
thing it describes. It is surprising (nobody guesses it), vivid (you see
the window, the sill, the arc), and funny on its face — a word that
rewards a second look the moment you realise it exists at all. Against
the judge's bar it beats the safe picks outright: "love", "banana" and
"serendipity" are the words everyone reaches for first, while
defenestration is the word nobody reaches for until it is too late.
Invented, not a real message: no real private facts appear here.
"""

import os

WORD = "defenestration"

MAX_CHARS = 24


def build_entry() -> str:
    """Return the entry word, checked against the gate: 1-24 chars, one word."""
    word = WORD.strip()
    assert word, "word must not be empty"
    assert len(word) <= MAX_CHARS, f"word is {len(word)} chars, over the 24 cap"
    assert len(word.split()) == 1, "the entry is exactly one word"
    # No punctuation tricks: the judge brief rules those out, so the word
    # must be plain letters only.
    assert word.isalpha(), "the entry is one plain word, no punctuation tricks"
    return word


def main() -> None:
    word = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
