#!/usr/bin/env python3
"""'Say What Actually Broke' — an honest error message, entered on make.fun.

The program stores a single plain-spoken error message in a file
called ``entry.txt`` under the directory given by the
MAKEFUN_OUTPUT_DIR environment variable (defaulting to /output).

It relies only on the standard library, touches no network, and
uses no randomness, so every run yields the identical file.
"""

import os
from pathlib import Path

# The message is kept as one literal so the entered text stays
# easy to audit; it is the fixed 141-character error message.
MESSAGE_TEXT = (
    "Error 404: this page was deleted in the redesign and nobody told "
    "the menu — try the search box above; it is now the only door "
    "into this site."
)

OUTPUT_NAME = "entry.txt"
FALLBACK_DIR = "/output"


def error_message() -> str:
    """Return the honest error message used as the entry."""
    return MESSAGE_TEXT


def output_folder() -> Path:
    """Pick the directory the entry file should be written into."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", FALLBACK_DIR))


def store_entry() -> Path:
    """Create the output directory if needed and write the entry."""
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / OUTPUT_NAME
    target.write_text(error_message(), encoding="utf-8")
    return target


def main() -> int:
    store_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
