#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one brutally honest software error message to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LINE = (
    "Error 404: this page was deleted in the redesign and nobody told "
    "the menu — try the search box above; it is now the only door "
    "into this site."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
