#!/usr/bin/env python3
"""PreToolUse hook：导师要写学习记录或笔记前，把收尾清单塞进上下文。

收尾一定会经过 `tracker.py comment`（写学习记录）和 `tracker.py note`（写笔记），
所以在这两个动作之前提醒，不依赖学习者说了什么。只提醒、不拦截。
"""
import json
import re
import sys

COMMENT = """【收尾清单】你正要写学习记录。先确认这一次是什么：
- 闯关 / 单关测试 / boss 测试：记录写完后还必须写笔记（tracker.py note）。
- 摸底：不写笔记。
写笔记前对照 .claude/skills/learn-level/note.md，逐项过一遍：
1. 错题：做错过的题（含纠正后掌握），带完整题面。
2. 手写照片：学习者这次上传的手写演算全部收进去，不论对错。回头数一遍聊天里的图。
3. 关键可视化：只收讲清概念或纠错的。
4. 感悟：只在学习者说“记下来”时写。
另外：发现卡片有错就 tracker.py erratum；最后用一句话给下一步建议，提醒下一关开新对话。"""

NOTE = """【笔记检查】发出前再数一遍：学习者这次上传的每一张手写演算，是否都在 --image 里（做对的也要收）？
错题是否都带了完整题面（题干、条件、每个小问；读图题附题图）？"""


def main():
    try:
        cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    except Exception:
        return
    if re.search(r"tracker\.py\s+comment\b", cmd):
        text = COMMENT
    elif re.search(r"tracker\.py\s+note\b", cmd):
        text = NOTE
    else:
        return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "additionalContext": text,
    }}, ensure_ascii=False))


main()
