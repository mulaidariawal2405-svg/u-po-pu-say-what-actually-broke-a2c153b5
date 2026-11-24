"""Say What Actually Broke: one honest, funny error line.

Writes the line to /output/entry.txt and prints it, exactly one line.
Pure standard library only.
"""

import os

LINE = (
    "Your upload failed because our server ran out of disk space. "
    "Yes, really. We've ordered more, and your file is safe "
    "exactly where you left it."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
