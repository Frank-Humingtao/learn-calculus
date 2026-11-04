---
name: learn-progress
description: 查看与修改学习进度：总览、推荐下一关、按学习者的话标记已掌握/待复习/重来。学习者问“我学到哪了”“这关我懂了”“改回待复习”“这几关跳过”时使用。
---

# 进度

所有状态都在 GitHub Issues 上，学习者也可以直接在网页或手机上改；所以每次都重新查，不要凭印象。

| 学习者说 | 做 |
|---|---|
| 学到哪了 / 下一步 | `python3 scripts/tracker.py status`（`--all` 含已掌握），用两三句话总结：完成比例、进行中、待复习，再给推荐 |
| X 我懂了 | `tracker.py set <id> done`；说的是一整个单元就对该单元每关执行 |
| X 没懂 / 要复习 | `tracker.py set <id> review` |
| X 重来 | `tracker.py set <id> todo` |
| X 的记录 | `tracker.py show <id>` |
| 今天到这 | 一句话总结今天的进展；在当前关卡写一条评论说明下次从哪继续 |

关卡 id 不确定时，从 `course/SYLLABUS.md` 里按标题匹配，并跟学习者确认。
