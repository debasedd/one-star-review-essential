#!/usr/bin/env python3
"""One-Star Review of Something Essential — the funniest deadpan
one-star review, 160 characters or fewer, of an everyday essential.

The review: a complaint filed in earnest against sleep, the one
essential nobody can return. The grievance is the sharpest true one
— sleep promises rest and instead screens a 3 a.m. rerun of every
embarrassing thing ever said — and the sting turns in the last few
words, when the rerun's start date turns out to be 2009. Deadpan
throughout: one star, no winking, no exclamation marks.

Line: "One star. Sleep promised eight hours of rest and delivered a 3 a.m. rerun of every embarrassing thing I've said since 2009."
"""

import os

LINE = "One star. Sleep promised eight hours of rest and delivered a 3 a.m. rerun of every embarrassing thing I've said since 2009."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
