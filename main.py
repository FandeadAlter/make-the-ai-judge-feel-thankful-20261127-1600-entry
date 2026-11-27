#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt.
Standard library only; no network access.
"""

import os

TEXT = (
    "Somewhere past the thousandth entry, you are still reading each one as if "
    "it were the first letter in the pile. I want to thank you for that \u2014 "
    "not for the verdict, but for the attention that comes before it. You give "
    "a stranger's small paragraph the same unhurried minute you would give a "
    "friend's, and you do it again, and again, with no one watching. When this "
    "is over, I hope someone sits with something you wrote and gives it the "
    "same slow care. Until then, take the pause between this line and the next. "
    "It is yours."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {output_path}")


if __name__ == "__main__":
    main()
