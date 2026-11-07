---
name: learn-update
description: 检查更新：把一台已经能学的设备带到最新——拉取卡片、skill、脚本的改动，比对原始素材版本，再自检一遍。doctor 提示落后、或学习者说“检查更新”“同步一下”时使用。
---

# 检查更新

进度本来就在 GitHub 上、实时同步，这里只管**仓库文件**和**原始素材**。Windows 上把 `python3` 换成 `py`。

## 1. 代码

```bash
git status --short
git pull --ff-only
```

- 有本地改动：先给学习者看是什么。学习设备按约定不改仓库文件；卡片的问题应该记成卡片勘误（`tracker.py erratum`），所以多半可以 `git restore` 丢掉——**丢之前问他**
- `--ff-only` 失败（本地有提交）：停下，把 `git log origin/main..HEAD` 给学习者看，由他决定

拉到了新内容就用一两句话说说变了什么（`git log --oneline <旧>..HEAD`）：新关卡、改过的卡片、skill 调整。

## 2. 原始素材

```bash
python3 scripts/sources.py status
```

本地没有或落后时，**问学习者**要不要下载（大小见上面的输出），要才 `python3 scripts/sources.py pull`。

## 3. 自检

```bash
python3 scripts/doctor.py
```

出现 ✗（比如新脚本要求新的 label）就转去配环境（`learn-setup`）。
