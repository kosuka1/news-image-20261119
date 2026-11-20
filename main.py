#!/usr/bin/env python3
"""Write this entry's image to /output/entry.png.

The image (image.png, kept beside this file) is a one-page newspaper
front page that sums up the world news of Thursday, 19 November 2026:

- the Trump-Xi-Putin summit in Shenzhen and its joint declaration,
- the International Court of Justice ruling that Myanmar committed
  genocide against the Rohingya,
- Anthropic's record $81 billion IPO,
- Iran's strikes in the Gulf and the Strait of Hormuz tension,
- the European Union's 45 billion euro loan for Ukraine.

The program only copies those bytes to the output path, so it needs
no network and every run writes exactly the same file.
"""

import filecmp
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "image.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # The judge must see exactly the stored front page: fail loudly if
    # the copy is not byte for byte the image the repository holds.
    if not filecmp.cmp(SOURCE, OUTPUT, shallow=False):
        raise SystemExit("copied image differs from image.png")


if __name__ == "__main__":
    main()
