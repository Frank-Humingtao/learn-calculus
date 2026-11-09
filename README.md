# learn-calculus

> **给 AI agent**：你是这里的导师。读 [CLAUDE.md](CLAUDE.md) 并照做。

一个由 AI 导师驱动的个人学习系统：放进素材 → AI 备课拆成关卡 → 摸底 → 一关一关地打，进度记在本仓库的 GitHub Issues。
只在 Mac 上的 Claude Code 里用。设计见 [DESIGN.md](DESIGN.md)。

## 准备

需要 `python3`、`git`、登录好的 `gh`（`brew install gh && gh auth login`）。备课另需：

```bash
bash scripts/setup.sh          # 备课档：pymupdf、mlx-whisper、ffmpeg、gh（不需要 sudo）
```

原始素材（教材 PDF、视频）放在主目录的 `course/sources/`，不进 git。

## 日常

在仓库目录打开 Claude Code，直接说：

| 你说 | 发生什么 |
|---|---|
| “我在 course/sources 放了新素材，备课吧” | 提取文字和关键帧 → 逐份摘要 → 生成 `course/SYLLABUS.md` 给你审核 → 确认后生成关卡卡片和 issue |
| “给我摸个底” | 按单元出诊断题，在 issue 上标注从哪开始 |
| “开始学” / “打 02-03” | 闯一关：对话、看原视频片段或读教材原文 |
| “这关我懂了” | 关闭该关的 issue |
| “测测我 02-03” / “打第二单元 boss” | 测试，记录题目与错因，给建议 |
| “我学到哪了” | 进度总览与推荐 |

**每关开一个新对话。** 进度在 GitHub 上，不依赖对话记忆；你也可以直接在 GitHub 网页或手机 App 上关闭/重开 issue、改 label。

## 用作模板学新课程

本仓库是 GitHub template repo：点 “Use this template” 生成新仓库，删除 `course/` 下的课程内容（保留目录结构），放入新素材，开始备课。
