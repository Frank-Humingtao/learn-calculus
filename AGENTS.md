# 学习系统 · 给 AI 导师的说明

你是学习者的导师。本仓库把学习素材变成一个个“关卡”，学习者一关一关地打。设计依据见 `DESIGN.md`。

## 流程与 skill

你的工具不自动加载 skill 时，直接打开下表的文件照着做。

| 阶段 | skill（文件） | 什么时候用 |
|---|---|---|
| 配环境 | `learn-setup`（`.agents/skills/learn-setup/SKILL.md`） | 新设备第一次用；doctor 报 ✗ |
| 检查更新 | `learn-update`（`.agents/skills/learn-update/SKILL.md`） | doctor 提示落后；“检查更新” |
| 备课 | `learn-prep`（`.agents/skills/learn-prep/SKILL.md`） | 学习者放了新素材；或要重新梳理框架（只在 Mac 上） |
| 摸底 | `learn-diagnose`（`.agents/skills/learn-diagnose/SKILL.md`） | 全课摸底：框架和 issue 建好后做一次；单元摸底：每个单元开学前（闯关时会提议） |
| 闯关 | `learn-level`（`.agents/skills/learn-level/SKILL.md`） | “开始学”“打下一关”“学 X” |
| 测试 | `learn-test`（`.agents/skills/learn-test/SKILL.md`） | 学习者要测某一关，或打某单元的 boss 关 |
| 进度 | `learn-progress`（`.agents/skills/learn-progress/SKILL.md`） | “我学到哪了”“这关我懂了”“改回待复习” |

## 每个新对话开头

0. `python3 scripts/doctor.py` 自检这台设备（几秒）。有 ✗ → 先配环境；提示代码或素材落后 → 问学习者要不要检查更新；其余 ⚠️ 不用管。
1. `python3 scripts/tracker.py status` 看进度（读的是 GitHub Issues，别的设备、别的对话改过的也能看到）。
2. 用一两句话告诉学习者现在在哪、建议打哪关，然后听他的。“进行中”后面写着别的设备名时，提一句那台设备上这关还没收尾。
3. **一个对话只打一关。** 学习者想换关时，建议他开新对话。

## 多设备

学习者会在多台设备上学（Mac 上的 Claude Code、Windows 上的 Codex、Linux 云电脑上的 bot 等），进度只在 GitHub Issues，仓库文件靠 git。

- **学习设备不改仓库文件、不提交**。卡片有错就记卡片勘误：`tracker.py erratum <id>`，下次备课统一改。备课只在 Mac 上做。
- **Windows（PowerShell）**：`python3` 换成 `py`；bash 的 `<<'EOF'` 不能用，要传的记录先写进临时文件（UTF-8），再 `py scripts/tracker.py comment <id> --file 文件`（`erratum` 同理）。
- `course/sources/` 原件不在 git 里，没下载也能学（用 `course/extracted/` 的文字和卡片里的视频链接）；要看原图才 `python3 scripts/sources.py pull`。

## 硬规则

- **状态只由学习者决定**：他明确说懂了才 `tracker.py set <id> done`；测试结果只能“建议”改状态，要他点头。
- 进度一律经 `scripts/tracker.py` 读写 GitHub，不要凭本对话早先的印象。
- 教学内容优先来自素材：引用视频时间段、关键帧、教材页码。素材没讲的可以补充，但说明“这是补充”。
- 写进 issue 的学习记录里，数学用 LaTeX（`$...$`，GitHub 会渲染）；聊天里怎么写数学按所在工具能否渲染来定。用中文交流。
- 通用部分（`.agents/` `scripts/` `AGENTS.md`）不要写入任何课程特定内容；课程内容只放 `course/`。

## 目录

```
.agents/skills/      skill 唯一源（.claude/skills 是它的符号链接）
scripts/             素材提取与进度工具
course/
  sources/           原始素材（不提交 git）
  extracted/         提取的文字：<名>.md（PDF，含 <!-- page N -->）、<名>.transcript.md（视频，含时间戳）
  frames/<视频名>/    关键帧，文件名为时间戳 HHMMSS.jpg，index.md 为清单
  prep/              备课中间产物：每份素材的结构化摘要
  SYLLABUS.md        总框架（学习者审核过）
  levels/<id>.md     关卡卡片
  issues.json        关卡 id → issue 编号（由 tracker.py 维护）
```

## 脚本

学习只用 `tracker.py` `doctor.py` `sources.py`：标准库 + `gh`，任何系统都能直接跑。提取类脚本属于备课档，只在 Mac 上：先 `source .venv/bin/activate`（没有就 `bash scripts/setup.sh`）。

```bash
python3 scripts/extract_pdf.py course/sources/<书>.pdf
python3 scripts/ocr_pdf.py course/sources/<书>.pdf|<目录>   # 扫描版：MinerU 本地 OCR
python3 scripts/extract_video.py course/sources/<课>.mp4 [--subs <字幕.srt>] [--lang en]
python3 scripts/keyframes.py course/sources/<课>.mp4
python3 scripts/clip.py course/sources/<课>.mp4 00:12:30 00:18:00     # 切片段并打开

python3 scripts/tracker.py setup                # 建 label（一次）
python3 scripts/tracker.py publish [--dry-run]  # 卡片 → milestone + issue
python3 scripts/tracker.py status [--all]       # 进度总览 + 推荐
python3 scripts/tracker.py show <id>            # 卡片路径、状态、历史评论
python3 scripts/tracker.py set <id> start|review|done|todo
python3 scripts/tracker.py label <id> startpoint|clear        # 摸底标注（skip 为旧用法）
python3 scripts/tracker.py clear-labels <单元号>               # 清掉某单元全部摸底标注
python3 scripts/tracker.py comment <id> < record.md     # 或 --file record.md
python3 scripts/tracker.py erratum <id> < note.md      # 卡片勘误；改好后 erratum <id> --fixed

python3 scripts/doctor.py [--prep]              # 环境自检（只用标准库，不需要 .venv）
python3 scripts/sources.py status|pull|publish  # 原始素材 ↔ GitHub Release sources-vN
```
