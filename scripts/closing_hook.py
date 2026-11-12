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
1. 这关做过的每一道题（不论对错）：完整题面，做错的再写错在哪和正确过程。
2. 手写照片：学习者这次上传的每一张都收进去，不论对错，放在对应题下面。回头数一遍聊天里的图。
3. 他自己的推导、讲解中的补充、易混点：写成“这关要记住的”小结。
4. 关键可视化：讲清概念或纠错的都收（截图或用 LaTeX 重写）。
5. 感悟：只在学习者说“记下来”时写。
笔记宁详细勿遗漏。
另外：发现卡片有错就 tracker.py erratum；最后用一句话给下一步建议，提醒下一关开新对话。"""

NOTE = """【笔记检查】发出前逐项过一遍（详见 note.md“发出前自查”）：
1. 学习者这次上传的每一张手写，是否都在 --image 里（做对的也要收）？
2. 这关出过的每一道题，是否都有一节、都带完整题面（题干、条件、每个小问；读图题附题图）？
3. 他自己的推导、讲解补充、易混点，是否都写进了“这关要记住的”？"""


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
