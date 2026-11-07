---
name: learn-setup
description: 配环境：让这台设备能接着学——按 doctor 的检查结果逐项补齐 gh、登录、设备名、可选的原始素材。不碰进度，重复做无害。新设备第一次用、doctor 报 ✗、或学习者说“配环境”“这台电脑能学了吗”时使用。
---

# 配环境

目标：`doctor` 全部没有 ✗。**只补缺的东西**：不写 issue、不改进度、不改仓库文件，所以做多少次都不会丢东西。

## 0. 先认清命令

| 系统 | Python 命令 | 说明 |
|---|---|---|
| macOS / Linux | `python3` | |
| Windows（PowerShell） | `py` | `python3` 往往是应用商店的占位程序；`py` 不行再试 `python` |

下文写 `python3` 的地方，在 Windows 上一律换成 `py`。PowerShell 里中文乱码时先运行 `chcp 65001`。

## 1. 跑检查

```bash
python3 scripts/doctor.py
```

照着输出里每个 ✗ 的 `→` 修复提示做，修一项、再跑一次。常见几项：

### gh 没装

| 系统 | 装法 |
|---|---|
| Windows | `winget install GitHub.cli`，装完**重开终端**让 PATH 生效 |
| macOS | `brew install gh`；没有 Homebrew 就 `bash scripts/setup.sh`（装到 `~/.local/bin`） |
| Linux 有 sudo | `sudo apt install gh`（或官方 install_linux 文档） |
| Linux 无 sudo / 云电脑 | 从 https://github.com/cli/cli/releases/latest 下 `gh_*_linux_amd64.tar.gz`，把 `bin/gh` 放进 `~/.local/bin`（家目录里的文件更换实例后也会保留） |

### gh 没登录

优先**学习者本人**在这台设备上交互登录，登录状态会保存在 `~/.config/gh`：

```bash
gh auth login        # GitHub.com → HTTPS → 浏览器或 device code
```

这一步要学习者自己操作（打开链接、输验证码），导师不要替他输密码或 token。

后备：没法交互登录的环境（云端 agent），由学习者自己把 fine-grained PAT 放进环境变量 `GH_TOKEN`，权限只给本仓库：**Issues 读写、Contents 只读**（下载素材需要 Contents）。不要把 token 写进仓库文件或聊天记录。

### label 缺

```bash
python3 scripts/tracker.py setup
```

## 2. 设备名

doctor 提示“设备名没设置”时，问学习者给这台设备起什么名字（短、英文，如 `mac`、`win-codex`、`grok-cloud`），写进仓库根目录的 `.learn-device`（不提交 git）：

```bash
echo win-codex > .learn-device
```

开始闯关时，进度评论里会写上这个名字，别的设备看进度就知道这关在哪台设备上开始。

## 3. 原始素材（可选）

学习只需要仓库里的提取文字和视频链接。要看教材原图（卡片里写着“OCR 丢了插图，回原 PDF”的地方）才需要原件，大小见 `python3 scripts/sources.py status`。问学习者要不要现在下：

```bash
python3 scripts/sources.py pull
```

## 4. 收尾

再跑一次 `doctor`，没有 ✗ 就告诉学习者“这台设备可以学了”，然后回到 `AGENTS.md` 的“每个新对话开头”。

⚠️ 不用全部消掉：“落后 origin”交给检查更新（`learn-update`），“没下素材”是正常的降级。

## 不要做

- 不要运行 `tracker.py set / label / publish`；配环境与进度无关
- 不要为了消除 ⚠️ 去提交或改仓库文件
- 备课档（`doctor --prep`、`setup.sh`）只在学习者要在这台 Mac 上备课时才装
