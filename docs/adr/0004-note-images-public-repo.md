# 笔记图片改存公开仓库 <仓库名>-note-images

取代 [0002](0002-notes-separate-issue-images-on-branch.md) 里“图片存孤立分支 `note-images`”这一部分；笔记单独开 issue 的决定不变。

2026-11-14 学习者发现：笔记图片在电脑网页能看，在 GitHub 手机 App 里看不到。原因是仓库私有，`blob/note-images/...?raw=true` 要登录才能打开（未登录访问返回 404）；网页带着登录 cookie，手机 App 渲染 Markdown 图片时不带。

现在 `tracker.py note` 把图片经 `gh api` 写进同一账号下的**公开**仓库 `<本仓库名>-note-images`（第一次用时自动创建），路径仍是 `<关卡id>/<时间>-<序号>.<扩展名>`，笔记里用 `https://raw.githubusercontent.com/<图片仓库>/<默认分支>/...` 引用，不登录也能显示。

## 考虑过的方案

- **整个仓库改公开**：仓库里有教材逐章提取文字（`course/extracted/`），Release 里有原始素材包，公开等于对外分发受版权保护的教材。否决。
- **网页拖拽上传的 user-attachments**：手机能显示，但没有命令行/API 接口。

## 后果

- 图片是公开的：只放手写照片和可视化截图，不要上传教材页截图等素材原件。
- 旧的 `note-images` 分支图片已迁到公开仓库、已发笔记里的链接已改写；该分支保留未删，确认无用后可手动删。
- 清理笔记时图片要去公开仓库单独删。
