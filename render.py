#!/usr/bin/env python3
"""Render page.html to entry.png with the local headless Chrome.

No network: the page is loaded from file:// and every drawing is inline
SVG/CSS in page.html plus three raster lead images loaded from local files in
art/ (cop31.png, riyadh.png, peru.png), so the screenshot is fully
deterministic. The raw screenshot is re-saved through Pillow, which strips any
encoder variance, so the shipped bytes are stable: same pixels in, same bytes
out, every run.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = os.path.expanduser(
    "~/.agent-browser/browsers/chrome-157.0.8103.78/chrome"
)
PAGE = os.path.join(HERE, "page.html")
RAW = os.path.join(HERE, ".render-raw.png")
OUT = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576


def main():
    if not os.path.exists(CHROME):
        print("chrome binary missing: %s" % CHROME, file=sys.stderr)
        return 1
    if not os.path.exists(PAGE):
        print("page.html missing", file=sys.stderr)
        return 1
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--window-size=1024,1024",
        "--screenshot=" + RAW,
        "file://" + PAGE,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0 or not os.path.exists(RAW):
        print("chrome failed: %s" % proc.stderr.strip(), file=sys.stderr)
        return 1
    from PIL import Image

    img = Image.open(RAW)
    if img.size != (1024, 1024):
        img = img.resize((1024, 1024), Image.LANCZOS)
    img = img.convert("RGB")
    img.save(OUT, format="PNG", optimize=True)
    try:
        os.remove(RAW)
    except OSError:
        pass
    size = os.path.getsize(OUT)
    if size > MAX_BYTES:
        # JPEG bytes are allowed under the entry.png name; keep quality high.
        img.save(OUT, format="JPEG", quality=88, optimize=True)
        size = os.path.getsize(OUT)
    print("entry.png: %dx%d %d bytes" % (img.size[0], img.size[1], size))
    if size > MAX_BYTES:
        print("still over 1 MiB", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
