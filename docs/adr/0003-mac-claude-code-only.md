# 只在 Mac 上的 Claude Code 里用，撤回多设备

2026-11-07 曾让仓库能在 Windows 上的 Codex、Linux 云电脑上的 bot、Cursor 云 Agent 里接着学（`doctor.py` 自检、`learn-setup` 配环境、`learn-update` 检查更新、设备名、素材打包进 GitHub Release，见 `.scratch/multi-agent-continuity/`）。实际用了两天，学习者发现在别的工具上学体验不好——可视化讲解、KaTeX 卡片、笔记截图都只有 Claude 能做——于是 2026-11-09 决定只在自己这台 Mac 上的 Claude Code 里用，多设备那一层整体删掉，让系统更轻。

进度和笔记仍然放 GitHub Issues：它们本来就不只是为多设备服务（网页和手机上能看、能直接改状态）。

## 后果

- 删掉 `doctor.py`、`sources.py`、`learn-setup`、`learn-update`、`.learn-device`；`AGENTS.md` 并入 `CLAUDE.md`，skill 从 `.agents/skills/` 搬到 `.claude/skills/`。
- 原始素材只在主目录的 `course/sources/`，worktree 里没有，要用主目录的路径。Release `sources-v1` 留作冷备份，不再更新（取代 ADR 0001）。
- 仍有一个“仓库文件过期”的口子：PR 在 GitHub 上合并后本地 main 不会自己更新，从旧 main 切出的 worktree 用的是旧 skill（2026-11-08 有一关因此没写笔记）。所以对话开头静默比较 `HEAD` 和 `origin/main`，落后才提醒先 `git pull`。
- 卡片勘误保留：闯关常在 worktree 里，直接改卡片不合并就丢了。
- 以后若想再支持别的工具，别直接把这些加回来，先回头看这条为什么撤。
- 2026-11-16 曾实测手机上的 Claude Code 云端会话（同一个 Claude，不是别的工具）：读照片、skill 都能用，但没有可视化卡片、`tracker.py` 的 gh GraphQL 被禁，学习者决定放弃，维持本条。结论见 `.scratch/cloud-learning/`。
