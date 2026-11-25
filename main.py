#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One-Line Robot Wedding Vows — writes the winning vow to /output/entry.txt."""
import os

VOW = "I promise to love you at 100% and at 1%, give you my only charging port first, and never trade you in for a newer model."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
