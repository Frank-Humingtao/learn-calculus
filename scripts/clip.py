#!/usr/bin/env python3
"""切出视频片段并打开

  python3 scripts/clip.py course/sources/lec01.mp4 00:12:30 00:18:00 [--no-open]
  → course/clips/lec01_001230-001800.mp4（不提交 git，可随时删）
"""
import argparse
import os
import subprocess
import sys

from common import COURSE, ffmpeg_exe, stem


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("start")
    ap.add_argument("end")
    ap.add_argument("--no-open", action="store_true")
    a = ap.parse_args()

    out_dir = os.path.join(COURSE, "clips")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "%s_%s-%s.mp4" % (stem(a.video), a.start.replace(":", ""), a.end.replace(":", "")))
    if not os.path.exists(out):
        subprocess.run([ffmpeg_exe(), "-loglevel", "error", "-ss", a.start, "-to", a.end,
                        "-i", a.video, "-c", "copy", out], check=True)
    print("✓ %s" % os.path.relpath(out))
    if not a.no_open and sys.platform == "darwin":
        subprocess.run(["open", out])


if __name__ == "__main__":
    main()
