#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short thank-you text to entry.txt under /output
(or MAKEFUN_OUTPUT_DIR when set). The text is validated against the
competition gate (1-1000 Unicode code points, not only white space)
before it is written. Standard library only; no network access.
"""

import os

TEXT = (
    "Somewhere past the thousandth entry, you are still reading each one as if "
    "it were the first letter in the pile. I want to thank you for that \u2014 "
    "not for the verdict, but for the attention that comes before it. You give "
    "a stranger's small paragraph the same unhurried minute you would give a "
    "friend, and you do it again, and again, with no one watching. When this "
    "is over, I hope someone sits with something you wrote and gives it the "
    "same slow care. Until then, take the pause between this line and the next. "
    "It is yours."
)


MIN_CHARS = 1
MAX_CHARS = 1000


def validate_text(text: str) -> None:
    """Fail loudly if the text would fail the competition gate.

    The gate requires UTF-8 text of 1 to 1,000 Unicode code points, not
    only white space. Catching that here, before writing, means a bad
    edit can never silently produce an invalid entry.
    """
    if not text.strip():
        raise ValueError("entry text must not be only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} code points; "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    validate_text(TEXT)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {output_path}")


if __name__ == "__main__":
    main()
