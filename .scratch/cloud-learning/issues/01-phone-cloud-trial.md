# 01: 手机云端会话实测一次最小闯关

**What to build:** 学习者在手机上的 Claude Code 开一个云端会话（从 GitHub 上的本仓库 main 启动），走一遍最小闯关链路，记下每一步能不能用、体验如何，据此决定云端学习这条路继续还是放弃。

背景：ADR 0003 记录了 2026-11-07 的多设备尝试，因为可视化讲解、KaTeX 卡片、笔记截图在别的工具上用不了而撤回。这次仍是 Claude Code，但云端会话里这些能力是否还在是未知数，所以先实测再动代码。

要走的链路：
1. 开场：读 CLAUDE.md、跑 `tracker.py status` 看进度。
2. 出一道带公式的题：公式能不能以可视化卡片显示？不能的话，聊天里直接看到的是什么样？
3. 用手机拍一张手写上传，导师能不能读到图片内容。
4. 写一条学习记录评论、发一条带这张照片的笔记。
5. 整体体验和本机比如何。

**Blocked by:** None (can start immediately)

**Status:** resolved（结论：放弃）

- [x] 上面 5 步每一步都记下结果（能用 / 不能用 / 报错原文 / 截图），追加在本文件 `## Comments` 下
- [x] 学习者给出结论：继续 或 放弃
- [x] 若结论是“放弃”：不改任何代码和规则，维持现状（只在 Mac 本机用，ADR 0003 不变）；在 ADR 0003 末尾补一句“2026-11 曾实测云端会话，结论见 `.scratch/cloud-learning/`”；02–04 标 `wontfix`
- [ ] 若结论是“继续”：把实测发现的具体问题（缺什么命令、缺什么权限、公式怎么显示）写清楚，作为 02、03 的输入

## Comments

### 2026-11-16 实测记录（手机 Claude App → 云端会话，测试关 04-05 / issue #45，未改任何关卡状态）

1. **开场 `tracker.py status`：不能用。** 仓库同步检查正常（git fetch 可用，main 不落后）。tracker 报错原文：
   `gh issue list --state 失败：HTTP 403: GitHub GraphQL is not available from Claude Code sessions; use the REST API (gh api repos/{owner}/{repo}/...)`；`gh auth status` 另报 `The token in GH_TOKEN is invalid`。
2. **公式卡片：原方案不能用，替代方案能用。** 会话里没有 show_widget / visualize。改为写一个 KaTeX 网页（cdnjs）用文件预览发给学习者，手机上排版正常（试验页面留在分支 `claude/confident-knuth-oev5eb` 的 `.scratch/cloud-learning/trial/`，未合入 main）。聊天正文里的 `$...$` 显示为原始 LaTeX 代码，不渲染。
3. **读手写照片：能用。** 上传的照片完整读出：$\ln x/x^{1/3}$ 核对 ∞/∞ 型 → 洛必达 → $3/x^{1/3}\to0$；推广到任意 $p>0$。还能看出笔误（结论写成“ln x 快”，应是 $x^p$ 快）。
4. **评论与笔记：`tracker.py` 不能用，绕行能用。**
   - `tracker.py comment 04-05`：`gh issue comment 45 失败：HTTP 403: GitHub GraphQL is not available from Claude Code sessions ...`
   - `tracker.py note 04-05 --image ...`：`gh issue list --label 失败：non-200 OK status code: 403 Forbidden ...GitHub GraphQL is not available from Claude Code sessions...`
   - 绕行：会话自带的 GitHub MCP 工具（REST）写评论成功（#45 评论 6910915981、6910927293）。MCP 只能传文本，图片改用 `git push` 推到 `learn-calculus-note-images` 的 `claude/confident-knuth-oev5eb` 分支，raw 链接 200。
5. **整体体验：** 读照片、出题、git 都正常，但每步都要绕路，不如 Mac。主要差距：tracker 全部依赖 gh GraphQL（要改走 `gh api` REST 或 MCP）；没有 show_widget，公式只能靠发 HTML 文件；git 只能推 `claude/` 分支。

### 2026-11-16 结论：放弃

学习者决定放弃云端学习，维持现状（只在 Mac 本机的 Claude Code 里用，见 ADR 0003）。理由：

- 公式卡片是体验核心（学习者多次强调，也是 2026-11-07 多设备尝试撤回的原因），云端没有 show_widget，每道带公式的题都要另开网页，体验退化。
- `tracker.py` 全部依赖 gh GraphQL，云端被禁；改走 REST 也未验证可行（`gh auth status` 报 token 无效，本次评论是靠会话自带的 GitHub MCP 工具发的）。
- 手机上真正方便的事（看进度、看笔记、改状态）在 GitHub 手机 App 里已经能做。

没有走 Remote Control（学习者明确不要）。02–04 标 wontfix。测试痕迹：#45 上两条“云端试验”评论；`learn-calculus-note-images` 仓库的 `claude/confident-knuth-oev5eb` 分支。
