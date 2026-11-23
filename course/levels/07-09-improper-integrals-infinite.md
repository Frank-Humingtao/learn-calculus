---
id: 07-09
title: 反常积分（无穷区间）
unit: 07 积分技巧
question: 积分区间无限长时，面积还可能是有限的吗？
prereqs: [05-06, 02-10, 07-01, 04-05]
---

## 范围
- 讲：由 $A(t)=\int_1^t\frac{dx}{x^2}=1-\frac1t\to1$ 引入；定义 $\int_a^{+\infty}f=\lim_{t\to+\infty}\int_a^tf$、$\int_{-\infty}^bf=\lim_{t\to-\infty}\int_t^bf$；收敛与发散；$\int_{-\infty}^{+\infty}f$ 要拆成两段且两段都收敛；$\frac1x$ 与 $\frac1{x^2}$ 的对比；p-积分 $\int_1^{+\infty}\frac{dx}{x^p}$ 当 $p>1$ 收敛（值 $\frac1{p-1}$）、$p\le1$ 发散。
- 不讲：被积函数无界的反常积分与比较判定（留给 07-10）。

## 通关标准
1. 能用极限写出无穷区间反常积分的定义，并判断收敛或发散。
2. 能计算需要分部积分和洛必达法则配合的反常积分（如 $\int_{-\infty}^0xe^x\,dx=-1$）。
3. 能正确处理 $\int_{-\infty}^{+\infty}$：拆成两段分别取极限，并说明为什么不能写成 $\lim_{t\to\infty}\int_{-t}^tf$。
4. 能推导并运用 p-积分结论，解释“被积函数趋于 0”并不保证收敛（$\frac1x$ 反例）。

## 学习路径
- 📖 阅读：§7.8 p.542–546 `course/sources/stewart9/072 07 积分技巧 - 7.08 反常积分.pdf`（文字版 `course/extracted/072 07 积分技巧 - 7.08 反常积分.md`），重点 引例与定义 1 p.542–543、例1 p.543–544、例2 p.544、例3 p.545（覆盖 1、2、3）
- 📖 阅读：例4 与 p-积分总结 p.545–546（覆盖 4）
- ✏️ 练习：§7.8 习题 p.549–552 第 3 题（面积随 $t$ 的变化，覆盖 1）；第 5、9、20 题（收敛/发散；$\int_{-\infty}^{+\infty}\frac{x}{x^2+1}$，覆盖 1、3）；第 27、30 题（分部 + 洛必达，覆盖 2）；第 32 题（换元后归结为 p-型，覆盖 4）
- 💬 对话要点：先画 $y=\frac1x$ 与 $y=\frac1{x^2}$，讲清两条曲线都趋于 0，但尾巴下的面积一个无限（$\int_1^\infty\frac1x dx$ 发散）、一个有限（$\int_1^\infty\frac1{x^2}dx=1$），再算出来验证。强调定义就是“先算到 $t$，再让 $t\to\infty$”。讲清 $\int_{-\infty}^{+\infty}x\,dx$ 不等于 0：必须拆成两段且两段都收敛才算收敛，而 $\int_0^{+\infty}x\,dx$ 发散，所以它发散（柯西主值见练习 73，可作拓展）。
- 🎬 MIT 18.01 第 22 讲：视频 [14:06–18:33](https://www.bilibili.com/video/BV1mNgm66EZu?p=22&t=846)（讲义 `course/extracted/mit1801/L22/OCW_18.01_L22_讲义_中文.md`，摘要 `course/prep/mit1801-L22.md`）——标准 1 的直观引子：$\int_0^\infty re^{-r^2}dr$ 收敛，所以“整体”可以取到无穷
- 🎬 MIT 18.01 第 32 讲：视频 [05:27–11:42](https://www.bilibili.com/video/BV1mNgm66EZu?p=32&t=327)；讲义 Definition、Example 1（讲义 `course/extracted/mit1801/L32/OCW_18.01_L32_讲义_中文.md`，摘要 `course/prep/mit1801-L32.md`）——标准 1：定义 + 面积直观；“把 $\infty$ 当端点”的简写及其条件，正对误区“把 $\infty$ 直接代入不写极限”
- 🎬 MIT 18.01 第 32 讲：视频 [11:43–14:03](https://www.bilibili.com/video/BV1mNgm66EZu?p=32&t=703)（讲义 `course/extracted/mit1801/L32/OCW_18.01_L32_讲义_中文.md`，摘要 `course/prep/mit1801-L32.md`）——标准 1：三段真实 Q&A 澄清“收敛 = 极限有限”
- 🎬 MIT 18.01 第 32 讲：视频 [21:00–27:01](https://www.bilibili.com/video/BV1mNgm66EZu?p=32&t=1260)；讲义 Example 4–6（讲义 `course/extracted/mit1801/L32/OCW_18.01_L32_讲义_中文.md`，摘要 `course/prep/mit1801-L32.md`）——标准 4：$p$-积分推导与 $p=1$ 分界，和斯图尔特内容一致
- 🎬 MIT 18.01 第 32 讲：视频 [00:15–05:26](https://www.bilibili.com/video/BV1mNgm66EZu?p=32&t=15)（讲义 `course/extracted/mit1801/L32/OCW_18.01_L32_讲义_中文.md`，摘要 `course/prep/mit1801-L32.md`）——增量：把“衰减谱”作为判敛散的总地图，斯图尔特没有这样组织

## 常见误区
- 以为被积函数趋于 0 积分就收敛（例 1 反例）。
- $\int_{-\infty}^{+\infty}$ 直接写成 $\lim_{t\to\infty}\int_{-t}^t$。
- 把 $\infty$ 当作数直接代入原函数，不写极限过程。
- p-积分的分界记反（$p=1$ 时发散）。

## 导师注意
- 例 2 要用洛必达法则（04-05），若学习者尚未学过需先补。
- OCR 错误：p.542 末式 $\lim\int_t^t$ 应为 $\int_1^t$；定义 1 后“$\int_a^{+\infty}f$ 是……面积的极限”应为 $\int_a^t$；例 3 第二式多出一个“0”；p-积分总结框（正文称“定理 2”）编号丢失。

## 后续
07-10
