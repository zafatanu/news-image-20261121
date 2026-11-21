#!/usr/bin/env python3
"""Entry point: copy the shipped front-page image to the harness output dir.

The image (entry.png, 1024x1024, <=1 MiB) is drawn by render.py from
page.html in this repository and shipped beside this file. This program
does no drawing, no network and no randomness: it only copies those
exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png), so repeated runs
are byte-identical by construction.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print("entry.png missing beside main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
