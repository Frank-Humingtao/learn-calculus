#!/usr/bin/env python3
"""从视频截取关键帧（板书/幻灯片）→ course/frames/<名>/HHMMSS.jpg + index.md

  python3 scripts/keyframes.py course/sources/lec01.mp4 [--scene 0.3] [--every 60]

画面变化超过 --scene 阈值时截一张；画面一直不变（摄像机对着黑板）时至少每 --every 秒截一张。
闯关时只看该关视频时间段内的几张图即可。
"""
import argparse
import glob
import os
import re
import subprocess

from common import FRAMES, ffmpeg_exe, hms, stem


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--scene", type=float, default=0.3)
    ap.add_argument("--every", type=int, default=60)
    ap.add_argument("--width", type=int, default=960)
    a = ap.parse_args()

    out_dir = os.path.join(FRAMES, stem(a.video))
    os.makedirs(out_dir, exist_ok=True)
    for old in glob.glob(os.path.join(out_dir, "*.jpg")):
        os.remove(old)

    select = "gt(scene\\,{s})+isnan(prev_selected_t)+gte(t-prev_selected_t\\,{e})".format(s=a.scene, e=a.every)
    vf = "select='{sel}',scale={w}:-2,showinfo".format(sel=select, w=a.width)
    tmp = os.path.join(out_dir, "tmp_%05d.jpg")
    p = subprocess.run([ffmpeg_exe(), "-hide_banner", "-i", a.video, "-vf", vf, "-fps_mode", "vfr", "-q:v", "4", tmp],
                       stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        raise SystemExit(p.stderr[-2000:])
    times = [float(t) for t in re.findall(r"pts_time:([\d.]+)", p.stderr)]
    files = sorted(glob.glob(os.path.join(out_dir, "tmp_*.jpg")))
    names = []
    for f, t in zip(files, times):
        name = hms(t).replace(":", "") + ".jpg"
        os.replace(f, os.path.join(out_dir, name))
        names.append((t, name))
    with open(os.path.join(out_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("# %s 关键帧\n\nsource: %s\n\n" % (stem(a.video), os.path.basename(a.video)))
        for t, name in names:
            f.write("- %s  %s\n" % (hms(t), name))
    print("✓ %s（%d 张）" % (os.path.relpath(out_dir), len(names)))


if __name__ == "__main__":
    main()
