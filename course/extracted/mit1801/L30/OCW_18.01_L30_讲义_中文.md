# MIT OCW 18.01 Exam 4 Review 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L30_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P30**（30-考前复习：极坐标积分）对齐。对应的官方 PDF 为 Fall 2006 **`exam4_review.pdf`（Exam 4 Review）**；本仓库 **`lec33.pdf` 与其 MD5 相同（别名）**。OCW **Video gallery** 将本课标为 **Lecture 33 = Exam 4 Review**；资源目录 Ses #32 挂有 `exam4_review.pdf`，Ses #33 日历为 Exam 4 本身（No Lecture Notes）。PDF **页眉自印 “Lecture 32: Exam 4 Review”**。日历 **Lecture 8 / 17 / 27**＝Exam 1–3 空桩，故对 \(n\ge27\) 有 **P30 ↔ OCW Lecture 33**（Pn ≈ lec\((n+3)\)）。课堂口播（先补极坐标面积／玫瑰／焦双曲线／开普勒，再答疑 Exam 4）与讲义（清单 + Handout + 有理函数 Postscript）的差异见同目录 [`MIT1801_L30_课上思路.md`](./MIT1801_L30_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/exam4_review.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。**本 PDF 为纯文字／公式复习单，无插图**（`ocw_figs/` 为空；页渲染见 `ocw_pages/page-1.png`…`page-7.png`＝封面 + notes pp.1–6）。**本文件转写 `exam4_review.pdf` 全文。**

---

## Lecture 33: Exam 4 Review

（第 33 讲：第四次考试复习｜PDF 页眉写作 Lecture 32）

18.01 Fall 2006

---

### Exam 4 Review（考试范围提纲）

1. 三角代换与三角积分（Trig substitution and trig integrals）。
2. 部分分式（Partial fractions）。
3. 分部积分（Integration by parts）。
4. 弧长与旋转体表面积（Arc length and surface area of revolution）。
5. 极坐标（Polar coordinates）。
6. 极坐标下的面积（Area in polar coordinates）。

---

### Questions from the Students（课堂上的学生提问摘录）

#### Q: 关于参数方程我们需要知道什么？

**A:** 只需牢记公式

\[
ds=\sqrt{\Bigl(\frac{dx}{dt}\Bigr)^{2}+\Bigl(\frac{dy}{dt}\Bigr)^{2}}\,dt.
\]

**例：** 给定 \(x(t)=t^{4}\)、\(y(t)=1+t\)，求弧长元／弧长。

\[
ds=\sqrt{(4t^{3})^{2}+(1)^{2}}\,dt,
\]

再对 \(t\) 积分。

#### Q: 能否快速复习部分分式？

**A:** 做部分分式时，先检查分子次数是否 **≥** 分母次数。若是，须先做**多项式长除**；若否，再拆成部分分式。

**例：**

\[
\frac{x^{2}+x+1}{(x-1)^{2}(x+2)}.
\]

已知解的形式为

\[
\frac{x^{2}+x+1}{(x-1)^{2}(x+2)}
=\frac{A}{x-1}+\frac{B}{(x-1)^{2}}+\frac{C}{x+2}.
\]

有两个系数容易求：\(B\) 与 \(C\)，可用**覆盖法（cover-up method）**。

求 \(B\)（令 \(x\to 1\)）：

\[
B=\frac{1^{2}+1+1}{1+2}=\frac{3}{3}=1.
\]

求 \(C\)（令 \(x\to -2\)）：

\[
C=\frac{(-2)^{2}-2+1}{(-2-1)^{2}}=\frac{1}{3}.
\]

求 \(A\)：可代入除已用过的 \(x=1,-2\) 以外最方便的值，通常取 \(x=0\)：

\[
\frac{1}{(-1)^{2}\cdot 2}
=\frac{A}{-1}+\frac{1}{(-1)^{2}}+\frac{1/3}{2},
\]

再解出 \(A\)。

> 课堂上分发的 Review Sheet 见下一页。

---

### Exam 4 Review Handout（Exam 4 复习讲义）

