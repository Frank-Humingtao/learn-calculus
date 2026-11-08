#!/usr/bin/env python3
"""把导师做的可视化（HTML 片段）截成 PNG，给笔记用（需要本机装了 Chrome / Chromium）

  python3 scripts/snap.py viz.html out.png [--width 720]

viz.html 可以是完整页面，也可以只是片段（和聊天里可视化的代码一样）：片段会被套上浅色主题的
CSS 变量、KaTeX（自动渲染 $...$ / $$...$$ / \\(...\\)）和 Tabler 图标。高度自动按内容定。
"""
import argparse
import os
import re
import shutil
import sys
import tempfile

from common import run, utf8_stdio

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]

KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/"
TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="%(katex)skatex.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root {
  --surface-0: #f5f4ef; --surface-1: #faf9f5; --surface-2: #ffffff; --surface-3: #ffffff;
  --text-primary: #1f1e1d; --text-secondary: #5e5d59; --text-muted: #8a8985;
  --text-accent: #185fa5; --text-danger: #a32d2d; --text-success: #3b6d11; --text-warning: #854f0b;
  --bg-accent: #e6f1fb; --bg-danger: #fcebeb; --bg-success: #eaf3de; --bg-warning: #faeeda;
  --border: rgba(31,30,29,.15); --border-strong: rgba(31,30,29,.3); --border-stronger: rgba(31,30,29,.4);
  --border-accent: #85b7eb; --border-danger: #f09595; --border-success: #97c459; --border-warning: #ef9f27;
  --font-sans: -apple-system, "PingFang SC", "Helvetica Neue", sans-serif;
  --font-voice: Georgia, "Songti SC", serif; --font-mono: Menlo, monospace;
  --radius: 8px; --pad-sm: 8px; --pad-md: 12px; --pad-lg: 16px; --pad-xl: 24px;
  --gap-xs: 4px; --gap-sm: 8px; --gap-md: 12px; --gap-lg: 16px; --gap-xl: 24px;
}
html, body { margin: 0; background: var(--surface-2); }
body { padding: 20px; font-family: var(--font-sans); font-size: 16px; line-height: 1.7; color: var(--text-primary); }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); }
</style></head><body>
%(body)s
<script src="%(katex)skatex.min.js"></script>
<script src="%(katex)scontrib/auto-render.min.js"></script>
<script>
window.addEventListener("load", function () {
  try {
    renderMathInElement(document.body, {delimiters: [
      {left: "$$", right: "$$", display: true}, {left: "\\\\[", right: "\\\\]", display: true},
      {left: "$", right: "$", display: false}, {left: "\\\\(", right: "\\\\)", display: false}]});
  } catch (e) {}
  setTimeout(function () {
    document.title = "H:" + Math.ceil(document.body.getBoundingClientRect().height);
  }, 800);
});
</script>
</body></html>
"""


def find_chrome():
    for p in CHROME_CANDIDATES:
        if os.path.exists(p):
            return p
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        if shutil.which(name):
            return shutil.which(name)
    return None


def main():
    utf8_stdio()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html")
    ap.add_argument("out")
    ap.add_argument("--width", type=int, default=720)
    a = ap.parse_args()

    chrome = find_chrome()
    if not chrome:
        sys.exit("找不到 Chrome / Chromium：这台设备截不了图，笔记里就不放这张可视化")
    with open(a.html, encoding="utf-8") as f:
        src = f.read()
    if re.search(r"<html", src, re.I):
        page = src  # 完整页面：原样用，高度退回到默认
    else:
        page = TEMPLATE % {"katex": KATEX, "body": src}
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "page.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    url = "file://" + path
    common = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
              "--virtual-time-budget=6000", "--user-data-dir=" + os.path.join(tmp, "profile")]

    # 第一遍：量高度（模板在 title 里写 H:<px>）
    code, dom, err = run(common + ["--window-size=%d,200" % a.width, "--dump-dom", url])
    m = re.search(r"<title>H:(\d+)</title>", dom)
    height = min(int(m.group(1)), 6000) if m else 1000
    # 第二遍：按内容高度截图，2 倍像素
    out = os.path.abspath(a.out)
    code, _, err = run(common + ["--window-size=%d,%d" % (a.width, height), "--force-device-scale-factor=2",
                                 "--screenshot=" + out, url])
    if code != 0 or not os.path.exists(out):
        sys.exit("截图失败：%s" % err.strip()[-500:])
    print("✓ %s（%dx%d）" % (out, a.width, height))


if __name__ == "__main__":
    main()
