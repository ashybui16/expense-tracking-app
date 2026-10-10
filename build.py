#!/usr/bin/env python3
"""Build index.html from src/tally.html.

src/tally.html is written as a page fragment (title, styles, markup, script) so it can be
published as-is to claude.ai, which supplies the <!doctype>/<head>/<body> skeleton.
This script adds that skeleton so the app also runs as a plain local file.

    python3 build.py          # writes index.html
    python3 build.py --serve  # also serves it at http://localhost:8000
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "tally.html"
OUT = ROOT / "index.html"
SPLIT = '<div class="wrap">'


def build() -> None:
    frag = SRC.read_text(encoding="utf-8")
    head, sep, body = frag.partition(SPLIT)
    if not sep:
        sys.exit(f"build: couldn't find {SPLIT!r} in {SRC}")
    OUT.write_text(
        "<!doctype html>\n<html lang=\"vi\">\n<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        f"{head.strip()}\n</head>\n<body>\n{SPLIT}{body.rstrip()}\n</body>\n</html>\n",
        encoding="utf-8",
    )
    print(f"build: wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
        print("serving at http://localhost:8000  (Ctrl+C to stop)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
