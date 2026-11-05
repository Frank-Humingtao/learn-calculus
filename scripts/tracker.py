#!/usr/bin/env python3
"""关卡进度：GitHub Issues 的薄封装（需要已登录的 gh）

  setup                       创建状态 label（一次）
  publish [--dry-run]         course/levels/*.md → 每单元一个 milestone + 每关一个 issue + 每单元一个 boss issue
  status [--all]              进度总览 + 推荐下一关
  show <id>                   卡片路径、issue 状态、历史评论
  set <id> start|review|done|todo
  label <id> skip|startpoint|clear     摸底标注（skip 为旧用法，新摸底不再使用）
  clear-labels <单元号>                清掉该单元所有关卡的摸底标注
  comment <id> < record.md    在 issue 下追加一条学习/测试记录

状态：未开始=open 无状态 label；进行中=label「进行中」；待复习=label「待复习」；已掌握=closed
关卡 id 与 issue 编号的对应保存在 course/issues.json。
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys

from common import COURSE, LEVELS, ROOT

ISSUES_JSON = os.path.join(COURSE, "issues.json")

L_DOING, L_REVIEW = "进行中", "待复习"
L_SKIP, L_START = "摸底:可跳过", "摸底:从这开始"
L_LEVEL, L_BOSS = "关卡", "boss"
LABELS = {
    L_LEVEL: ("ededed", "一个关卡"),
    L_BOSS: ("b60205", "单元阶段测试"),
    L_DOING: ("fbca04", "正在学"),
    L_REVIEW: ("d93f0b", "需要复习"),
    L_SKIP: ("0e8a16", "摸底显示可能已掌握"),
    L_START: ("1d76db", "摸底显示从这里开始"),
}
ICON = {"done": "✅", "doing": "🟡", "review": "🔁", "todo": "⬜"}


# ---------- gh ----------

def gh_path():
    exe = shutil.which("gh") or os.path.expanduser("~/.local/bin/gh")
    if not os.path.exists(exe):
        sys.exit("找不到 gh：先运行 bash scripts/setup.sh")
    return exe


def gh(*args, input=None, check=True):
    p = subprocess.run([gh_path()] + list(args), cwd=ROOT, input=input, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode != 0:
        sys.exit("gh %s 失败：%s" % (" ".join(args[:3]), p.stderr.strip()))
    return p.stdout


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


def cmd_comment(a):
    body = sys.stdin.read().strip()
    if not body:
        sys.exit("评论内容为空（从标准输入传入）")
    print(gh("issue", "comment", issue_no(a.id), "--body-file", "-", input=body).strip())


def main():
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
    p = sub.add_parser("comment"); p.add_argument("id"); p.set_defaults(f=cmd_comment)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
