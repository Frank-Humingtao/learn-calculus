---
id: 07-02
title: 三角函数的积分
unit: 07 积分技巧
question: $\sin^m x\cos^n x$、$\tan^m x\sec^n x$ 的积分，按什么规律拆？
prereqs: [05-08, 03-04]
---

## 范围
- 讲：$\int\sin^m x\cos^n x\,dx$ 的三种情形（$\cos$ 奇次留一个 $\cos x$ 令 $u=\sin x$；$\sin$ 奇次反之；都偶次用半角公式）；$\int\tan^m x\sec^n x\,dx$ 的两种情形（$\sec$ 偶次留 $\sec^2x$ 令 $u=\tan x$；$\tan$ 奇次留 $\sec x\tan x$ 令 $u=\sec x$）；$\int\sec x\,dx=\ln|\sec x+\tan x|+C$；$\int\sec^3x\,dx$（分部 + 解方程）；积化和差处理 $\int\sin mx\cos nx\,dx$ 等。
- 不讲：三角换元（留给 07-03）；三角函数系正交性与傅里叶系数（练习 75–78，可作拓展）。

## 通关标准
1. 能说出“奇次幂拆出一个因子做换元，余下的偶次幂用 $\sin^2x+\cos^2x=1$ 改写”的统一思想，并据此判断 $\sin^m x\cos^n x$ 该用哪条策略。
2. 能计算两者都是偶次的情形（半角公式，如 $\int\sin^4x\,dx$），并解释为什么改写成 $1-\cos^2x$ 无用。
3. 能计算 $\tan^m x\sec^n x$ 的两类标准情形，并会推导 $\int\sec x\,dx$、用分部求 $\int\sec^3x\,dx$。
4. 能用积化和差公式计算 $\int\sin mx\cos nx\,dx$ 一类积分。

## 学习路径
- 📖 阅读：§7.2 p.493–495 `course/sources/stewart9/066 07 积分技巧 - 7.02 三角函数的积分.pdf`（文字版 `course/extracted/066 07 积分技巧 - 7.02 三角函数的积分.md`），重点 例1、例2 p.493，例3、例4 p.494，策略框 p.495（覆盖 1、2）
- 📖 阅读：p.495–498 例5 p.495、例6 与策略框 p.496、$\int\sec x$ 公式与例7 p.497、例8 p.497–498、例9 p.498（覆盖 3、4）
- ✏️ 练习：§7.2 习题 p.498–500 第 1、4、9 题（奇次/偶次幂，覆盖 1、2）；第 22、27、31 题（正切正割，覆盖 3）；第 43 题（积化和差，覆盖 4）；第 64 题（四种方法求 $\int\sin x\cos x\,dx$，覆盖 1）
- 💬 对话要点：从“要令 $u=\sin x$，被积函数里得有一个 $\cos x\,dx$”这个需求倒推出拆因子的做法，让学习者自己归纳策略框，而不是先背表。追问：$\sin^2x\cos^2x$ 为什么没法拆？$\tan^2x\sec x$ 两条策略都不适用时怎么办（化成 $\sec^3x-\sec x$）？检验：给 3 个积分只让他说“留哪个因子、令 $u$ 为什么”。
- 🎬 MIT 18.01 第 24 讲：视频 [00:59–05:13](https://www.bilibili.com/video/BV1mNgm66EZu?p=24&t=59)（讲义 `course/extracted/mit1801/L24/OCW_18.01_L24_讲义_中文.md`，摘要 `course/prep/mit1801-L24.md`）——半角公式的来历（由 $\cos2\theta$ 推出），作为标准 2 的预备
- 🎬 MIT 18.01 第 24 讲：视频 [07:21–18:03](https://www.bilibili.com/video/BV1mNgm66EZu?p=24&t=441)；讲义 Method A、Example 1–2（讲义 `course/extracted/mit1801/L24/OCW_18.01_L24_讲义_中文.md`，摘要 `course/prep/mit1801-L24.md`）——标准 1：奇次拆因子的统一思想；“漏负号”的真实问答可作为常见误区示范
- 🎬 MIT 18.01 第 24 讲：视频 [18:04–29:45](https://www.bilibili.com/video/BV1mNgm66EZu?p=24&t=1084)；讲义 Method B、Example 3（讲义 `course/extracted/mit1801/L24/OCW_18.01_L24_讲义_中文.md`，摘要 `course/prep/mit1801-L24.md`）——标准 2：偶次幂用半角公式，$\sin^2\cos^2$ 两种做法
- 🎬 MIT 18.01 第 25 讲：视频 [00:45–12:11](https://www.bilibili.com/video/BV1mNgm66EZu?p=25&t=45)；讲义（L24）sec/tan 段（讲义 `course/extracted/mit1801/L25/OCW_18.01_L25_讲义_中文.md`，摘要 `course/prep/mit1801-L25.md`）——标准 3：$\tan^m\sec^n$ 的 sec 偶次情形（$\sec^4$），推导 $\int\sec$；增量：用对数导数推 $\int\sec$，比斯图尔特“乘 $\frac{\sec+\tan}{\sec+\tan}$”更有道理

## 常见误区
- 奇次幂情形也去用半角公式，绕远路；偶次幂硬拆因子导致无法换元。
- 对 $\cos2x$ 积分忘乘 $\frac12$（教材注明默认用了换元 $u=2x$）。
- 把 $\int\sec x\,dx$ 记成 $\ln|\sec x|$，与 $\int\tan x\,dx=\ln|\sec x|+C$ 混淆。
- 积化和差时 $\sin(-x)=-\sin x$ 的符号处理出错。

## 导师注意
- OCR 错误：例 2 中“$u=-\sin x\,dx$”应为 $du=-\sin x\,dx$；$\tan^m x\sec^n x$ 策略 (a) 中“$n=2k+1$, $k\ge2$”应为 $n=2k$。
- 练习区双栏错乱、题号乱序（61–66 混在 30–60 之间），按题号找题时需对照原 PDF。
- 例 2 的图 7-2-1（判断哪条是原函数）需看原 PDF。

## 后续
07-03
