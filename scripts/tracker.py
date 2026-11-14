#!/usr/bin/env python3
"""关卡进度：GitHub Issues 的薄封装（需要已登录的 gh）

  setup                       创建状态 label（一次）
  publish [--dry-run]         course/levels/*.md → 每单元一个 milestone + 每关一个 issue + 每单元一个 boss issue
  status [--all]              进度总览 + 推荐下一关
  show <id>                   卡片路径、issue 状态、历史评论
  set <id> start|review|done|todo
  label <id> skip|startpoint|clear     摸底标注（skip 为旧用法，新摸底不再使用）
  clear-labels <单元号>                清掉该单元所有关卡的摸底标注
  comment <id> < record.md    在 issue 下追加一条学习/测试记录（或 --file record.md）
  erratum <id> < note.md      记一条卡片勘误：打「卡片勘误」label 并评论（或 --file note.md）
  erratum <id> --fixed        勘误已在卡片里改好：去掉 label
  note <id> [--file n.md] [--image a.png ...] [--intro 一句导读]
                              给学习者看的笔记：找到或创建该关的笔记 issue，上传图片，追加一条评论

状态：未开始=open 无状态 label；进行中=label「进行中」；待复习=label「待复习」；已掌握=closed
关卡 id 与 issue 编号的对应保存在 course/issues.json。
笔记 issue 带 label「笔记」、与关卡同 milestone、一直 open，按标题前缀 [<id>] 查找（不进 issues.json）。
笔记里的图片经 gh api 存到公开仓库 <本仓库名>-note-images 的 <id>/ 下（私有仓库的图手机 App 显示不出来）；正文里写 {{img1}} {{img2}} … 指定位置，没写的追加在末尾。
"""
import argparse
import glob
import json
import os
import re
import sys

from common import COURSE, LEVELS, ROOT, find_gh, run, utf8_stdio

ISSUES_JSON = os.path.join(COURSE, "issues.json")

L_DOING, L_REVIEW = "进行中", "待复习"
L_SKIP, L_START = "摸底:可跳过", "摸底:从这开始"
L_LEVEL, L_BOSS = "关卡", "boss"
L_ERRATUM = "卡片勘误"
L_NOTE = "笔记"
IMAGE_REPO_SUFFIX = "-note-images"
LABELS = {
    L_LEVEL: ("ededed", "一个关卡"),
    L_BOSS: ("b60205", "单元阶段测试"),
    L_DOING: ("fbca04", "正在学"),
    L_REVIEW: ("d93f0b", "需要复习"),
    L_SKIP: ("0e8a16", "摸底显示可能已掌握"),
    L_START: ("1d76db", "摸底显示从这里开始"),
    L_ERRATUM: ("5319e7", "卡片有错，等下次备课修正"),
    L_NOTE: ("0075ca", "给学习者回看的笔记"),
}
ICON = {"done": "✅", "doing": "🟡", "review": "🔁", "todo": "⬜"}


# ---------- gh ----------

def gh(*args, input=None, check=True):
    exe = find_gh()
    if not exe:
        sys.exit("找不到 gh：brew install gh 或 bash scripts/setup.sh，再 gh auth login")
    code, out, err = run([exe] + list(args), input=input)
    if check and code != 0:
        sys.exit("gh %s 失败：%s" % (" ".join(args[:3]), err.strip()))
    return out


def gh_json(*args):
    return json.loads(gh(*args) or "null")


# ---------- 卡片 ----------

