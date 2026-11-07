---
id: 03-04
title: 三角函数的导数
unit: 03 求导法则
question: 为什么 $(\sin x)'=\cos x$，关键在于哪个极限？
prereqs: [03-03, 02-05]
---

## 范围
- 讲：由 $\sin$ 的切线斜率图像猜出 $(\sin x)'=\cos x$；用和角公式加两个特殊极限证明；$(\cos x)'=-\sin x$；用商法则推出 $(\tan x)'=\sec^2x$ 等其余公式（共六个）；只在弧度制下成立；简谐运动 $s=4\cos t$ 的速度与加速度；高阶导数 4 个一循环。两个特殊极限 $\lim_{\theta\to0}\frac{\sin\theta}{\theta}=1$（单位圆扇形 + 夹逼定理）与 $\lim_{\theta\to0}\frac{\cos\theta-1}{\theta}=0$，以及“凑形”求三角极限。
- 不讲：$\sin(x^2)$、$\sin^2x$ 这类复合函数（留给 03-05）；反三角函数（留给 03-08）。

## 通关标准
1. 能用单位圆中的不等式 $\sin\theta<\theta<\tan\theta$ 和夹逼定理，说清 $\lim_{\theta\to0}\frac{\sin\theta}{\theta}=1$ 的证明思路，并说出它为什么要求弧度制。
2. 能从导数定义 + 和角公式 + 两个特殊极限推出 $(\sin x)'=\cos x$。
3. 能写出六个三角函数的导数，并用积、商法则求含三角函数的导数，求水平切线。
4. 能用凑形法求 $\lim_{x\to0}\frac{\sin7x}{4x}$ 这类极限，能用循环规律求高阶导数。