1. **用三角代换积分**；算出三角积分后，借助直角三角形求 \(\mathrm{trig}(\mathrm{trig}^{-1})\)，回到原变量：
   - a) \(a^{2}-x^{2}\)：用 \(x=a\sin u\)，\(dx=a\cos u\,du\)。
   - b) \(a^{2}+x^{2}\)：用 \(x=a\tan u\)，\(dx=a\sec^{2}u\,du\)。
   - c) \(x^{2}-a^{2}\)：用 \(x=a\sec u\)，\(dx=a\sec u\tan u\,du\)。

2. **用部分分式积分有理函数 \(P/Q\)（多项式之比）**：若 \(\deg P<\deg Q\)，则把 \(Q\) 完全分解为一次与二次因子，并把 \(P/Q\) 写成更简单项之和。例如

\[
\frac{3x^{2}+1}{(x-1)(x+2)^{2}(x^{2}+9)}
=\frac{A}{x-1}+\frac{B_{1}}{x+2}+\frac{B_{2}}{(x+2)^{2}}+\frac{Cx+D}{x^{2}+9}.
\]

形如 \(D/(x^{2}+9)\) 的项可用三角代换 \(x=3\tan u\) 积分。  
此法原则上可积任意有理函数；实践中最难的往往是**分解分母**。习题课上还遇到系统覆盖所有情形所需的另两步：**配平方**¹与**长除**²。

3. **分部积分：**

\[
\int_{a}^{b} uv'\,dx=\Bigl[uv\Bigr]_{a}^{b}-\int_{a}^{b} u'v\,dx.
\]

当 \(u'v\) 比 \(uv'\) 更简单时使用。（若 \(u'\) 比 \(u\) 更简单，常属此类。）

4. **弧长：** \(ds=\sqrt{dx^{2}+dy^{2}}\)。按你想对 \(x\)、\(t\) 或 \(y\) 积分，写成

\[
\begin{aligned}
ds&=\sqrt{1+(dy/dx)^{2}}\,dx,\\
ds&=\sqrt{(dx/dt)^{2}+(dy/dt)^{2}}\,dt,\\
ds&=\sqrt{(dx/dy)^{2}+1}\,dy.
\end{aligned}
\]

5. **旋转体表面积：**
   - a) 绕 \(x\) 轴：\(2\pi y\,ds=2\pi y\sqrt{1+(dy/dx)^{2}}\,dx\)（需要 \(y=y(x)\)）。
   - b) 绕 \(y\) 轴：\(2\pi x\,ds=2\pi x\sqrt{(dx/dy)^{2}+1}\,dy\)（需要 \(x=x(y)\)）。

6. **极坐标：** \(x=r\cos\theta\)，\(y=r\sin\theta\)（较少用 \(r=\sqrt{x^{2}+y^{2}}\)，\(\theta=\tan^{-1}(y/x)\)）。
   - a) 由 \((x,y)\) 方程代入求曲线的极坐标方程。
   - b) 由极坐标方程作图，并弄清 \(\theta\) 的范围（常为积分做准备）。

7. **极坐标下的面积：**

\[
\int_{\theta_1}^{\theta_2}\frac12 r^{2}\,d\theta.
\]

（注意 \(\theta\) 的范围，以免重复计算或漏掉区域。）

---

¹ 例如把分母改写为 \(x^{2}+4x+13=(x+2)^{2}+9=u^{2}+a^{2}\)，其中 \(u=x+2\)，\(a=3\)。

² 当 \(\deg P\ge\deg Q\) 时用长除：\(P(x)/Q(x)=P_{1}(x)+R(x)/Q(x)\)，其中 \(P_{1}\) 为商多项式（易积），\(R\) 为余式。关键是 \(\deg R<\deg Q\)，从而 \(R/Q\) 可拆成部分分式。

---

### 下列公式将印在 Exam 4 试卷上

\[
\begin{aligned}
\sin^{2}x+\cos^{2}x&=1,&
\sec^{2}x&=\tan^{2}x+1,\\
\sin^{2}x&=\tfrac12-\tfrac12\cos 2x,&
\cos^{2}x&=\tfrac12+\tfrac12\cos 2x,\\
\cos 2x&=\cos^{2}x-\sin^{2}x,&
\sin 2x&=2\sin x\cos x.
\end{aligned}
\]

