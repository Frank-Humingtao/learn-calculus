#!/usr/bin/env python3
"""视频 → course/extracted/<名>.transcript.md（约 30 秒一段，带时间戳）

  # 有字幕（.srt/.vtt）：最快，不需要转写
  python3 scripts/extract_video.py course/sources/lec01.mp4 --subs course/sources/lec01.srt
  # 与视频同名的 .srt/.vtt 会被自动使用
  python3 scripts/extract_video.py course/sources/lec01.mp4
  # 没有字幕：用 mlx-whisper 在本地转写（Apple Silicon）
  python3 scripts/extract_video.py course/sources/lec01.mp4 --lang en
"""
import argparse
import os
import re

from common import EXTRACTED, hms, parse_hms, stem

WHISPER_MODEL = "mlx-community/whisper-large-v3-turbo"


def read_subs(path):
    with open(path, encoding="utf-8-sig") as f:
        content = f.read()
    segs = []
    for block in re.split(r"\n\s*\n", content):
        lines = [l for l in block.strip().splitlines() if l.strip()]
        for i, l in enumerate(lines):
            m = re.match(r"([\d:.,]+)\s*-->\s*([\d:.,]+)", l)
            if m:
                text = " ".join(re.sub(r"<[^>]+>", "", x) for x in lines[i + 1:]).strip()
                if text:
                    segs.append((parse_hms(m.group(1)), parse_hms(m.group(2)), text))
                break
    return segs


def transcribe(path, lang):
    import mlx_whisper
    _ensure_ffmpeg_name()  # mlx-whisper 通过 PATH 调用 ffmpeg
    r = mlx_whisper.transcribe(path, path_or_hf_repo=WHISPER_MODEL, language=lang, verbose=False)
    return [(s["start"], s["end"], s["text"].strip()) for s in r["segments"]]


def _ensure_ffmpeg_name():
    """imageio-ffmpeg 的可执行文件名带版本号；在 venv/bin 里放一个名为 ffmpeg 的链接"""
    import shutil
    import sys
    from common import ffmpeg_exe
    if shutil.which("ffmpeg"):
        return
    link = os.path.join(os.path.dirname(sys.executable), "ffmpeg")
    if not os.path.exists(link):
        os.symlink(ffmpeg_exe(), link)
    os.environ["PATH"] = os.path.dirname(link) + os.pathsep + os.environ["PATH"]


def merge(segs, window=30.0):
    out, cur = [], None
    for st, en, tx in segs:
        if cur and en - cur[0] <= window:
            cur = (cur[0], en, cur[2] + " " + tx)
        else:
            if cur:
                out.append(cur)
            cur = (st, en, tx)
    if cur:
        out.append(cur)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--subs")
    ap.add_argument("--lang", help="en / zh …；不填自动识别")
    a = ap.parse_args()

    subs = a.subs
    if not subs:
        base = os.path.splitext(a.video)[0]
        for ext in (".srt", ".vtt", ".en.srt", ".en.vtt", ".zh.srt"):
            if os.path.exists(base + ext):
                subs = base + ext
                break
    segs = read_subs(subs) if subs else transcribe(a.video, a.lang)

    os.makedirs(EXTRACTED, exist_ok=True)
    out = os.path.join(EXTRACTED, stem(a.video) + ".transcript.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# %s 文字稿\n\nsource: %s\ntext: %s\n\n" % (
            stem(a.video), os.path.basename(a.video), "字幕 " + os.path.basename(subs) if subs else "whisper 转写"))
        for st, en, tx in merge(segs):
            f.write("[%s - %s] %s\n\n" % (hms(st), hms(en), tx))
    dur = hms(segs[-1][1]) if segs else "0"
    print("✓ %s（%s，%s）" % (os.path.relpath(out), dur, "字幕" if subs else "转写"))


if __name__ == "__main__":
    main()
