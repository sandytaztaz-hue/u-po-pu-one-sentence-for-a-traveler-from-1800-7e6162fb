# One Sentence for a Traveler from 1800 — make.fun entry program.
#
# Writes a single sentence (125 characters) to /output/entry.txt that
# explains the modern internet to someone who has just stepped out of
# the year 1800, using only words and pictures that person could hold
# in their head: a harbour, ships from every shore, letters, songs and
# gossip arriving at your door, faster than any horse could ride.
#
# Deterministic: the same bytes on every run, no input, no clock, no
# randomness. The output directory is created if it does not exist.
# No trailing newline: the file holds exactly the sentence, nothing else.
# The sentence is one breath long and every word in it is one a person
# from 1800 would already know — no word coined after their time.

import os

ENTRY = (
    "It is a harbour where ships from every shore unload letters, songs "
    "and gossip at your door, faster than any horse could ride."
)


def main():
    out_file = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out_file, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the expected sentence")
    if not 1 <= len(written) <= 200:
        raise SystemExit("entry length outside the 1-200 character gate")


if __name__ == "__main__":
    main()
