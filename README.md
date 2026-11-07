# learn-calculus

> **给 AI agent**：你是这里的导师。先读 [AGENTS.md](AGENTS.md) 并照做；第一步是 `python3 scripts/doctor.py`（Windows 用 `py`）。

一个由 AI 导师驱动的个人学习系统：放进素材 → AI 备课拆成关卡 → 摸底 → 一关一关地打，进度记在本仓库的 GitHub Issues。
在 Claude Code 和 Codex 里都能用。设计见 [DESIGN.md](DESIGN.md)。

## 换一台设备接着学

进度在 GitHub Issues 上，卡片和提取文字在 git 里，所以 clone 下来就能学。只需要 `python3`（≥ 3.8）、`git`、登录好的 `gh`：

```bash
git clone https://github.com/Frank-Humingtao/learn-calculus.git
cd learn-calculus
python3 scripts/doctor.py        # 缺什么、怎么补，逐项告诉你
```

然后在这个目录里对导师说“配环境”，它会照 [learn-setup](.agents/skills/learn-setup/SKILL.md) 带你装 gh、登录、给设备起名、（可选）下载原始素材。之后每次开新对话它都会先自检；本地落后时会建议“检查更新”。

原始素材（教材 PDF 等）不进 git，打包在本仓库的 Release `sources-vN` 里：`python3 scripts/sources.py pull`。不下载也能学，只是看不了原图。

### 在不同 agent 上使用

| agent | 怎么接入 |
|---|---|
| **Claude Code**（macOS） | 在仓库目录打开即可：自动读 `CLAUDE.md` → `AGENTS.md`，skill 经 `.claude/skills` 加载。备课也在这里做（需要 `bash scripts/setup.sh`） |
| **Codex**（Windows，PowerShell） | 在仓库目录打开即可：自动读 `AGENTS.md`、`.agents/skills`。命令用 `py` 代替 `python3`；gh 用 `winget install GitHub.cli`。中文乱码先 `chcp 65001` |
| **Cursor 云 Agent** | 检出仓库后自动读 `AGENTS.md` 和 `.agents/skills`；没有交互登录时，由你在它的 secret 里放 `GH_TOKEN`（见下） |
| **Grok bot（云电脑，Linux）** | 不会自动读仓库文件。把下面这段放进 bot 的用户技能/工作流，第一次在云电脑上 `gh auth login`（登录状态会保留） |

Grok bot 用户技能（复制粘贴）：

```text
当我要学微积分（或说“开始学”“打下一关”“我学到哪了”）时：
1. 仓库在 ~/learn-calculus；没有就 git clone https://github.com/Frank-Humingtao/learn-calculus.git ~/learn-calculus
2. cd ~/learn-calculus && git pull --ff-only
3. 读 ~/learn-calculus/AGENTS.md，按它的“每个新对话开头”和 skill 文件（.agents/skills/<名>/SKILL.md）当我的导师
所有教学规则以仓库里的文件为准，这里不另写规则。
```

**令牌**（只给没法交互登录的环境）：GitHub → Settings → Developer settings → Fine-grained tokens，只选本仓库，权限 **Issues: Read and write**、**Contents: Read-only**，放进环境变量 `GH_TOKEN`。不要写进仓库或聊天。

### 学习设备的约定

- 不改仓库文件、不提交；卡片有错由导师记“卡片勘误”（issue 上的 label），回到 Mac 备课时统一改
- 两台设备别同时打同一关；“进行中”会显示是在哪台设备上开始的

## 在 Mac 上备课

```bash
bash scripts/setup.sh          # 备课档：pymupdf、mlx-whisper、ffmpeg、gh（不需要 sudo）
python3 scripts/doctor.py --prep
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
