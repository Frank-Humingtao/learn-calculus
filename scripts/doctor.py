#!/usr/bin/env python3
"""环境自检：这台设备能不能接着学

  python3 scripts/doctor.py           学习档：python、git、gh 登录与权限、label、进度映射、代码与素材是否最新
  python3 scripts/doctor.py --prep    另查备课档（pymupdf、mlx-whisper、ffmpeg、MinerU；只在 Mac 上需要）

只用标准库，不需要先装 .venv。每项打印 ✓ / ⚠️ / ✗：
  ✗  学不了，先修（配环境：.agents/skills/learn-setup/SKILL.md）
  ⚠️  能学但有降级或有更新（检查更新：.agents/skills/learn-update/SKILL.md）
退出码：有 ✗ 为 1，否则 0。只读，不改任何东西（除了 git fetch）。
"""
import glob
import json
import os
import platform
import sys

from common import DEVICE_FILE, LEVELS, ROOT, device_name, find_gh, run, utf8_stdio

WIN = platform.system() == "Windows"
PY = "py" if WIN else "python3"
results = []


def report(level, name, detail="", fix=""):
    results.append(level)
    icon = {"ok": "✓", "warn": "⚠️", "fail": "✗"}[level]
    print("%s %s%s" % (icon, name, "：" + detail if detail else ""))
    if fix and level != "ok":
        for line in fix.splitlines():
            print("    → " + line)


def check_python():
    v = sys.version_info
    s = "%d.%d.%d（%s）" % (v[0], v[1], v[2], sys.executable)
    if v < (3, 8):
        report("fail", "Python", s + "，需要 ≥ 3.8", "装新版 Python 3")
    else:
        report("ok", "Python", s + ("；本设备用 `py` 运行脚本" if WIN else ""))


def check_git():
    code, out, _ = run(["git", "--version"])
    if code != 0:
        report("fail", "git", "找不到", "Windows: winget install Git.Git；Linux: 包管理器装 git")
        return None
    code, url, _ = run(["git", "remote", "get-url", "origin"])
    if code != 0:
        report("fail", "git 仓库", "没有 origin 远端", "在 git clone 下来的仓库目录里运行")
        return None
    report("ok", "git", "%s；origin = %s" % (out.strip(), url.strip()))
    return True


def check_gh():
    exe = find_gh()
    if not exe:
        report("fail", "gh（GitHub CLI）", "找不到",
               "Windows: winget install GitHub.cli（装完重开终端）\n"
               "macOS: brew install gh，或 bash scripts/setup.sh\n"
               "Linux: 见 https://github.com/cli/cli/blob/trunk/docs/install_linux.md ；无 sudo 时下载 linux_amd64.tar.gz 解压到 ~/.local/bin")
        return None
    code, _, err = run([exe, "auth", "status"])
    via = "GH_TOKEN 环境变量" if os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") else "gh auth login"
    if code != 0:
        report("fail", "gh 登录", "未登录（%s）" % err.strip().splitlines()[-1] if err.strip() else "未登录",
               "%s auth login   （或设置 GH_TOKEN：fine-grained PAT，仅本仓库，Issues 读写 + Contents 只读）" % exe)
        return None
    report("ok", "gh", "%s；已登录（%s）" % (exe, via))
    return exe


def check_repo(gh):
    code, out, err = run([gh, "repo", "view", "--json", "nameWithOwner,viewerPermission"])
    if code != 0:
        report("fail", "仓库访问", err.strip() or "失败", "确认登录的账号能访问这个私有仓库")
        return False
    d = json.loads(out)
    perm = d.get("viewerPermission") or ""
    if perm in ("ADMIN", "MAINTAIN", "WRITE", "TRIAGE"):
        report("ok", "仓库权限", "%s（%s）" % (d["nameWithOwner"], perm))
        return True
    report("fail", "仓库权限", "%s 只有 %s，改不了 issue" % (d["nameWithOwner"], perm or "未知"),
           "换有写权限的账号，或给 PAT 加 Issues: Read and write")
    return False


def check_labels(gh):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from tracker import LABELS, L_ERRATUM, L_NOTE
    code, out, _ = run([gh, "label", "list", "--limit", "200", "--json", "name", "--jq", ".[].name"])
    have = set(out.splitlines()) if code == 0 else set()
    missing = [n for n in LABELS if n not in have and n not in (L_ERRATUM, L_NOTE)]
    if missing:
        report("fail", "label", "缺 %s" % "、".join(missing), "%s scripts/tracker.py setup" % PY)
    else:
        report("ok", "label", "齐全")


def check_issues(gh):
    path = os.path.join(ROOT, "course", "issues.json")
    cards = glob.glob(os.path.join(LEVELS, "*.md"))
    if not os.path.exists(path):
        report("warn" if not cards else "fail", "进度映射", "没有 course/issues.json",
               "还没备课就正常；已有卡片则 %s scripts/tracker.py publish" % PY)
        return
    with open(path, encoding="utf-8") as f:
        mp = json.load(f)
    code, out, err = run([gh, "issue", "list", "--state", "all", "--limit", "1000", "--json", "number,state"])
    if code != 0:
        report("fail", "进度读取", err.strip(), "")
        return
    issues = {d["number"]: d["state"] for d in json.loads(out)}
    lost = sorted(k for k, n in mp.items() if n not in issues)
    if lost:
        report("fail", "进度映射", "%d 关在 GitHub 上找不到 issue：%s" % (len(lost), ", ".join(lost[:8])),
               "确认 origin 指向正确的仓库")
        return
    done = sum(1 for n in mp.values() if issues[n] == "CLOSED")
    report("ok", "进度", "%d 个关卡/boss 对上 GitHub issue，已掌握 %d" % (len(mp), done))


