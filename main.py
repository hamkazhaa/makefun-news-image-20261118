#!/usr/bin/env python3
"""World news of Wednesday 18 November 2026, summed up in one image.

The entry image is the entry.png beside this file: a front page built for
this bounty -- a dramatic illustration of the day (a collapsed bridge arch
under a drone-filled dusk sky, a cyclone wall on the horizon) above five
verified headlines from 18 November 2026.

This program copies entry.png to /output/entry.png (or $MAKEFUN_OUTPUT_DIR,
or the directory named by argv[1]) byte for byte, so every run writes
identical bytes. Standard library only, no network, no randomness.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv):
    if len(argv) > 1:
        out_dir = Path(argv[1])
    else:
        out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Verify the copy byte for byte: a truncated or partial write must fail
    # loudly instead of handing the judge a corrupt image.
    if _sha256(SOURCE) != _sha256(target):
        raise SystemExit("entry.png copy failed verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
