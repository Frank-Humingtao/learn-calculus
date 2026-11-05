#!/usr/bin/env python3
"""扫描版 PDF → MinerU 本地 OCR → course/extracted/<名>.md

  python3 scripts/ocr_pdf.py course/sources/book.pdf     # 单个文件
  python3 scripts/ocr_pdf.py course/sources/scans/       # 整个目录（只加载一次模型）
  python3 scripts/ocr_pdf.py --convert-only              # 只把已有 JSON 重新转成 md

需要 mineru-kit（MinerU ≥ 3，独立安装，见 setup.sh 注释）。
MinerU 的原始输出（middle_json）放在 course/extracted/.mineru/，不提交 git。
产物格式同 extract_pdf.py：每页以 <!-- page N --> 开头，有印刷页码时写成
<!-- page N | p.105 -->；公式为 LaTeX，插图只保留图注。
"""
import glob
import json
import os
import shutil
import subprocess
import sys

from common import EXTRACTED, stem

RAW = os.path.join(EXTRACTED, ".mineru")
SKIP = {"header", "footer", "page_number", "page_footnote"}


def mineru_kit():
    exe = shutil.which("mineru-kit") or os.path.expanduser("~/.local/bin/mineru-kit")
    if not os.path.exists(exe):
        sys.exit("找不到 mineru-kit：先 `uv tool install --python 3.12 'mineru[all]'`")
    return exe


def inline(c):
    """把 MinerU 的 content（字符串或嵌套片段）拼成一行 markdown"""
    if isinstance(c, str):
        return c
    if isinstance(c, dict):
        t = c.get("type")
        if t == "equation_inline":
            return " $%s$ " % c["content"].strip()
        if t == "image_body":
            return ""
        return inline(c.get("content", ""))
    if isinstance(c, list):
        return "".join(inline(x) for x in c)
    return ""


def render_block(b):
    t = b.get("type")
    if t in SKIP:
        return None
    if t == "paragraph_title" or t == "title":
        return "#" * min(b.get("level", 2) + 1, 6) + " " + inline(b["content"]).strip()
    if t in ("equation", "interline_equation"):
        return "$$\n%s\n$$" % inline(b["content"]).strip()
    if t == "image":
        caps = [inline(x).strip() for x in b.get("content", [])
                if isinstance(x, dict) and x.get("type") != "image_body"]
        return "[图] " + " ".join(c for c in caps if c)
    if t == "table":
        return "[表]\n" + inline(b.get("content", "")).strip()
    text = inline(b.get("content", "")).strip()
    return text or None


def page_number(blocks):
    for b in blocks:
        if b.get("type") == "page_number":
            s = inline(b["content"]).strip()
            if s.isdigit():
                return s
    return None


def convert(json_path, name):
    d = json.load(open(json_path, encoding="utf-8"))
    pages = d["pages"]
    out = os.path.join(EXTRACTED, name + ".md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# %s\n\nsource: %s.pdf\npages: %d\nocr: mineru\n\n" % (name, name, len(pages)))
        for p in pages:
            n = p["page_idx"] + 1
            printed = page_number(p["blocks"])
            f.write("<!-- page %d%s -->\n" % (n, " | p.%s" % printed if printed else ""))
            parts = [r for r in (render_block(b) for b in p["blocks"]) if r]
            f.write("\n\n".join(parts) + "\n\n")
    print("✓ %s（%d 页）" % (os.path.relpath(out), len(pages)))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    os.makedirs(RAW, exist_ok=True)
    if args != ["--convert-only"]:
        env = dict(os.environ)
        env.setdefault("MINERU_MODEL_SOURCE", "modelscope")
        cmd = [mineru_kit(), "parse", *args, "-p", "all", "--tier", "standard",
               "--ocr-mode", "ocr", "-f", "middle_json", "-o", RAW]
        subprocess.run(cmd, check=True, env=env)
    for j in sorted(glob.glob(os.path.join(RAW, "*.json"))):
        convert(j, stem(j))


if __name__ == "__main__":
    main()