\[
\begin{aligned}
\frac{d}{dx}\tan x&=\sec^{2}x,&
\frac{d}{dx}\sec x&=\sec x\tan x,\\
\frac{d}{dx}\tan^{-1}x&=\frac{1}{1+x^{2}},&
\frac{d}{dx}\sin^{-1}x&=\frac{1}{\sqrt{1-x^{2}}}.
\end{aligned}
\]

\[
\int\tan x\,dx=-\ln(\cos x)+c,\qquad
\int\sec x\,dx=\ln(\sec x+\tan x)+c.
\]

> 下一页为有理函数积分的系统复习。

---

### Postscript: Systematic integration of rational functions  
（附言：有理函数的系统积分法）

对一般有理函数 \(P/Q\)，第一步是把它写成**一个多项式**加上**分子次数低于分母**的真分式之和。

例如

\[
\frac{x^{3}}{x^{2}-2x+1}=x+2+\frac{3x-2}{x^{2}-2x+1}.
\]

（做此次长除时**不要**分解分母 \(Q(x)=x^{2}-2x+1\)，原样留下即可。）商 \(x+2\) 是多项式，易积。余项

\[
\frac{3x-2}{(x-1)^{2}}
\]

的分子次数 1 低于分母次数 2，故有部分分式分解。事实上

\[
\frac{3x-2}{(x-1)^{2}}
=\frac{(3x-3)+1}{(x-1)^{2}}
=\frac{3}{x-1}+\frac{1}{(x-1)^{2}}.
\]

一般地，若 \(\deg P=n\)、\(\deg Q=m\)，长除给出

\[
\frac{P(x)}{Q(x)}=P_{1}(x)+\frac{R(x)}{Q(x)},
\]

其中商 \(P_{1}\) 次数为 \(n-m\)，余式 \(R\) 次数至多为 \(m-1\)。

#### 求「简单」碎块的积分

\[
\int\frac{dx}{(x-a)^{n}}
=\frac{-1}{n-1}(x-a)^{1-n}+c
\quad(n\neq 1);
\]

若 \(n=1\)，则为 \(\ln|x-a|+c\)。另一方面，形如

\[
\int\frac{x\,dx}{(Ax^{2}+Bx+C)^{n}}
\quad\text{与}\quad
\int\frac{dx}{(Ax^{2}+Bx+C)^{n}}
\]

的项先**配平方**：

\[
Ax^{2}+Bx+C=A\Bigl(x-\frac{B}{2A}\Bigr)^{2}+\Bigl(C-\frac{B^{2}}{4A}\Bigr).
\]

再用变量 \(u=\sqrt{A}\,(x-B/(2A))\)，化为

\[
\int\frac{u\,du}{(u^{2}+k^{2})^{n}}
\quad\text{与}\quad
\int\frac{du}{(u^{2}+k^{2})^{n}}
\]

的组合。前者用 \(w=u^{2}+k^{2}\)，\(dw=2u\,du\)；后者用三角代换 \(u=k\tan\theta\)，\(du=k\sec^{2}\theta\,d\theta\)，导向 \(\sec\)-\(\tan\) 积分；\(n\) 较大时实际计算很长。

还有本讲未系统覆盖的其它情形。示例如下：

1. 若 \(Q(x)=(x-a)^{m}(x-b)^{n}\)，则分解式为

\[
\frac{A_{1}}{x-a}+\frac{A_{2}}{(x-a)^{2}}+\cdots+\frac{A_{m}}{(x-a)^{m}}
+\frac{B_{1}}{x-b}+\frac{B_{2}}{(x-b)^{2}}+\cdots+\frac{B_{n}}{(x-b)^{n}}.
\]

2. 若有二次因子如 \((Ax^{2}+Bx+C)^{p}\)，则对每个这样的因子得到项

\[
\frac{a_{1}x+b_{1}}{Ax^{2}+Bx+C}
+\frac{a_{2}x+b_{2}}{(Ax^{2}+Bx+C)^{2}}
+\cdots
+\frac{a_{p}x+b_{p}}{(Ax^{2}+Bx+C)^{p}}.
\]

（积分这些二次碎块时：配平方并做三角代换。）

> **注（排版）：** 源 PDF 第二项分子曾印成 \(a_{2}x+b_{2}x\)；按标准模板应为 \(a_{2}x+b_{2}\)，上式已按惯例更正。
