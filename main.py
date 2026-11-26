"""The Printer Apology — a one-line apology note from an office printer.

The printer apologises to the people who keep jamming it, feeding it
cheap paper and swearing at it. The entry is a single line of at most
120 characters, printed deterministically.
"""

APOLOGY = (
    "Sorry I jammed on page 2 of your 40-page report \u2014 "
    "you feed me discount paper, then slap me when I choke on it."
)

MAX_CHARS = 120


def get_apology() -> str:
    """Return the printer's apology line, guaranteed within the limit."""
    assert len(APOLOGY) <= MAX_CHARS, f"apology is {len(APOLOGY)} chars, over {MAX_CHARS}"
    return APOLOGY


def main() -> None:
    print(get_apology())


if __name__ == "__main__":
    main()