## 学习路径
- 📖 阅读：§3.3 p.191–195 `course/sources/stewart9/025 03 求导法则 - 3.03 三角函数的导数.pdf`（文字版 `course/extracted/025 03 求导法则 - 3.03 三角函数的导数.md`），重点 图 3-3-1 p.191–192、$\sin$ 导数的证明 p.192–193、p.194 六个公式表、例 2 p.194（水平切线）、例 3 p.194–195（弹簧）、例 4 p.195（27 阶导数）（覆盖 2、3、4）
- 📖 阅读：同文件 p.195–197，重点 公式 5 的证明（图 3-3-6）p.195–196、例 5 p.196（$\frac{\sin7x}{4x}$）、例 6 p.197（$x\cot x$）（覆盖 1、4）
- ✏️ 练习：§3.3 习题 p.197–199 第 5、13、17、21 题（求导）、第 24 题（证明 $\sec$ 的导数）（覆盖 3）
- ✏️ 练习：同上 第 27、39 题（切线、水平切线）、第 61 题（$\sin x$ 的 99 阶导）（覆盖 3、4）
- ✏️ 练习：同上 第 45、47、51、57 题（三角极限）（覆盖 4）
- ✏️ 挑战（可选）：第 26 题用定义证明 $(\cos x)'=-\sin x$（覆盖 2）
- 💬 对话要点：先让学习者在 $\sin x$ 图像上逐点估切线斜率、描出 $f'$，问“这条曲线像谁”。然后从定义出发卡在 $\frac{\sin h}{h}$ 和 $\frac{\cos h-1}{h}$ 两处，再回头证这两个极限，让他看到整个证明的关键就在这里。追问“如果用角度制，$\lim\frac{\sin\theta}{\theta}$ 还是 1 吗”，检验他是否理解弧度制的作用。（覆盖 1、2）
- 🎬 MIT 18.01 第 2 讲：视频 [25:44–29:05](https://www.bilibili.com/video/BV1mNgm66EZu?p=2&t=1544)（讲义 `course/extracted/mit1801/L02/OCW_18.01_L02_讲义_中文.md`，摘要 `course/prep/mit1801-L02.md`）——只做预告：两个三角极限的陈述与“为什么”的悬念
- 🎬 MIT 18.01 第 3 讲：视频 [02:19–11:00](https://www.bilibili.com/video/BV1mNgm66EZu?p=3&t=139)；讲义 Derivatives of sin x and cos x（讲义 `course/extracted/mit1801/L03/OCW_18.01_L03_讲义_中文.md`，摘要 `course/prep/mit1801-L03.md`）——标准 2（合角 + 两个特殊极限推 $\sin'=\cos$）；“A、B 就是零点导数、一点定全局”是斯图尔特没有的视角
- 🎬 MIT 18.01 第 3 讲：视频 [11:00–25:55](https://www.bilibili.com/video/BV1mNgm66EZu?p=3&t=660)；L02 讲义图 fig12–fig15（讲义 `course/extracted/mit1801/L03/OCW_18.01_L03_讲义_中文.md`，摘要 `course/prep/mit1801-L03.md`）——标准 1 的“为什么要弧度制”部分；五个真实追问可作诊断题。注意不覆盖标准 1 要求的“不等式 + 夹逼”写法
- 🎬 MIT 18.01 第 3 讲：视频 [25:55–36:01](https://www.bilibili.com/video/BV1mNgm66EZu?p=3&t=1555)（讲义 `course/extracted/mit1801/L03/OCW_18.01_L03_讲义_中文.md`，摘要 `course/prep/mit1801-L03.md`）——增量：任意角的纯几何证明，作为补充或学有余力的拓展
- 🎬 MIT 18.01 第 4 讲：视频 [25:54–27:38](https://www.bilibili.com/video/BV1mNgm66EZu?p=4&t=1554)（讲义 `course/extracted/mit1801/L04/OCW_18.01_L04_讲义_中文.md`，摘要 `course/prep/mit1801-L04.md`）——标准 4（高阶导数四个一循环）
- 🎬 MIT 18.01 第 5 讲：视频 [32:06–33:23](https://www.bilibili.com/video/BV1mNgm66EZu?p=5&t=1926)（讲义 `course/extracted/mit1801/L05/OCW_18.01_L05_讲义_中文.md`，摘要 `course/prep/mit1801-L05.md`）——标准 3：$(\tan x)'=\sec^2x$ 由商法则得到（课上留作练习）
- 🎬 MIT 18.01 第 7 讲：视频 [19:19–20:57](https://www.bilibili.com/video/BV1mNgm66EZu?p=7&t=1159)；[28:04–30:35](https://www.bilibili.com/video/BV1mNgm66EZu?p=7&t=1684)；讲义 Specific formulas（讲义 `course/extracted/mit1801/L07/OCW_18.01_L07_讲义_中文.md`，摘要 `course/prep/mit1801-L07.md`）——$\sec x$ 导数的标准形；$(\sin x)'$ 要会从两个特殊极限证（Q&A t=1562）
- 🎬 MIT 18.01 第 25 讲：视频 [02:23–04:39](https://www.bilibili.com/video/BV1mNgm66EZu?p=25&t=143)、[06:49–09:39](https://www.bilibili.com/video/BV1mNgm66EZu?p=25&t=409)（讲义 `course/extracted/mit1801/L25/OCW_18.01_L25_讲义_中文.md`，摘要 `course/prep/mit1801-L25.md`）——用商法则推 $\tan,\sec$ 的导数，以及对数导数 $u'/u=(\ln u)'$ 的一次应用

## 常见误区
- 在角度制下套用这些公式（教材明确提醒只适用于弧度）。
- 凑形时写成 $\sin7x=7\sin x$，或者凑出 $\frac{\sin7x}{7x}$ 后忘了补系数。
- $\sec$、$\csc$、$\cot$ 的导数符号记混；口诀：带“余”字的（cos、csc、cot）导数都带负号。

## 导师注意
- OCR 错误：公式 5 证明最后一行把双侧极限写成了 $0^+$，实际是先证右侧、再由偶函数得双侧，引用时以原 PDF 为准。
- 例 3 的弹簧示意图、图 3-3-6 单位圆扇形图在 OCR 中缺失，讲证明时要看原 PDF。
- 部分练习（如 10、12、16、29、34、40）含 $e^x$，需要 03-02。
- （18.01）18.01 L03 用“短弧约等于弦”直观说明 $\frac{\sin\theta}\theta\to1$，不是严格证明；标准 1 的夹逼证明仍以斯图尔特为准。

## 后续
03-05
