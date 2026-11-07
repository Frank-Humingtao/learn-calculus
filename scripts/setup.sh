#!/bin/bash
# 备课档（只在 macOS / Apple Silicon 上需要；只学习的设备不用跑，见 .agents/skills/learn-setup）
# 安装本地工具（不需要 sudo / Homebrew）：
#   .venv：pymupdf（PDF）、mlx-whisper（转写）、imageio-ffmpeg（自带 ffmpeg）
#   ~/.local/bin/gh：GitHub CLI（没有时顺便装上）
# 扫描版 PDF 另需 MinerU（mineru-kit），见 scripts/ocr_pdf.py
# 装完用 python3 scripts/doctor.py --prep 检查
set -e
cd "$(dirname "$0")/.."

if [ ! -d .venv ]; then python3 -m venv .venv; fi
.venv/bin/pip install -q --upgrade pip
.venv/bin/pip install -q pymupdf mlx-whisper imageio-ffmpeg

if ! command -v gh >/dev/null && [ ! -x ~/.local/bin/gh ]; then
  arch=$(uname -m); [ "$arch" = "x86_64" ] && arch=amd64
  url=$(curl -s https://api.github.com/repos/cli/cli/releases/latest | grep -o "https://[^\"]*macOS_${arch}.zip" | head -1)
  tmp=$(mktemp -d)
  curl -sL "$url" -o "$tmp/gh.zip" && unzip -q "$tmp/gh.zip" -d "$tmp"
  mkdir -p ~/.local/bin && cp "$tmp"/*/bin/gh ~/.local/bin/gh
  echo "gh 已装到 ~/.local/bin/gh（建议把 ~/.local/bin 加入 PATH）"
fi

echo "✓ 完成。之后：source .venv/bin/activate"
