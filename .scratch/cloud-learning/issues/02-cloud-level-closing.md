# 02: 云端闯关能完整收尾

**What to build:** 在手机云端会话里打完一关后，收尾的每一步都和本机一样能做完：看进度、改状态、写学习记录、发笔记（含手机拍的手写照片）。

已知卡点（以 01 实测为准）：
- `tracker.py` 全部经 `gh` 读写 GitHub Issues，第一次发笔记还会建公开图片仓库；云端未必有 `gh` 登录和对应权限。认证方式按 01 的结果定，凭证由学习者自己在云端环境里配置，不写进仓库。
- 手机照片常是 HEIC；本机靠 Mac 的 `sips` 转 JPEG 和压缩，云端（Linux）没有。
- 可视化截图依赖 Chrome；没有时笔记里应改用 LaTeX 重写，而不是报错中断。

**Blocked by:** 01

**Status:** wontfix（01 实测后学习者决定放弃云端学习，见 01 的 Comments）

- [ ] 云端会话里 `tracker.py` 的 status / show / set / comment / erratum 正常工作
- [ ] 云端会话里 `tracker.py note` 能发笔记，HEIC 和 JPEG 照片都能显示在笔记 issue 里（GitHub 手机 App 能看到）
- [ ] 没有 Chrome 时，截可视化的那一步给出明确的“改用 LaTeX”提示，收尾流程不中断
- [ ] 本机 Mac 上的行为不变（回归：在本机发一条测试笔记仍正常）
- [ ] 学习者在手机上真实打一关，收尾完整走通
