# learn-calculus

一个由 AI 导师驱动的个人学习系统：放进素材 → AI 备课拆成关卡 → 摸底 → 一关一关地打，进度记在本仓库的 GitHub Issues。
在 Claude Code 和 Codex 里都能用。设计见 [DESIGN.md](DESIGN.md)。

## 第一次使用

```bash
bash scripts/setup.sh          # 本地工具：pymupdf、mlx-whisper、ffmpeg、gh（不需要 sudo）
~/.local/bin/gh auth login     # 登录 GitHub（只需一次）
```

## 日常

在仓库目录打开 Claude Code 或 Codex，直接说：

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