def parse_card(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        sys.exit("卡片缺少 frontmatter：%s" % path)
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        meta[k.strip()] = v
    for k in ("id", "title", "unit", "question"):
        if not meta.get(k):
            sys.exit("卡片 %s 缺少字段 %s" % (path, k))
    meta.setdefault("prereqs", [])
    meta["body"] = m.group(2)
    meta["path"] = os.path.relpath(path, ROOT)
    return meta


def load_cards():
    return [parse_card(p) for p in sorted(glob.glob(os.path.join(LEVELS, "*.md")))]


def section(body, title):
    m = re.search(r"^##\s*%s\s*\n(.*?)(?=^##\s|\Z)" % re.escape(title), body, re.M | re.S)
    return m.group(1).strip() if m else ""


def units_of(cards):
    """[(unit_title, unit_key, [cards])]，unit_key 取 id 的第一段"""
    out = []
    for c in cards:
        key = c["id"].split("-")[0]
        if not out or out[-1][1] != key:
            out.append((c["unit"], key, []))
        out[-1][2].append(c)
    return out


def load_map():
    if os.path.exists(ISSUES_JSON):
        with open(ISSUES_JSON, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_map(mp):
    with open(ISSUES_JSON, "w", encoding="utf-8") as f:
        json.dump(mp, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


def issue_no(tid):
    mp = load_map()
    if tid not in mp:
        sys.exit("%s 还没有 issue（先 publish；用 status --all 查看全部 id）" % tid)
    return str(mp[tid])


# ---------- 命令 ----------

def cmd_setup(a):
    for name, (color, desc) in LABELS.items():
        gh("label", "create", name, "--color", color, "--description", desc, "--force")
    print("✓ 已创建 %d 个 label" % len(LABELS))


def cmd_publish(a):
    cards = load_cards()
    if not cards:
        sys.exit("course/levels/ 里还没有卡片")
    ids = [c["id"] for c in cards]
    for c in cards:
        for p in c["prereqs"]:
            if p not in ids or ids.index(p) >= ids.index(c["id"]):
                sys.exit("%s 的前置 %s 不存在或排在它后面" % (c["id"], p))
    mp = load_map()
    repo = "" if a.dry_run else gh_json("repo", "view", "--json", "nameWithOwner,defaultBranchRef")
    base = "" if a.dry_run else "https://github.com/%s/blob/%s/" % (repo["nameWithOwner"], repo["defaultBranchRef"]["name"])
    existing = set() if a.dry_run else {m["title"] for m in gh_json("api", "repos/{owner}/{repo}/milestones?state=all&per_page=100")}

    for unit, key, ucards in units_of(cards):
        if unit not in existing:
            print("+ milestone %s" % unit)
            if not a.dry_run:
                gh("api", "repos/{owner}/{repo}/milestones", "-f", "title=" + unit)
        for c in ucards:
            if c["id"] in mp:
                continue
            body = "**核心问题**：%s\n\n### 通关标准\n%s\n\n前置：%s\n\n📄 卡片：[%s](%s%s)\n" % (
                c["question"], section(c["body"], "通关标准") or "（见卡片）",
                ", ".join(c["prereqs"]) or "无", c["path"], base, c["path"])
            print("+ issue %s %s" % (c["id"], c["title"]))
            if not a.dry_run:
                url = gh("issue", "create", "--title", "[%s] %s" % (c["id"], c["title"]),
                         "--body", body, "--label", L_LEVEL, "--milestone", unit).strip()
                mp[c["id"]] = int(url.rsplit("/", 1)[1])
                save_map(mp)
        bid = key + "-boss"
        if bid not in mp:
            lst = "\n".join("- [%s] %s" % (c["id"], c["title"]) for c in ucards)
            body = "单元阶段测试：综合以下关卡出题，题目以跨关卡综合与迁移为主。\n\n%s\n" % lst
            print("+ issue %s BOSS" % bid)
            if not a.dry_run:
                url = gh("issue", "create", "--title", "[%s] BOSS · %s" % (bid, unit),
                         "--body", body, "--label", L_BOSS, "--milestone", unit).strip()
                mp[bid] = int(url.rsplit("/", 1)[1])
                save_map(mp)
    print("✓ 完成" + ("（dry-run，未改动 GitHub）" if a.dry_run else ""))


def fetch_states():
    """{issue_number: (state, labels)}"""
    data = gh_json("issue", "list", "--state", "all", "--limit", "1000", "--json", "number,state,labels")
    return {d["number"]: (d["state"], {l["name"] for l in d["labels"]}) for d in data}


def status_of(state, labels):
    if state == "CLOSED":
        return "done"
    if L_DOING in labels:
        return "doing"
    if L_REVIEW in labels:
        return "review"
    return "todo"


def cmd_status(a):
    cards = load_cards()
    mp = load_map()
    states = fetch_states()

    def st(tid):
        n = mp.get(tid)
        if n is None or n not in states:
            return "todo", set()
        s, labels = states[n]
        return status_of(s, labels), labels

    total = done = 0
    recs = {"doing": [], "review": [], "start": [], "ready": [], "boss": []}
    for unit, key, ucards in units_of(cards):
        m = sum(1 for c in ucards if st(c["id"])[0] == "done")
        total += len(ucards)
        done += m
        bs, _ = st(key + "-boss")
        print("## %s  %d/%d%s" % (unit, m, len(ucards), "  🏆 boss 已过" if bs == "done" else ""))
        for c in ucards:
            s, labels = st(c["id"])
            tag = " 〔可跳过〕" if L_SKIP in labels else (" 〔从这开始〕" if L_START in labels else "")
            if a.all or s != "done":
                print("  %s %-8s %s%s" % (ICON[s], c["id"], c["title"], tag))
            if s in ("doing", "review"):
                recs[s].append(c)
            elif s == "todo":
                prereq_ok = all(st(p)[0] == "done" for p in c["prereqs"])
                if L_START in labels:
                    recs["start"].append(c)
                elif prereq_ok and L_SKIP not in labels:
                    recs["ready"].append(c)
        if m == len(ucards) and bs != "done":
            recs["boss"].append({"id": key + "-boss", "title": "BOSS · " + unit})
    print("\n总进度：%d/%d（%.0f%%）" % (done, total, 100.0 * done / total if total else 0))
    errata = sorted(tid for tid, n in mp.items() if L_ERRATUM in states.get(n, ("", set()))[1])
    if errata:
        print("待修卡片勘误：%s" % ", ".join(errata))
    order = recs["doing"] + recs["review"] + recs["boss"] + recs["start"] + recs["ready"]
    if order:
        print("\n建议下一步：")
        for c in order[:4]:
            print("  → %s %s" % (c["id"], c["title"]))


def cmd_show(a):
    n = issue_no(a.id)
    card = [c for c in load_cards() if c["id"] == a.id]
    if card:
        print("卡片：%s" % card[0]["path"])
    d = gh_json("issue", "view", n, "--json", "url,state,labels,comments")
    labels = {l["name"] for l in d["labels"]}
    print("issue：%s\n状态：%s  label：%s\n" % (
        d["url"], ICON[status_of(d["state"], labels)], ", ".join(sorted(labels)) or "无"))
    if not d["comments"]:
        print("（还没有学习记录）")
    for c in d["comments"]:
        print("—— %s ——\n%s\n" % (c["createdAt"][:10], c["body"]))


def cmd_set(a):
    n = issue_no(a.id)
    if a.to == "start":
        gh("issue", "reopen", n, check=False)
        gh("issue", "edit", n, "--add-label", L_DOING, "--remove-label", L_REVIEW)
    elif a.to == "review":
        gh("issue", "reopen", n, check=False)
        gh("issue", "edit", n, "--add-label", L_REVIEW, "--remove-label", L_DOING)
    elif a.to == "todo":
        gh("issue", "reopen", n, check=False)
        gh("issue", "edit", n, "--remove-label", L_DOING + "," + L_REVIEW)
    elif a.to == "done":
        gh("issue", "edit", n, "--remove-label", L_DOING + "," + L_REVIEW)
        gh("issue", "close", n, "--reason", "completed", check=False)
    print("✓ %s → %s %s" % (a.id, ICON[{"start": "doing"}.get(a.to, a.to)], a.to))


def cmd_label(a):
    n = issue_no(a.id)
    if a.kind == "skip":
        gh("issue", "edit", n, "--add-label", L_SKIP, "--remove-label", L_START)
    elif a.kind == "startpoint":
        gh("issue", "edit", n, "--add-label", L_START, "--remove-label", L_SKIP)
    else:
        gh("issue", "edit", n, "--remove-label", L_SKIP + "," + L_START)
    print("✓ %s 摸底标注 → %s" % (a.id, a.kind))


def cmd_clear_labels(a):
    unit = a.unit.zfill(2)
    mp = load_map()
    ids = [c["id"] for c in load_cards() if c["id"].split("-")[0] == unit]
    if not ids:
        sys.exit("没有单元 %s 的关卡" % unit)
    states = fetch_states()
    n_cleared = 0
    for tid in ids:
        n = mp.get(tid)
        if n is None:
            continue
        labels = states.get(n, ("", set()))[1]
        if labels & {L_SKIP, L_START}:
            gh("issue", "edit", str(n), "--remove-label", L_SKIP + "," + L_START)
            n_cleared += 1
    print("✓ 单元 %s：清掉 %d 关的摸底标注" % (unit, n_cleared))


_PROTECT = re.compile(r"\$`[^`\n]*`\$|(`+).+?\1")
_INLINE = re.compile(r"(?<![\\$])\$(?!\$)([^$`\n]+?)(?<![\\$])\$(?!\$)")


def _inline_math(seg):
    return _INLINE.sub(lambda m: "$`%s`$" % m.group(1), seg)


def gh_math(text):
    """让公式在 GitHub 上一定渲染：
    - 行内 $x$ → $`x`$：GitHub 要求开头的 $ 前面是空白或 ASCII，紧挨中文字、全角标点（：，；（）就不认；
      $`x`$ 写法不受影响。
    - 独占一行的 $$ 块前后补空行：块前没空行时 GitHub 当普通段落。
    代码块、行内代码、已是 $`x`$ 的不动。"""
    out, fence, display = [], False, False

    def blank_before():
        if out and out[-1].strip():
            out.append("")

    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```") and not display:
            fence = not fence
            out.append(line)
            continue
        if fence:
            out.append(line)
            continue
        if display:
            out.append(line)
            if s == "$$":
                display = False
                out.append("")
            continue
        if s == "$$" or (s.startswith("$$") and not s.endswith("$$")):
            blank_before()
            out.append(line)
            display = True
            continue
        if len(s) > 4 and s.startswith("$$") and s.endswith("$$"):
            blank_before()
            out.extend([line, ""])
            continue
        pos, buf = 0, []
        for m in _PROTECT.finditer(line):
            buf.append(_inline_math(line[pos:m.start()]))
            buf.append(m.group(0))
            pos = m.end()
        buf.append(_inline_math(line[pos:]))
        out.append("".join(buf))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def read_body(a):
    """--file 优先，否则读标准输入；公式规整成 GitHub 能渲染的写法（见 gh_math）"""
    if a.file:
        with open(a.file, encoding="utf-8-sig") as f:
            return gh_math(f.read().strip())
    return gh_math(sys.stdin.read().strip())


def cmd_comment(a):
    body = read_body(a)
    if not body:
        sys.exit("评论内容为空（从标准输入传入）")
    print(gh("issue", "comment", issue_no(a.id), "--body-file", "-", input=body).strip())


def cmd_erratum(a):
    n = issue_no(a.id)
    if a.fixed:
        gh("issue", "edit", n, "--remove-label", L_ERRATUM)
        print("✓ %s 的卡片勘误已清除" % a.id)
        return
    body = read_body(a)
    if not body:
        sys.exit("勘误内容为空（从标准输入传入：哪里错、应改成什么）")
    gh("label", "create", L_ERRATUM, "--color", LABELS[L_ERRATUM][0],
       "--description", LABELS[L_ERRATUM][1], check=False)
    gh("issue", "edit", n, "--add-label", L_ERRATUM)
    body = "📝 **卡片勘误**\n\n" + body
    print(gh("issue", "comment", n, "--body-file", "-", input=body).strip())


# ---------- 笔记 ----------

def ensure_label(name):
    gh("label", "create", name, "--color", LABELS[name][0], "--description", LABELS[name][1], check=False)


def repo_name():
    return gh_json("repo", "view", "--json", "nameWithOwner")["nameWithOwner"]


def ensure_image_repo(repo):
    """图片放在公开仓库 <repo>-note-images：私有仓库的图片链接要登录，GitHub 手机 App 显示不出来。第一次用时创建"""
    img = repo + IMAGE_REPO_SUFFIX
    code, _, _ = run([find_gh(), "api", "repos/" + img])
    if code != 0:
        gh("repo", "create", img, "--public", "--description", "%s 笔记里的图片，由 scripts/tracker.py note 上传" % repo)
        print("+ 新建公开图片仓库 https://github.com/%s（只放笔记图片）" % img)
    return img


def shrink(path):
    """Mac 上用 sips 把长边压到 1600px，省空间；别处原样上传"""
    import shutil
    import tempfile
    if not shutil.which("sips") or not path.lower().endswith((".png", ".jpg", ".jpeg")):
        return path
    out = os.path.join(tempfile.mkdtemp(), os.path.basename(path))
    code, _, _ = run(["sips", "-Z", "1600", path, "--out", out])
    return out if code == 0 and os.path.getsize(out) < os.path.getsize(path) else path


def upload_image(img_repo, tid, path, stamp, i):
    import base64
    ext = os.path.splitext(path)[1].lower() or ".png"
    dest = "%s/%s-%d%s" % (tid, stamp, i, ext)
    with open(shrink(path), "rb") as f:
        payload = json.dumps({"message": "笔记图片 " + dest, "content": base64.b64encode(f.read()).decode()})
    gh("api", "-X", "PUT", "repos/%s/contents/%s" % (img_repo, dest), "--input", "-", input=payload)
    branch = gh_json("api", "repos/" + img_repo)["default_branch"]
    return "https://raw.githubusercontent.com/%s/%s/%s" % (img_repo, branch, dest)


def note_issue(tid, intro):
    """找到或创建该关的笔记 issue，返回编号"""
    data = gh_json("issue", "list", "--label", L_NOTE, "--state", "all", "--limit", "500", "--json", "number,title")
    for d in data or []:
        if d["title"].startswith("[%s]" % tid):
            return str(d["number"])
    n = issue_no(tid)
    cards = load_cards()
    if tid.endswith("-boss"):
        key = tid.split("-")[0]
        unit = next((c["unit"] for c in cards if c["id"].split("-")[0] == key), None)
        title, head = "BOSS · %s" % (unit or key), "单元阶段测试的错题与收获。"
    else:
        c = next((c for c in cards if c["id"] == tid), None)
        if not c:
            sys.exit("找不到关卡 %s 的卡片" % tid)
        unit, title, head = c["unit"], c["title"], "**核心问题**：%s" % c["question"]
    body = gh_math("%s\n\n%s📌 关卡与学习进度：#%s\n" % (head, (intro.strip() + "\n\n") if intro else "", n))
    ensure_label(L_NOTE)
    args = ["issue", "create", "--title", "[%s] %s · 笔记" % (tid, title), "--body", body, "--label", L_NOTE]
    if unit:
        args += ["--milestone", unit]
    url = gh(*args).strip()
    print("+ 新建笔记 issue %s" % url)
    return url.rsplit("/", 1)[1]


def cmd_note(a):
    import datetime
    body = read_body(a) if (a.file or not sys.stdin.isatty()) else ""
    if not body and not a.image:
        sys.exit("笔记为空：没有正文也没有图片就不写")
    for p in a.image:
        if not os.path.isfile(p):
            sys.exit("图片不存在：%s" % p)
    n = note_issue(a.id, a.intro)
    if a.image:
        img_repo = ensure_image_repo(repo_name())
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        for i, p in enumerate(a.image, 1):
            md = "![](%s)" % upload_image(img_repo, a.id, p, stamp, i)
            ph = "{{img%d}}" % i
            body = body.replace(ph, md) if ph in body else (body + "\n\n" + md).strip()
    print(gh("issue", "comment", n, "--body-file", "-", input=body).strip())


def main():
    utf8_stdio()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("setup").set_defaults(f=cmd_setup)
    p = sub.add_parser("publish"); p.add_argument("--dry-run", action="store_true"); p.set_defaults(f=cmd_publish)
    p = sub.add_parser("status"); p.add_argument("--all", action="store_true"); p.set_defaults(f=cmd_status)
    p = sub.add_parser("show"); p.add_argument("id"); p.set_defaults(f=cmd_show)
    p = sub.add_parser("set"); p.add_argument("id"); p.add_argument("to", choices=["start", "review", "done", "todo"])
    p.set_defaults(f=cmd_set)
    p = sub.add_parser("label"); p.add_argument("id"); p.add_argument("kind", choices=["skip", "startpoint", "clear"])
    p.set_defaults(f=cmd_label)
    p = sub.add_parser("clear-labels"); p.add_argument("unit"); p.set_defaults(f=cmd_clear_labels)
    p = sub.add_parser("comment"); p.add_argument("id"); p.add_argument("--file"); p.set_defaults(f=cmd_comment)
    p = sub.add_parser("erratum"); p.add_argument("id"); p.add_argument("--fixed", action="store_true"); p.add_argument("--file")
    p.set_defaults(f=cmd_erratum)
    p = sub.add_parser("note"); p.add_argument("id"); p.add_argument("--file")
    p.add_argument("--image", action="append", default=[]); p.add_argument("--intro", default="")
    p.set_defaults(f=cmd_note)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
