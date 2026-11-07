# 多设备、多 agent 接着学

Status: ready-for-agent

## 目标

学习者能在 Mac（Claude Code）、Windows（Codex，PowerShell）、Grok bot 的 Linux 云电脑、Cursor 云 Agent 上接着学同一门课：
`git clone` 即得到学习所需的一切，进度只在 GitHub Issues，新设备几分钟内配好环境并能自检。

## 决定（2026-11-07 grilling）

1. **素材**：原件不进 git，也不用 LFS；打包发到私有仓库 Release `sources-vN`，需要看原图的设备再下载。本机原件先从 worktree 移回主目录。见 ADR 0001。
2. **依赖两档**：学习档 = python3（≥3.8，标准库）+ git + gh（已登录），覆盖 macOS / Linux / 原生 Windows；备课档 = pymupdf、mlx-whisper、ffmpeg、MinerU，只在 Mac。`setup.sh` 只装备课档。
3. **`scripts/doctor.py`**：标准库实现，逐项 ✓/✗/⚠️ 并给修复命令；`--prep` 加查备课档。缺素材、素材过期、本地落后 origin 是 ⚠️。
4. **配环境**（`learn-setup`）：按 doctor 的 ✗ 逐项修（各平台装 gh、登录、Windows 用 `py`、选下素材、起设备名）；不碰进度，重复无害。登录优先 `gh auth login`，`GH_TOKEN`（fine-grained PAT）作后备。
5. **检查更新**（`learn-update`）：`git pull` → 比对素材 Release → 跑 doctor。`learn-prep` 末尾发布新 `sources-vN`。
6. **AGENTS.md**：对话开头第 0 步跑 doctor；流程表写 skill 文件路径；学习设备不改仓库文件，卡片有错记卡片勘误。聊天显示偏好不写进仓库。
7. **tracker.py**：`set start` 评论带设备名（`.learn-device`，不提交；缺省 hostname）；`status` 的进行中带设备名；`erratum <id>` 打 `卡片勘误` label 并评论；输出强制 UTF-8。不加锁。
8. **README**：首句写给 AI；“在不同 agent 上使用”一节，含 Grok bot 可粘贴的技能文字。

## 不做

- 不为纯聊天 bot 写额外接口
- 不做多设备锁
- 学习设备上不做 git 提交
