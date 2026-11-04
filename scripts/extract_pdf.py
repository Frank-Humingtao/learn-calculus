#!/usr/bin/env python3
"""PDF → course/extracted/<名>.md，每页以 <!-- page N --> 开头

  python3 scripts/extract_pdf.py course/sources/book.pdf

文字太少的页会列出来：多半是扫描版，需要用 MinerU 做 OCR，
或让 AI 直接读那几页的 PDF 图像。
"""
import os
import sys

from common import EXTRACTED, stem


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    import fitz  # pymupdf

    src = sys.argv[1]
    doc = fitz.open(src)
    os.makedirs(EXTRACTED, exist_ok=True)
    out = os.path.join(EXTRACTED, stem(src) + ".md")
    sparse = []
    with open(out, "w", encoding="utf-8") as f:
        f.write("# %s\n\nsource: %s\npages: %d\n\n" % (stem(src), os.path.basename(src), len(doc)))
        for i, page in enumerate(doc, 1):
            text = page.get_text("text").strip()
            if len(text) < 50:
                sparse.append(i)
            f.write("<!-- page %d -->\n%s\n\n" % (i, text))
    print("✓ %s（%d 页）" % (os.path.relpath(out), len(doc)))
    if len(sparse) > len(doc) * 0.3:
        print("⚠ %d/%d 页几乎没有文字，可能是扫描版，需要 OCR（MinerU）" % (len(sparse), len(doc)))
    elif sparse:
        print("  文字很少的页：%s" % ", ".join(map(str, sparse[:30])))


if __name__ == "__main__":
    main()
