---
Status: superseded by ADR-0003
---

# 原始素材用 GitHub Release 分发，不进 git

原始素材（教材 PDF、视频、讲义包）几百 MB，要在多台设备之间迁移，但学习时多数设备用不到它们：卡片的学习路径靠 `course/extracted/` 的文字和在线视频链接就够，只有看 OCR 丢掉的插图才需要原件。所以 `course/sources/` 继续不进 git，改为打成一个 zip，作为私有仓库的 Release 资产 `sources-vN` 发布（`scripts/sources.py`）；需要原图的设备再 `pull`，本地版本记在 `course/sources/.version`。

## 考虑过的方案

- **直接提交到 git**：每次 clone 都要拉几百 MB，历史里永远带着，以后换素材只会更大。
- **Git LFS**：免费额度每月 1GB 流量，每 clone 一次就用掉三分之一；还要求每台设备装 git-lfs。
- **只提交需要看图的页面截图**：体积小，但要在备课时额外挑页截图，且学习时想翻原书别处就没有。

## 后果

- clone 快，没下载素材的设备是“降级可用”，doctor 只给 ⚠️。
- 素材有变动时必须重新发布：`learn-prep` 末尾 `sources.py publish`，doctor / `learn-update` 比对版本号提示下载。
- 2026-11-07 之前素材只存在于做备课的 worktree 里，差点随 worktree 清理丢失；现在主目录与 Release 各有一份。


> 2026-11-09：被 [ADR 0003](0003-mac-claude-code-only.md) 取代。只在一台 Mac 上用后不再需要分发素材，`sources.py` 已删除；Release `sources-v1` 留作冷备份，不再更新。
