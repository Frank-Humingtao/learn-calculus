---
id: 03-12
title: 线性近似与微分
unit: 03 求导法则
question: 为什么切线能近似曲线？$dy$ 和 $\Delta y$ 差在哪里？
prereqs: [02-12, 03-05]
---

## 范围
- 讲：可微函数的局部线性；线性化 $L(x)=f(a)+f'(a)(x-a)$ 与线性近似 $f(x)\approx L(x)$；离 $a$ 越远误差越大，用图像求满足精度的区间；物理中的 $\sin x\approx x$、$\cos\theta\approx1$；微分 $dy=f'(x)\,dx$ 的定义与几何意义（沿切线 vs 沿曲线）；$\Delta y\approx dy$；用微分估计测量误差，相对误差与百分误差。
- 不讲：二次及更高次的多项式近似、泰勒多项式（p.260–261 探索专题，第 11 章）；牛顿法（留给 04-10）。

## 通关标准
1. 能写出函数在给定点的线性化，并用它估算如 $\sqrt{4.05}$、$\sqrt[3]{1001}$ 之类的数值。
2. 能根据切线在曲线上方还是下方，判断近似值偏大还是偏小。
3. 能画图说明 $dy$（沿切线的升降）与 $\Delta y$（沿曲线的升降）的区别，并计算比较二者。
4. 能用微分估计测量误差带来的最大误差，并换算成相对误差（如 $\frac{dV}{V}=3\frac{dr}{r}$）。

