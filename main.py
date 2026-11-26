#!/usr/bin/env python3
"""Write one office-life joke to /output/entry.txt.

Pure Python 3 standard library. No network, no files read, no randomness:
both runs write identical bytes.

Run:  MAKEFUN_OUTPUT_DIR=out python3 main.py   ->  out/entry.txt
"""

import os

JOKE = (
    "I told my manager I was blocked, so she booked a meeting to unblock "
    "me \u2014 now I\u2019m blocked by the meeting about being blocked."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
