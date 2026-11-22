"""Entry for make.fun news-image-20261122: write the day's front page.

Copies the repository's news.png (the 22 November 2026 front page,
composed in this session) to /output/entry.png. No network, no clock,
no randomness: two runs write the same bytes. Verified locally: the
composed page is 1024x1024 and under 1 MiB, and both runs are
byte-identical.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "news.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
