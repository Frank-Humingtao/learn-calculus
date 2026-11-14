# 笔记单独开 issue，图片经 API 存到孤立分支 note-images

> 图片存放部分已被 [0004](0004-note-images-public-repo.md) 取代：改存公开仓库 `<仓库名>-note-images`。

学习者经常回看关卡 issue，但学习记录是写给导师的压缩格式，人看着累；而他又想把手写解题照片、导师做的可视化留下来。于是给学习者的东西单独成为「笔记」：每关一个笔记 issue（label `笔记`、同 milestone、一直 open），关卡 issue 和状态照旧只给导师用，导师平时不读笔记，上下文不变大。

图片是难点：仓库是私有的，GitHub 网页拖拽上传的附件没有命令行接口。所以 `tracker.py note` 用 `gh api` 把图片直接写进孤立分支 `note-images`（`<关卡id>/<时间>-<序号>.png`），笔记里用 `https://github.com/<repo>/blob/note-images/...?raw=true` 引用。2026-11-08 学习者实测：这种链接和 `/raw/` 链接都能显示，`raw.githubusercontent.com` 不行（私有仓库要 token）。

## 考虑过的方案

- **同一个 issue 里分人看 / AI 看两段**（`<details>` 折叠或 HTML 注释）：学习者只想看给人的那部分，混在一起翻起来还是乱。
- **Release 附件存图**（像原始素材那样）：私有仓库的 Release 下载链接在 issue 里显示不出来。
- **图片提交到 main**：仓库越来越大，而且闯关时不改仓库文件。

## 后果

- 每次闯关结束写两份：学习记录（导师）+ 笔记（学习者），错因在学习记录里仍要用文字记一句。
- 笔记 issue 不进 `issues.json`（闯关时不提交文件），按标题前缀 `[<id>]` + label 查找。
- `note-images` 分支只放图，永远不合并进 main；清理笔记时图片要单独删。
- 可视化转图片靠本机 Chrome（`scripts/snap.py`）。
