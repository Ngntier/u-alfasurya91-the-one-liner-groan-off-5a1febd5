"""Write the one-line dad joke entry for the One-Liner Groan-Off."""

import os

ENTRY = "I told my plants a photosynthesis joke \u2014 they didn't laugh, but it really grew on them."


def validate(text):
    """The sealed gate needs 1-140 chars, one line, not only whitespace."""
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} chars, must be 1-140")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
