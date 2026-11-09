---
name: learn-prep
description: 备课：把 course/sources/ 里的视频和 PDF 提取成文字与关键帧，逐份摘要，合并成总框架 SYLLABUS.md 交学习者审核，确认后生成关卡卡片并发布为 GitHub issue。学习者放入新素材或要求（重新）梳理课程时使用。
---

# 备课

备课分 5 步，**第 4 步必须停下来等学习者审核**。每步产物都落盘，中断后可从断点继续：先看哪些产物已存在。

先 `source .venv/bin/activate`（没有 `.venv` 就 `bash scripts/setup.sh`）。原始素材只在主目录（`git worktree list` 第一行）的 `course/sources/`；在 worktree 里备课时，提取命令直接用主目录里的素材路径。

## 1. 提取（本地，不读内容）

对 `course/sources/` 中每个还没有提取结果的文件：

| 素材 | 命令 | 产物 |
|---|---|---|
| PDF | `python3 scripts/extract_pdf.py <pdf>` | `course/extracted/<名>.md` |
| 视频 | `python3 scripts/extract_video.py <视频> [--lang en]`（同名 .srt/.vtt 会自动使用；没有字幕就本地转写，很慢，放后台跑） | `course/extracted/<名>.transcript.md` |
| 视频 | `python3 scripts/keyframes.py <视频>` | `course/frames/<名>/` |

PDF 若提示扫描版，或抽查发现文字层是乱码（中文缺失、公式错乱）：改用 `python3 scripts/ocr_pdf.py <pdf 或目录>`（MinerU 本地 OCR，产物格式相同，页标记带印刷页码 `<!-- page N | p.105 -->`，约 7 秒/页，放后台跑）。没装 MinerU 时先征得学习者同意：它要 Python ≥ 3.10，用 `uv tool install --python 3.12 'mineru[all]'` 装，模型用 `mineru-kit models download --tier standard --source modelscope` 下。少量页可直接用读图能力读 PDF 页面。
抽查每个产物开头和中间一段，确认不是乱码。

## 2. 逐份摘要 → `course/prep/<名>.md`

**每份素材单独处理，不要一次把所有素材读进上下文。** 支持子代理就每份素材派一个子代理并行做，只把摘要文件路径带回来。

摘要格式：

```markdown
# <素材名>（视频 / 教材）
类型与风格：例如“MIT 18.01 第 3 讲，偏直观，板书推导多”

## <素材自身的小节>  [00:03:10–00:15:40] 或 [p.45–48]
- 概念：……
- 关键推导/例题：……（视频：对应关键帧 frames/<名>/001230.jpg）
- 讲法特点：……
- 学生可能的误区：……
```

视频的小节边界以文字稿时间戳为准；文字稿提到“看这里/this”等指代时，查看该时刻附近的关键帧补全内容。

## 3. 合并 → `course/SYLLABUS.md`

读全部 `course/prep/*.md`（只读摘要，不读原文），对齐不同素材讲同一内容的地方，拆成单元和关卡：

- 关卡 10–20 分钟，用一个**核心问题**来定义（例如“为什么 0/0 型的极限仍然可能存在？”）。
- 关卡 id：`<两位单元号>-<两位关卡号>`，如 `02-03`。
- 前置只引用排在前面的关卡。

```markdown
# <课程名> 总框架

素材：列出每份素材及一句话特点

## 01 <单元名>
| id | 关卡 | 核心问题 | 前置 | 素材覆盖 |
|---|---|---|---|---|
| 01-01 | … | …？ | — | 18.01 L1 05:00–18:00；Stewart p.12–15 |
```

最后列出：素材之间讲法冲突或互补的地方、素材没覆盖需要导师补充的地方。

## 4. 学习者审核（停下来）

用几句话概括框架（多少单元、多少关、整体顺序的考虑），请学习者看 `course/SYLLABUS.md` 并提修改意见。按意见改，直到他明确确认。**没有确认不要进入第 5 步。**

## 5. 卡片与发布

为每个关卡写 `course/levels/<id>-<英文短名>.md`：

```markdown
---
id: 02-03
title: 极限的 ε-δ 定义
unit: 02 极限与连续
question: 怎样把“无限接近”说得完全精确？
prereqs: [02-01, 02-02]
---

## 范围
- 讲：……
- 不讲：……（留给 02-05）

## 通关标准
1. 能用自己的话解释 ε 和 δ 各自代表什么
2. 能对线性函数写出 ε-δ 证明
3. 能判断一个给定的 δ 选取是否成立

## 学习路径
- 🎬 视频：18.01 第 3 讲 `course/sources/lec03.mp4` 12:30–25:00，板书见 `course/frames/lec03/` 中 001300–002400 的帧（覆盖标准 1、2）
- 📖 阅读：Stewart 第 2.4 节 `course/sources/stewart.pdf` p.110–114（覆盖 1、2、3）
- 💬 对话要点：先从“误差容忍度”的比喻讲起……（覆盖 1、3）

## 常见误区
- 以为 δ 必须由 ε 唯一确定
- ……

## 后续
02-04
```

写完运行：

```bash
python3 scripts/tracker.py publish --dry-run   # 先检查
python3 scripts/tracker.py publish             # 建 milestone + issue，写入 course/issues.json
```

然后 `git add course && git commit && git push`。

告诉学习者备课完成，建议下一步做摸底（`learn-diagnose`）。

## 增量更新

后来又加了素材：只对新素材做 1–2 步，再把它挂到已有卡片的“学习路径”上；确实有新内容才新增关卡（新增也要先让学习者确认）。**已发布关卡的 id 不改不删。**

增量备课同样以 `git push` 收尾。

## 处理卡片勘误

闯关时发现的卡片问题记在 issue 上（label `卡片勘误`）。备课时先 `python3 scripts/tracker.py status` 看“待修卡片勘误”，逐个 `tracker.py show <id>` 读勘误评论，改卡片，提交后 `tracker.py erratum <id> --fixed`。