def check_sync():
    code, _, err = run(["git", "fetch", "-q", "origin"])
    if code != 0:
        report("warn", "代码同步", "git fetch 失败：%s" % err.strip(), "检查网络或 git 凭据")
        return
    code, head, _ = run(["git", "symbolic-ref", "-q", "--short", "refs/remotes/origin/HEAD"])
    base = head.strip() or "origin/main"
    _, behind, _ = run(["git", "rev-list", "--count", "HEAD.." + base])
    _, dirty, _ = run(["git", "status", "--porcelain", "--untracked-files=no"])
    behind = int(behind.strip() or 0)
    if behind:
        report("warn", "代码同步", "比 %s 落后 %d 个提交（卡片、skill 可能是旧的）" % (base, behind),
               "检查更新：.agents/skills/learn-update/SKILL.md（或 git pull）")
    else:
        report("ok", "代码同步", "与 %s 一致" % base)
    if dirty.strip():
        report("warn", "本地改动", "有未提交的修改；学习设备不改仓库文件，卡片有错记卡片勘误",
               "git status 看看是什么")


def check_sources(gh):
    from sources import has_files, latest_tag, local_tag, size_mb, tag_no
    lt, rt = local_tag(), (latest_tag() if gh else None)
    if not has_files():
        report("warn", "原始素材", "没下载（能学，但看不了教材原图）",
               "需要看图时：%s scripts/sources.py pull（%.0fMB）" % (PY, size_mb(rt)))
    elif rt and tag_no(lt) < tag_no(rt):
        report("warn", "原始素材", "本地 %s，最新 %s" % (lt or "无版本号", rt), "%s scripts/sources.py pull" % PY)
    else:
        report("ok", "原始素材", lt or "有（无版本号）")


def check_skills():
    skills = sorted(os.path.basename(os.path.dirname(p))
                    for p in glob.glob(os.path.join(ROOT, ".agents", "skills", "*", "SKILL.md")))
    if not skills:
        report("fail", "skill", ".agents/skills/ 里没有 SKILL.md", "重新 git clone")
        return
    report("ok", "skill", "、".join(skills))
    link = os.path.join(ROOT, ".claude", "skills")
    if not os.path.isdir(link):
        report("warn", ".claude/skills", "符号链接失效（只影响 Claude Code；Codex、Cursor 读 .agents/skills）",
               "Windows 上可忽略；需要时 git config core.symlinks true 后重新 checkout")


def check_device():
    if os.path.exists(DEVICE_FILE):
        report("ok", "设备名", device_name())
    else:
        report("warn", "设备名", "没设置，暂用 hostname「%s」" % device_name(),
               "起个名字，例如：echo win-codex > .learn-device")


def check_prep():
    print("\n—— 备课档 ——")
    if platform.system() != "Darwin":
        report("warn", "备课档", "只支持 macOS（mlx-whisper 需要 Apple Silicon），本设备只用来学习")
        return
    vpy = os.path.join(ROOT, ".venv", "bin", "python")
    if not os.path.exists(vpy):
        report("fail", ".venv", "没有", "bash scripts/setup.sh")
        return
    for mod, pkg in (("fitz", "pymupdf"), ("mlx_whisper", "mlx-whisper"), ("imageio_ffmpeg", "imageio-ffmpeg")):
        code, _, _ = run([vpy, "-c", "import " + mod])
        report("ok" if code == 0 else "fail", pkg, "" if code == 0 else "没装", "bash scripts/setup.sh")
    import shutil
    mineru = shutil.which("mineru") or os.path.exists(os.path.join(ROOT, ".venv", "bin", "mineru"))
    report("ok" if mineru else "warn", "MinerU", "" if mineru else "没装（只有扫描版 PDF 需要）",
           "见 scripts/ocr_pdf.py 开头的说明")


def main():
    utf8_stdio()
    prep = "--prep" in sys.argv[1:]
    print("设备：%s  系统：%s %s\n" % (device_name(), platform.system(), platform.release()))
    check_python()
    git_ok = check_git()
    gh = check_gh()
    if gh and check_repo(gh):
        check_labels(gh)
        check_issues(gh)
    if git_ok:
        check_sync()
    check_skills()
    check_sources(gh)
    check_device()
    n_fail, n_warn = results.count("fail"), results.count("warn")
    if prep:
        k = len(results)
        check_prep()
        prep_fail = results[k:].count("fail")
    print()
    if prep and prep_fail:
        print("✗ 备课档缺 %d 项（不影响学习）→ bash scripts/setup.sh" % prep_fail)
    if n_fail:
        print("✗ %d 项要先修才能学 → 配环境：.agents/skills/learn-setup/SKILL.md" % n_fail)
    elif n_warn:
        print("✓ 可以学（%d 项提示，见 ⚠️）" % n_warn)
    else:
        print("✓ 一切就绪")
    sys.exit(1 if n_fail or (prep and prep_fail) else 0)


if __name__ == "__main__":
    main()
