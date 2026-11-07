#!/usr/bin/env python3
"""原始素材的分发：course/sources/ 不进 git，打包放在 GitHub Release「sources-vN」（见 docs/adr/0001）

  status     本地素材版本 vs 最新 Release
  pull       下载最新（或 --tag 指定）版本并解压到 course/sources/（大小见 status）
  publish    把本地 course/sources/ 打包发布为下一个 sources-vN（备课后在 Mac 上用）

只用标准库 + gh，Windows / Linux / macOS 通用。
"""
import argparse
import os
import re
import shutil
import sys
import tempfile
import zipfile

from common import COURSE, find_gh, run, utf8_stdio

SOURCES = os.path.join(COURSE, "sources")
VERSION_FILE = os.path.join(SOURCES, ".version")
ASSET = "sources.zip"
SKIP = {"README.md", ".version", ".DS_Store"}


def gh(*args):
    exe = find_gh()
    if not exe:
        sys.exit("找不到 gh：先配环境")
    code, out, err = run([exe] + list(args))
    if code != 0:
        sys.exit("gh %s 失败：%s" % (" ".join(args[:3]), err.strip()))
    return out


def tag_no(tag):
    m = re.fullmatch(r"sources-v(\d+)", tag or "")
    return int(m.group(1)) if m else 0


def latest_tag():
    """最新的 sources-vN；查不到返回 None（gh 不可用时也返回 None，不退出）"""
    exe = find_gh()
    if not exe:
        return None
    code, out, _ = run([exe, "release", "list", "--limit", "100", "--json", "tagName", "--jq", ".[].tagName"])
    if code != 0:
        return None
    tags = [t for t in out.split() if tag_no(t)]
    return max(tags, key=tag_no) if tags else ""


def size_mb(tag):
    """Release 里压缩包的大小（MB）；查不到返回 0"""
    exe = find_gh()
    if not exe or not tag:
        return 0
    code, out, _ = run([exe, "release", "view", tag, "--json", "assets",
                        "--jq", '.assets[] | select(.name == "%s") | .size' % ASSET])
    return int(out.strip()) / 1e6 if code == 0 and out.strip().isdigit() else 0


def local_tag():
    try:
        with open(VERSION_FILE, encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


def has_files():
    return any(n not in SKIP for n in os.listdir(SOURCES)) if os.path.isdir(SOURCES) else False


def cmd_status(a):
    lt, rt = local_tag(), latest_tag()
    print("本地：%s" % (lt or ("有文件但无版本号" if has_files() else "无")))
    print("最新：%s" % ("%s（%.0fMB）" % (rt, size_mb(rt)) if rt else "（查不到 Release）"))
    if rt and tag_no(lt) < tag_no(rt):
        print("→ python3 scripts/sources.py pull")


def cmd_pull(a):
    tag = a.tag or latest_tag()
    if not tag:
        sys.exit("仓库里还没有 sources-vN Release")
    tmp = tempfile.mkdtemp()
    try:
        print("下载 %s（%.0fMB，稍等）…" % (tag, size_mb(tag)))
        gh("release", "download", tag, "--pattern", ASSET, "--dir", tmp, "--clobber")
        with zipfile.ZipFile(os.path.join(tmp, ASSET)) as z:
            root = os.path.realpath(SOURCES)
            for name in z.namelist():
                dest = os.path.realpath(os.path.join(SOURCES, name))
                if not dest.startswith(root + os.sep):
                    sys.exit("压缩包里有可疑路径：%s" % name)
            z.extractall(SOURCES)
            n = len(z.namelist())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        f.write(tag + "\n")
    print("✓ %s：%d 个文件已解压到 course/sources/" % (tag, n))


def cmd_publish(a):
    if not has_files():
        sys.exit("course/sources/ 里没有素材")
    rt = latest_tag()
    if rt is None:
        sys.exit("查不到 Release（gh 未登录？）")
    tag = "sources-v%d" % (tag_no(rt) + 1)
    tmp = tempfile.mkdtemp()
    try:
        zpath = os.path.join(tmp, ASSET)
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_STORED) as z:
            for d, dirs, fs in os.walk(SOURCES):
                for f in sorted(fs):
                    rel = os.path.relpath(os.path.join(d, f), SOURCES)
                    if f in SKIP and os.path.dirname(rel) == "" or f == ".DS_Store":
                        continue
                    z.write(os.path.join(d, f), rel.replace(os.sep, "/"))
            n = len(z.namelist())
        print("上传 %s：%d 个文件、%.0fMB（几百 MB 要十几分钟）…" % (tag, n, os.path.getsize(zpath) / 1e6))
        gh("release", "create", tag, zpath, "--title", "原始素材 " + tag.split("-")[1],
           "--notes", "course/sources/ 的原件，%d 个文件。用 python3 scripts/sources.py pull 下载解压。" % n)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        f.write(tag + "\n")
    print("✓ 已发布 %s" % tag)


def main():
    utf8_stdio()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(f=cmd_status)
    p = sub.add_parser("pull"); p.add_argument("--tag"); p.set_defaults(f=cmd_pull)
    sub.add_parser("publish").set_defaults(f=cmd_publish)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
