---
id: 07-03
title: 三角换元
unit: 07 积分技巧
question: 遇到 $\sqrt{a^2-x^2}$ 这类根式，为什么要换成三角函数？
prereqs: [07-02]
---

## 范围
- 讲：逆换元 $x=g(t)$ 与普通换元的区别、为何要求 $g$ 一对一（限制 $\theta$ 范围）；表 7-3-1 三种根式：$\sqrt{a^2-x^2}\to x=a\sin\theta$，$\sqrt{a^2+x^2}\to x=a\tan\theta$，$\sqrt{x^2-a^2}\to x=a\sec\theta$；画直角三角形把结果换回 $x$；定积分直接换积分限；先配方/线性换元再三角换元；双曲换元作为对照。
- 不讲：有理换元 $u=\sqrt[n]{g(x)}$（留给 07-05）。

## 通关标准
1. 能根据根式形式选出正确的三角换元，并说明为什么要限制 $\theta$ 的范围（开根号时 $|\cos\theta|=\cos\theta$）。
2. 能完成不定积分的三角换元，并用直角三角形把 $\cot\theta$、$\sec\theta$ 等换回 $x$。
3. 能对定积分做三角换元并正确换限（如椭圆面积 $\pi ab$）。
4. 能先配方（如 $3-2x-x^2=4-(x+1)^2$）再换元，并能识别“直接 $u$ 换元更简单”而不必三角换元的情形。

## 学习路径
- 📖 阅读：§7.3 p.500–502 `course/sources/stewart9/067 07 积分技巧 - 7.03 三角换元.pdf`（文字版 `course/extracted/067 07 积分技巧 - 7.03 三角换元.md`），重点 表 7-3-1 p.500、例1 p.501、例2 p.501–502（覆盖 1、2、3）
- 📖 阅读：p.502–505 例3 p.502、例4 p.503（“注”）、例5 p.503–504、例6 p.504、例7 p.504–505（覆盖 2、4）
- ✏️ 练习：§7.3 习题 p.505–506 第 1–4 题（只选换元，覆盖 1）；第 5、7 题（给定换元并画三角形，覆盖 2）；第 13、21 题（定积分换限，覆盖 3）；第 24、29 题（直接换元 vs. 配方后三角换元，覆盖 4）
- 💬 对话要点：用 $\sin^2\theta+\cos^2\theta=1$、$1+\tan^2\theta=\sec^2\theta$ 让学习者自己看出每种根式“配”哪个恒等式。追问“$x=3\sin\theta$ 和 $u=9-x^2$ 有什么本质区别”“为什么 $\theta$ 要在 $[-\pi/2,\pi/2]$”。检验：给出 $\int\frac{x}{\sqrt{x^2+4}}dx$，看他会不会先想到直接换元。
- 🎬 MIT 18.01 第 24 讲：视频 [29:46–46:44](https://www.bilibili.com/video/BV1mNgm66EZu?p=24&t=1786)；讲义 Example 4 / fig1–fig2（讲义 `course/extracted/mit1801/L24/OCW_18.01_L24_讲义_中文.md`，摘要 `course/prep/mit1801-L24.md`）——标准 1、2、3：$\sqrt{a^2-y^2}$ 用 $a\sin\theta$ 换元；增量：用扇形加三角形几何核验结果，斯图尔特例 2（椭圆面积）没有这种复核
- 🎬 MIT 18.01 第 25 讲：视频 [12:12–25:47](https://www.bilibili.com/video/BV1mNgm66EZu?p=25&t=732)（讲义 `course/extracted/mit1801/L25/OCW_18.01_L25_讲义_中文.md`，摘要 `course/prep/mit1801-L25.md`）——标准 2：$x=\tan\theta$ 换元加三角形还原 $\csc\theta$；“为什么想到 tan”“为什么 $u=\sin$”两个真实问答可直接作为追问
- 🎬 MIT 18.01 第 25 讲：视频 [25:49–29:07](https://www.bilibili.com/video/BV1mNgm66EZu?p=25&t=1549)；讲义三列表（讲义 `course/extracted/mit1801/L25/OCW_18.01_L25_讲义_中文.md`，摘要 `course/prep/mit1801-L25.md`）——标准 1：三种根式对应三种换元
- 🎬 MIT 18.01 第 25 讲：视频 [29:09–37:34](https://www.bilibili.com/video/BV1mNgm66EZu?p=25&t=1749)；讲义配方例 / fig4（讲义 `course/extracted/mit1801/L25/OCW_18.01_L25_讲义_中文.md`，摘要 `course/prep/mit1801-L25.md`）——标准 4：先配方再用 sec 换元；常数 $-\ln2$ 并入 $\tilde C$，正对卡片上“两种答案差一个常数”的误区
- 🎬 MIT 18.01 第 26 讲：讲义“高次二次幂：三角换元”（$\int\frac{dx}{(x^2+1)^{10}}\to\int\cos^{18}u\,du$）（讲义 `course/extracted/mit1801/L26/OCW_18.01_L26_讲义_中文.md`，摘要 `course/prep/mit1801-L26.md`）——补充例：部分分式与三角换元、三角积分的衔接
- 🎬 MIT 18.01 第 28 讲：视频 [15:13–19:33](https://www.bilibili.com/video/BV1mNgm66EZu?p=28&t=913)（讲义 `course/extracted/mit1801/L28/OCW_18.01_L28_讲义_中文.md`，摘要 `course/prep/mit1801-L28.md`）——标准 1：$\sqrt{1+4x^2}$ 选 $x=\frac12\tan u$ 的应用例
- 🎬 MIT 18.01 第 30 讲：讲义 Handout 第 1 条（讲义 `course/extracted/mit1801/L30/OCW_18.01_L30_讲义_中文.md`，摘要 `course/prep/mit1801-L30.md`）——标准 1、2：三种根式与换元的对照表，用直角三角形换回原变量

## 常见误区
- 见到根式就机械套三角换元（教材例 4 注专门提醒）。
- 不定积分忘记换回原变量；画三角形时边标错。
- 不理解 $\theta$ 范围的作用，开根号时绝对值处理不清。
- 配方出错；多重换元后换积分限漏一步；看到三角与双曲换元两种答案以为有一个错（常数 $-\ln a$ 可被吸收）。

## 导师注意
- OCR 错误：例 3 中 $\theta$ 范围应为开区间 $-\pi/2<\theta<\pi/2$，“$\csc\theta=\sqrt{x^2+4/x}$”应为 $\sqrt{x^2+4}/x$；例 6 换成 $u=\cos\theta$ 后积分限“$\int_0^{1/2}$”应为 $\int_1^{1/2}$。
- 练习 16 的积分限 $\int_2^{2/3}$ 疑为 $\int_0^{2/3}$。
- 直角三角形图（图 7-3-1 等）需看原 PDF。

## 后续
07-06
