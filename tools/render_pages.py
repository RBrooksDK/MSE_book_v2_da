"""Render selected PDF pages to PNG for visual inspection.

Usage: python tools/render_pages.py file.pdf outdir 1 3 5-7 [--dpi 80]
"""
import pathlib
import sys

import fitz

args = sys.argv[1:]
dpi = 80
if "--dpi" in args:
    i = args.index("--dpi")
    dpi = int(args[i + 1])
    del args[i:i + 2]
pdf, out, pages = args[0], pathlib.Path(args[1]), args[2:]
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
wanted = []
for p in pages:
    if "-" in p:
        a, b = map(int, p.split("-"))
        wanted += range(a, b + 1)
    else:
        wanted.append(int(p))
for n in wanted:
    if 1 <= n <= doc.page_count:
        pix = doc[n - 1].get_pixmap(dpi=dpi)
        target = out / f"{pathlib.Path(pdf).stem}_p{n:03d}.png"
        pix.save(target)
        print(target)
print(f"{doc.page_count} pages")
