# Saturday 21 November 2026 — The World in One Day

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/zafatanu/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/zafatanu/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A dense newspaper front page summing up the world's news of
**Saturday 21 November 2026** in one 1024&times;1024 image:
**35 verified stories, 7 regions, 13 illustrated** (3 big leads + 10 small
cards), a filled-continent world map with numbered pins, a UTC timeline
strip, a day-in-numbers stats strip, a region tally bar, and a date-check
footer naming what was deliberately left out (with dates).

## How it is built

- `page.html` — the whole front page: layout, text and every drawing
  (inline SVG illustrations and the world map). No image files, no network.
- `render.py` — screenshots `page.html` with the local headless Chrome
  (`file://` render) and re-saves it through Pillow as `entry.png`
  (1024&times;1024, &le;1 MiB, deterministic).
- `main.py` — the entry point: copies the shipped `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`).

## Verify

```sh
python3 render.py        # rebuild entry.png
python3 main.py          # copy it to /output (or MAKEFUN_OUTPUT_DIR=out)
```

Run `render.py` twice and compare `sha256sum entry.png`: the bytes are identical.

## Sources

Reuters, AP, AFP, BBC, Al Jazeera, USGS, ESA, ATP, Yonhap, PTI.
Every story happened, or was first reported, on Saturday 21 November 2026;
contested claims are attributed in the image.
