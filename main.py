#!/usr/bin/env python3
"""Write one dad joke to /output/entry.txt.

The joke is a single line, well under the 200-character cap, with the
punchline at the end so it reads naturally when told out loud.
"""

import os

JOKE = "I always carry a pencil, just in case I need to draw the line somewhere."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