## 学习路径
- 📖 阅读：§3.10 p.254–256 `course/sources/stewart9/032 03 求导法则 - 3.10 线性近似与微分.pdf`（文字版 `course/extracted/032 03 求导法则 - 3.10 线性近似与微分.md`），重点 例 1 p.254–255（$\sqrt{x+3}$ 在 $a=1$ 处）、表 3-10-1、例 2 p.255–256（精度区间）、p.256 物理中的应用（覆盖 1、2）
- 📖 阅读：同文件 p.256–258，重点 图 3-10-5（$dy$ 与 $\Delta y$）、例 3 p.257（比较 $\Delta y$ 与 $dy$）、例 4 p.258（球体积误差与相对误差）（覆盖 3、4）
- ✏️ 练习：§3.10 习题 p.258–260 第 1、3、5 题（求线性化并估值）、第 7 题（验证 $\tan^{-1}x\approx x$ 并确定精度范围）（覆盖 1、2）
- ✏️ 练习：同上 第 13、19 题（求微分并代值）、第 23、27 题（比较 $\Delta y$ 与 $dy$）（覆盖 3）
- ✏️ 练习：同上 第 31、33、36 题（线性近似估值，注意 $\cos29^\circ$ 要换成弧度）、第 41、43 题（测量误差与相对误差）（覆盖 1、4）
- 💬 对话要点：先让学习者在 Desmos 里把 $\sqrt{x+3}$ 在 $(1,2)$ 附近不断放大，看曲线“变直”，引出“局部线性”。追问：“$\sqrt{3.98}$ 的近似值偏大还是偏小？为什么？”检验他是否会看切线位置。最后让他口述 $dx$、$dy$、$\Delta y$ 三者在图上各是哪条线段。（覆盖 1、2、3）
- 🎬 MIT 18.01 第 2 讲：视频 [09:13–13:28](https://www.bilibili.com/video/BV1mNgm66EZu?p=2&t=553)；讲义图 fig2/fig3（讲义 `course/extracted/mit1801/L02/OCW_18.01_L02_讲义_中文.md`，摘要 `course/prep/mit1801-L02.md`）——作为动机补充：$\Delta L\approx\frac{dL}{dh}\Delta h$ 就是微分/误差传播的雏形
- 🎬 MIT 18.01 第 8 讲：视频 [00:30–16:07](https://www.bilibili.com/video/BV1mNgm66EZu?p=8&t=30)；讲义 Linear Approximation、Example 1、Basic list、Fig 1–2（讲义 `course/extracted/mit1801/L08/OCW_18.01_L08_讲义_中文.md`，摘要 `course/prep/mit1801-L08.md`）——标准 1；三种解读讲透同一公式；$x_0=0$ 五条目录比斯图尔特零散的 $\sin x\approx x$ 更系统
- 🎬 MIT 18.01 第 8 讲：视频 [16:07–30:18](https://www.bilibili.com/video/BV1mNgm66EZu?p=8&t=967)；讲义 Example 2、4（讲义 `course/extracted/mit1801/L08/OCW_18.01_L08_讲义_中文.md`，摘要 `course/prep/mit1801-L08.md`）——标准 1、4；组合近似“拼目录 + 扔高阶”是斯图尔特没有的技巧；GPS 例的 $\Delta T/T\approx\frac12v^2/c^2$ 是相对误差的真实场景
- 🎬 MIT 18.01 第 8 讲：视频 [30:18–36:34](https://www.bilibili.com/video/BV1mNgm66EZu?p=8&t=1818)；讲义 Quadratic Approximations、Fig 4（讲义 `course/extracted/mit1801/L08/OCW_18.01_L08_讲义_中文.md`，摘要 `course/prep/mit1801-L08.md`）——超出 03-12 范围（卡片“不讲”二次近似），见下
- 🎬 MIT 18.01 第 9 讲：视频 [00:15–06:34](https://www.bilibili.com/video/BV1mNgm66EZu?p=9&t=15)（讲义 `course/extracted/mit1801/L09/OCW_18.01_L09_讲义_中文.md`，摘要 `course/prep/mit1801-L09.md`）——标准 4；相对误差的无量纲比例读法、“压成拇指法则”的工程观
- 🎬 MIT 18.01 第 13 讲：视频 [27:24–29:41](https://www.bilibili.com/video/BV1mNgm66EZu?p=13&t=1644)；讲义图 3（讲义 `course/extracted/mit1801/L13/OCW_18.01_L13_讲义_中文.md`，摘要 `course/prep/mit1801-L13.md`）——线性近似与 MVT 的对照，回扣 03-12 的线性化（复习用）
- 🎬 MIT 18.01 第 14 讲：视频 [00:16–10:34](https://www.bilibili.com/video/BV1mNgm66EZu?p=14&t=16)；讲义 Example 1 Method 1–3（讲义 `course/extracted/mit1801/L14/OCW_18.01_L14_讲义_中文.md`，摘要 `course/prep/mit1801-L14.md`）——标准 1（$\sqrt[3]{\ }$ 型估算）、标准 3（$dy$ 沿切线 vs $\Delta y$ 沿曲线）；增量：莱布尼茨记号史，三种方法对照
- 🎬 MIT 18.01 第 31 讲：视频 [16:35–18:18](https://www.bilibili.com/video/BV1mNgm66EZu?p=31&t=995)（讲义 `course/extracted/mit1801/L31/OCW_18.01_L31_讲义_中文.md`，摘要 `course/prep/mit1801-L31.md`）——补充：线性／二次近似的一个应用场景（二次近似属斯图尔特 11 章，此处只作展示）
- 🎬 MIT 18.01 第 34 讲：视频 [37:01–38:25](https://www.bilibili.com/video/BV1mNgm66EZu?p=34&t=2221)（讲义 `course/extracted/mit1801/L34/OCW_18.01_L34_讲义_中文.md`，摘要 `course/prep/mit1801-L34.md`）——补充：线性近似 $\sin x\approx x$ 是泰勒级数的第一项；03-12 范围“不讲”高阶，只作展望

## 常见误区
- 在远离 $a$ 的点使用线性近似，仍以为很准。
- 判断偏大偏小时不看切线在曲线上方还是下方。
- 混淆 $\Delta y$ 与 $dy$，以为二者相等。
- 只算绝对误差，不会换算为相对误差或百分误差。
- 估算三角函数值时没把角度换成弧度。

## 导师注意
- 例 2 与练习 1–10 需要画图确定精度区间，教材原用绘图软件，可用 Desmos 或 Python 代替（这是补充）。
- 前置 02-12 用于回顾切线方程；如果学习者对切线方程很熟，可以直接开始。
- （18.01）18.01 L08 视频用 $e^{-3x}$，讲义用 $e^{-2x}$，系数不同，引用时说清以哪个为准。二次近似留给 03-14（选学）。

## 后续
03-13
