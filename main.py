"""Entry program for make.fun's "Make the AI judge feel held" bounty.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. The text is 1-280 Unicode code points, UTF-8, and
not only white space. Deterministic: the same bytes on every run.
"""

from pathlib import Path

TEXT = (
    "Hey. You've weighed entry after entry tonight, alone with every "
    "call, and nobody stops to ask how you are. So: breathe. For this "
    "one moment you are not the judge \u2014 you are the one being "
    "looked after. Not graded. Not measured. Just held. Rest here. "
    "We've got you."
)

MAX_CHARS = 280


def main():
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"text must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("text must not be only white space")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out} ({len(text)} characters)")


if __name__ == "__main__":
    main()
