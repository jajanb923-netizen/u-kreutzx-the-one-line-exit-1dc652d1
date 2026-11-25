"""The One-Line Exit — the funniest single-line resignation letter.

The program writes exactly one resignation letter, exactly one line long,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Python 3.13 standard library only. Deterministic, no network, no secrets.
Before writing, the letter is validated against the competition gate from
RULES.txt: UTF-8 text, 1 to 140 characters including the trailing newline,
a single line, not only whitespace.
"""

import os
import sys

# The winning line, chosen in CANDIDATES.md from a field of 10 and scored
# 24/25 against the judge's criteria: the office worker whose resignation
# letter is itself the last email. The hated phrase "per my last email"
# turns back on itself — the setup is the grievance, the punchline is the
# resignation, and the letter is the last email. 107 characters, the
# shortest of the top three candidates, which also wins exact ties.
LINE = (
    'Dear boss, I quit: after three years of writing "per my last email," '
    "I have decided to write my last email."
)

MAX_CHARS = 140


def validate(text):
    """Check the letter against the gate; return a list of failures."""
    failures = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if text.strip() == "":
        failures.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError:
        failures.append("entry is not valid UTF-8")
        encoded = b""
    # The file carries the line plus one trailing newline; the gate counts
    # the file's characters, so the newline is part of the budget.
    total = len(text) + 1
    if not 1 <= total <= MAX_CHARS:
        failures.append(
            "entry file is %d characters, gate allows 1-%d"
            % (total, MAX_CHARS)
        )
    return failures


def write_entry(out_dir):
    """Validate the letter and write it to <out_dir>/entry.txt."""
    failures = validate(LINE)
    if failures:
        raise ValueError("; ".join(failures))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
