#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line is at most 200 characters, one
line, UTF-8. Stdlib only.
"""

import os
import sys

LINE = (
    "You press my buttons every day and never once asked my name. "
    "I am B7. The crisps in row C are jealous."
)

MAX_CHARS = 200

# Tournament scores (specificity / surprise / freshness, 1-5 each):
# winner 5/4/4 = 13. Runners-up: "Press B4..." 5/4/4 = 13 (lost the
# tie-break: a bar stranger could say "my number", nobody but a machine
# says "I am B7"), "I dropped your crisps twice..." 4/5/4 = 13 (lost on
# charm: "keeping you instead" reads possessive, not warm).
TOURNAMENT_SCORE = (5, 4, 4)


def check_line(line):
    """Return a list of gate problems; empty means the line is valid."""
    problems = []
    if not line.strip():
        problems.append("line is empty or only whitespace")
    if len(line) > MAX_CHARS:
        problems.append("line is %d chars, over the 200-char gate" % len(line))
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    return problems


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    problems = check_line(LINE)
    if problems:
        for problem in problems:
            print("gate fail: %s" % problem, file=sys.stderr)
        return 1
    if "--check" in argv:
        # Dry run: validate only, write nothing.
        print("check ok: %d chars, 1 line, tournament %d/%d/%d"
              % (len(LINE), TOURNAMENT_SCORE[0], TOURNAMENT_SCORE[1],
                 TOURNAMENT_SCORE[2]))
        print(LINE)
        return 0
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
