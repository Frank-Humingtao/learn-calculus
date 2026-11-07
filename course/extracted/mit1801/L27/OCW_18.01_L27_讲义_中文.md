# MIT OCW 18.01 Lecture 30 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L27_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P27**（27-分部积分与降阶）对齐。对应的官方 PDF 实为 Fall 2006 **`lec30.pdf`（Lecture 30: Integration by Parts, Reduction Formulae）**。OCW 课程日历中的 **Lecture 8** 是 Exam 1、**Lecture 17** 是 Exam 2、**Lecture 27** 是 Exam 3，**都没有**常规讲义 PDF / 本系列课堂录像（lec27 为空桩／Exam stub）；故对 \(n\ge16\) 有 Bilibili **P27 ↔ OCW Lecture 30**（Pn ≈ lec\((n+2)\)；跳过空的 lec27）。课堂口播（Jerison：先收尾部分分式大例，再分部积分／降阶／酒杯应用）与讲义的差异见同目录 [`MIT1801_L27_课上思路.md`](./MIT1801_L27_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec30.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。**本文件只转写 lec30.pdf 中「分部积分／降阶公式」正文（notes pp.1–3；`ocw_pages/page-2.png`…`page-4.png`）**。同一 PDF 后半为 **Arc Length / Parametric Equations**（notes pp.4–8，含 Figure 1–8），属下一话题，**不收入本文**；那些图未裁入 `ocw_figs/`（见 README 与 `ocw_figs/NOTE_no_figures.txt`）。分部积分／降阶页**无插图**。

---

## Lecture 30: Integration by Parts, Reduction Formulae

（第 30 讲：分部积分与降阶公式）

18.01 Fall 2006

---

### Integration by Parts（分部积分）

记住乘积法则：

\[
(uv)'=u'v+uv'.
\]

可改写为

\[
uv'=(uv)'-u'v.
\]

两边积分，得到分部积分公式：

\[
\int uv'\,dx=uv-\int u'v\,dx.
\]

---

### Example 1. \(\displaystyle\int\tan^{-1}x\,dx\)

乍看并不清楚分部积分如何帮忙。写成

\[
\int\tan^{-1}x\,dx=\int\tan^{-1}x\,(1\cdot dx)=\int uv'\,dx,
\]

其中

\[
u=\tan^{-1}x,\qquad v'=1.
\]

于是

\[
v=x,\qquad u'=\frac{1}{1+x^{2}}.
\]

代入分部积分公式：

\[
\int\tan^{-1}x\,dx
=x\tan^{-1}x-\int\frac{1}{1+x^{2}}\cdot x\,dx
=x\tan^{-1}x-\frac12\ln|1+x^{2}|+c.
\]

---

### Alternative Approach to Integration by Parts（另一写法）

同上，由乘积法则

\[
(uv)'=u'v+uv'
\]

改写为

\[
uv'=(uv)'-u'v.
\]

这次取**定积分**：

\[
\int_{a}^{b}uv'\,dx=\int_{a}^{b}(uv)'\,dx-\int_{a}^{b}u'v\,dx.
\]

由微积分基本定理：

\[
\int_{a}^{b}uv'\,dx=uv\Big|_{a}^{b}-\int_{a}^{b}u'v\,dx.
\]

不定积分的另一记法是

\[
\int u\,dv=uv-\int v\,du.
\]

二者相同，因为

\[
dv=v'\,dx\implies uv'\,dx=u\,dv,
\qquad
du=u'\,dx\implies u'v\,dx=v\,du.
\]

---

### Example 2. \(\displaystyle\int(\ln x)\,dx\)

\[
u=\ln x,\quad du=\frac{1}{x}\,dx;\qquad
dv=dx,\quad v=x.
\]

\[
\int(\ln x)\,dx
=x\ln x-\int x\cdot\frac{1}{x}\,dx
=x\ln x-\int dx
=x\ln x-x+c.
\]

也可用「高级猜测」：找某个函数导数等于 \(\ln x\)。试

\[
\frac{d}{dx}(x\ln x)=\ln x+x\cdot\frac{1}{x}=\ln x+1.
\]

几乎对，但多了 \(1\)。修正猜测：

\[
\frac{d}{dx}(x\ln x-x)=\ln x+1-1=\ln x.
\]

---

### Reduction Formulas (Recurrence Formulas)（降阶／递推公式）

#### Example 3. \(\displaystyle\int(\ln x)^{n}\,dx\)

取

\[
u=(\ln x)^{n}\implies u'=n(\ln x)^{n-1}\cdot\frac{1}{x},
\qquad
v'=1,\quad v=x.
\]

代入分部积分：

\[
\int(\ln x)^{n}\,dx
=x(\ln x)^{n}-\int n(\ln x)^{n-1}\,dx
\]

（中间 \(x\cdot(1/x)\) 消去）。不断重复分部积分，得到完整降阶：

\[
n\to(n-1)\to(n-2)\to(n-3)\to\cdots
\]

#### Example 4. \(\displaystyle\int x^{n}e^{x}\,dx\)

取

\[
u=x^{n}\implies u'=nx^{n-1};\qquad
v'=e^{x}\implies v=e^{x}.
\]

代入：

\[
\int x^{n}e^{x}\,dx=x^{n}e^{x}-\int nx^{n-1}e^{x}\,dx.
\]

重复：\(n\to(n-1)\to(n-2)\to\cdots\)。

---

### 坏消息与好消息

**坏消息**：积分只要稍改一点，就可能无法用初等函数求出：

\[
\int\bigl(\tan^{-1}x\bigr)^{2}\,dx=\text{impossible（不可初等）},
\]

\[
\int\frac{e^{x}}{x}\,dx=\text{also impossible}.
\]

**好消息**：求不出原函数时，

\[
\int_{1}^{2}\frac{e^{x}}{x}\,dx
\]

本身就是**答案**，而不是问题——你不必再「积出来」！

最重要的是**把积分设对**（设好之后总可以用计算机数值计算）。那为什么还要手算积分？因为常常遇到**一族相关积分**，例如

\[
F(a)=\int_{1}^{\infty}\frac{e^{x}}{x^{a}}\,dx,
\]

你想知道答案如何依赖参数 \(a\)。

---

> **（本讲义 PDF 后续）** notes 自第 4 页起转入 **Arc Length**（弧长）与 **Parametric Equations**（参数方程），含 Figure 1–8（\(ds\) 无穷小、放大直角三角形、曲线段 \(P_{0}P_{1}\)、单位圆、圆弧、弧度、圆／椭圆参数曲线等）。该段属下一话题；Bilibili P27／本文件不转写、不裁图。详见同目录 README 与 [`MIT1801_L27_课上思路.md`](./MIT1801_L27_课上思路.md) §6。
