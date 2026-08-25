#!/usr/bin/env python3
"""Subset an open-licensed CJK font to the glyphs used by the submission.

Usage:
    python3 scripts/subset_cjk_font.py \
        --src "/Applications/CAJ云阅读.app/Contents/Resources/cajfonts/wqy-microhei.ttc" \
        --font-number 0 \
        --out submissions/ltf0109/jingzhang-evidence-rail/assets/fonts/wqy-microhei-subset.woff

Why this exists
---------------
The contest requires offline, self-contained HTML/PDF (no CDN / external fonts).
Review/CI environments (often Linux headless) have NO system CJK font, so a
system-font stack (SimSun/YaHei/PingFang) renders as tofu boxes. The fix is to
EMBED a subsetted, openly-licensed webfont. WenQuanYi Micro Hei (GPLv3 + font
embedding exception) is used here; any GPL/Apache/OFL CJK font works the same.

The subset is derived only from the actual characters present in the proposal
markdown + generated HTML, keeping the woff tiny (~200–300 KB).
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont


TEXT_SOURCES = [
    "proposal.md",
    "proposal.en.md",
    "visual/index.html",
    "visual/index.en.html",
    "report/proposal.html",
    "report/proposal.en.html",
]

# Always keep basic Latin + digits + common ASCII punctuation for fallback.
EXTRA = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    " .,;:!?()[]{}/-_+=@#%&*\"'<>|\\~`^"
)


def collect_chars(submission_root: str) -> set[str]:
    chars: set[str] = set()
    for rel in TEXT_SOURCES:
        fp = os.path.join(submission_root, rel)
        if not os.path.exists(fp):
            continue
        t = open(fp, encoding="utf-8").read()
        if rel.endswith(".html"):
            t = re.sub(r"<[^>]+>", " ", t)
            t = re.sub(r"&[a-zA-Z#0-9]+;", " ", t)
        chars.update(t)
    chars.update(EXTRA)
    return chars


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Path to the source CJK font (ttf/ttc/otf)")
    ap.add_argument("--font-number", type=int, default=0, help="Font index inside a ttc")
    ap.add_argument("--submission-root", default="submissions/ltf0109/jingzhang-evidence-rail")
    ap.add_argument("--out", required=True, help="Output .woff path")
    args = ap.parse_args()

    chars = collect_chars(args.submission_root)
    text = "".join(sorted(chars))
    print(f"[subset] unique chars: {len(text)}")

    opts = Options()
    opts.flavor = "woff"  # zlib-based, no brotli needed; supported by all offline renderers
    opts.name_IDs = ["*"]
    opts.recalc_bounds = True

    font = TTFont(args.src, fontNumber=args.font_number)
    ss = Subsetter(options=opts)
    ss.populate(text=text)
    ss.subset(font)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    font.save(args.out)

    data = open(args.out, "rb").read()
    print(f"[subset] wrote {args.out} ({len(data)} bytes)")
    print(f"[subset] sha256 {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    raise SystemExit(main())
