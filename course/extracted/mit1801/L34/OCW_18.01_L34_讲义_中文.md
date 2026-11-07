# MIT OCW 18.01 Lecture 37 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L34_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P34**（34-泰勒级数）对齐。对应的官方 PDF 实为 Fall 2006 **`lec37.pdf`（Lecture 37: Taylor Series）**。日历 **Lecture 8 / 17 / 27**＝Exam 1–3 空桩；**Ses #34 = Exam 4**（无本系列课堂录像），故 OCW **Video gallery** 常把同一堂课标为 **Lecture 38: Taylor's Series**。对 \(n\ge27\) 有 **P34 ↔ OCW Lecture 37**（Pn ≈ lec\((n+3)\)；视频编号可能显示 38）。课堂口播（先收尾积木悬伸再入幂级数／Taylor；现场 \(S-xS\) 与 Q&A；未展开讲义中的代换诸例、\(\ln/\arctan\)、二项式、基点 \(b\neq0\)）与讲义的差异见同目录 [`MIT1801_L34_课上思路.md`](./MIT1801_L34_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec37.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。**`lec37.pdf` 通篇为方程与文字，无单独插图**；故本目录 `ocw_figs/` 为空（不发明图、不复用 P33 积木图）。**本文件转写 `lec37.pdf` 全文。**

---

## Lecture 37: Taylor Series

（第 37 讲：泰勒级数）

18.01 Fall 2006

---

## General Power Series（一般幂级数）

**What is \(\cos x\) anyway?**（\(\cos x\) 究竟是什么？）

### Recall: geometric series.（回忆：几何级数）

\[
1 + a + a^{2} + \cdots = \frac{1}{1-a}
\quad\text{当 }|a|<1.
\]

### General power series.（一般幂级数）

一般幂级数是无穷和：

\[
f(x) = a_0 + a_1 x + a_2 x^{2} + a_3 x^{3} + \cdots
\]

当 \(|x|<R\) 时它表示 \(f\)，其中 \(R=\) **收敛半径（radius of convergence）**。这意味着：若 \(|x|<R\)，则当 \(n\to\infty\) 时 \(|a_n x^{n}|\to 0\)（「几何式地」）。另一方面，若 \(|x|>R\)，则 \(|a_n x^{n}|\) **不**趋于 0。例如在几何级数中，若 \(|a|=1/2\)，则 \(|a^{n}|=1/2^{n}\)。由于 \(|a|<1\) 时高阶项越来越小，级数的「尾巴」可忽略。

### Example 1.

若 \(a=-1\)，则 \(|a^{n}|=1\) 不趋于 0。

\[
1 - 1 + 1 - 1 + \cdots
\]

和在 0 与 1 之间来回跳，因此不趋于定值。在区间 \(-1<a<1\) **之外**，该级数发散。

---

## Basic Tools（基本工具）

在收敛半径内部，**多项式的运算法则适用于级数**。

### Substitution/Algebra.（代换／代数）

\[
\frac{1}{1-x} = 1 + x + x^{2} + \cdots.
\]

### Example 2. \(x=-u\).

\[
\frac{1}{1+u} = 1 - u + u^{2} - u^{3} + \cdots.
\]

### Example 3. \(x=-v^{2}\).

\[
\frac{1}{1+v^{2}} = 1 - v^{2} + v^{4} - v^{6} + \cdots.
\]

### Example 4.

\[
\Bigl(\frac{1}{1-x}\Bigr)\Bigl(\frac{1}{1-x}\Bigr)
=(1+x+x^{2}+\cdots)(1+x+x^{2}+\cdots).
\]

逐项相乘得：

\[
1 + 2x + 3x^{2} + \cdots
=\frac{1}{(1-x)^{2}}.
\]

记住，这里的 \(x\) 是像 \(1/2\) 这样的数。取 \(x\) 的越来越高的幂，结果越来越小。

### Differentiation (term by term).（逐项求导）

\[
\frac{d}{dx}\Bigl(\frac{1}{1-x}\Bigr)
=\frac{d}{dx}\bigl(1+x+x^{2}+x^{3}+\cdots\bigr)
\]

\[
\frac{1}{(1-x)^{2}}
=0+1+2x+3x^{2}+\cdots
\]

（其中 1 是 \(a_0\) 意义下的常数项导数后余下的首项系数关系；与 Example 4 同答，但用了新方法。）

### Integration (term by term).（逐项积分）

若

\[
f(x)=a_0+a_1 x+a_2 x^{2}+\cdots,
\]

则

\[
\int f(x)\,dx
=c+a_0 x+\frac{a_1}{2}x^{2}+\frac{a_2}{3}x^{3}+\cdots.
\]

### Example 5. \(\displaystyle\int\frac{du}{1+u}\)

由

\[
\frac{1}{1+u}=1-u+u^{2}-u^{3}+\cdots
\]

得

\[
\int\frac{du}{1+u}
=c+u-\frac{u^{2}}{2}+\frac{u^{3}}{3}-\frac{u^{4}}{4}+\cdots.
\]

取定积分从 0 到 \(x\)：

\[
\ln(1+x)
=\int_{0}^{x}\frac{du}{1+u}
=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots.
\]

于是我们得到了 \(\ln(1+x)\) 的级数展开。

### Example 6. Integrate Example 3.

\[
\frac{1}{1+v^{2}}=1-v^{2}+v^{4}-v^{6}+\cdots
\]

\[
\int\frac{dv}{1+v^{2}}
=c+v-\frac{v^{3}}{3}+\frac{v^{5}}{5}-\frac{v^{7}}{7}+\cdots.
\]

\[
\tan^{-1}x
=\int_{0}^{x}\frac{dv}{1+v^{2}}
=x-\frac{x^{3}}{3}+\frac{x^{5}}{5}-\frac{x^{7}}{7}+\cdots.
\]

---

## Taylor's Series and Taylor's Formula（泰勒级数与泰勒公式）

若 \(f(x)=a_0+a_1 x+a_2 x^{2}+\cdots\)，我们想弄清所有这些系数是什么。求导：

\[
\begin{aligned}
f'(x)&=a_1+2a_2 x+3a_3 x^{2}+\cdots,\\
f''(x)&=(2)(1)a_2+(3)(2)a_3 x+(4)(3)a_4 x^{2}+\cdots,\\
f'''(x)&=(3)(2)(1)a_3+(4)(3)(2)a_4 x+\cdots.
\end{aligned}
\]

把 \(x=0\) 代入以上各式：

\[
f(0)=a_0;\quad
f'(0)=a_1;\quad
f''(0)=2a_2;\quad
f'''(0)=(3!)a_3.
\]

**Taylor 公式**告诉我们系数是什么：

\[
f^{(n)}(0)=(n!)\,a_n.
\]

记住 \(n!=n(n-1)(n-2)\cdots(2)(1)\)，且 \(0!=1\)。系数 \(a_n\) 由

\[
a_n=\frac{1}{n!}\,f^{(n)}(0)
\]

给出。

### Example 7. \(f(x)=e^{x}\).

\[
\begin{aligned}
f'(x)&=e^{x},\\
f''(x)&=e^{x},\\
f^{(n)}(x)&=e^{x},\\
f^{(n)}(0)&=e^{0}=1.
\end{aligned}
\]

因此由 Taylor 公式 \(a_n=1/n!\)，且

\[
e^{x}
=\frac{1}{0!}+\frac{1}{1!}x+\frac{1}{2!}x^{2}+\frac{1}{3!}x^{3}+\cdots
=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}.
\]

现在可以把 \(e\) 算到任意精度：

\[
e=1+1+\frac{1}{2}+\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\cdots.
\]

### Example 7（续）. \(f(x)=\cos x\).

\[
\begin{aligned}
f'(x)&=-\sin x,\\
f''(x)&=-\cos x,\\
f'''(x)&=\sin x,\\
f^{(4)}(x)&=\cos x.
\end{aligned}
\]

\[
\begin{aligned}
f(0)&=\cos0=1,\\
f'(0)&=-\sin0=0,\\
f''(0)&=-\cos0=-1,\\
f'''(0)&=\sin0=0.
\end{aligned}
\]

只有偶次系数非零，且符号交替。因此

\[
\cos x
=1-\frac{1}{2}x^{2}+\frac{1}{4!}x^{4}-\frac{1}{6!}x^{6}+\frac{1}{8!}x^{8}+\cdots.
\]

注意：\(\cos x\) 是偶函数；该幂级数亦然——它只含 \(x\) 的偶次幂。

求 \(\sin x\) 的 Taylor 级数有两种办法：对 \(\cos x\) 求导，或直接用 Taylor 公式。我们取导数：

\[
\frac{d}{dx}\cos x
=0-2\cdot\frac{1}{2}x+\frac{4}{4!}x^{3}-\frac{6}{6!}x^{5}+\frac{8}{8!}x^{7}+\cdots
\]

\[
=-\sin x
=-x+\frac{x^{3}}{3!}-\frac{x^{5}}{5!}+\frac{x^{7}}{7!}+\cdots,
\]

故

\[
\sin x
=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\cdots.
\]

与学期早些时候的二次近似对照：

\[
\cos x\approx 1-\frac12 x^{2},\qquad
\sin x\approx x.
\]

也可写成：

\[
\cos x
=\sum_{k=0}^{\infty}(-1)^{k}\frac{x^{2k}}{(2k)!}
=(-1)^{0}\frac{x^{0}}{0!}+(-1)^{1}\frac{x^{2}}{2!}+\cdots
=1-\frac12 x^{2}+\cdots,
\]

\[
\sin x
=\sum_{k=0}^{\infty}(-1)^{k}\frac{x^{2k+1}}{(2k+1)!}
\quad(\text{令 }n=2k+1).
\]

### Example 8: Binomial Expansion.（二项式展开）\(f(x)=(1+x)^{a}\)

\[
(1+x)^{a}
=1+\frac{a}{1}x+\frac{a(a-1)}{2!}x^{2}+\frac{a(a-1)(a-2)}{3!}x^{3}+\cdots.
\]

---

## Taylor Series with Another Base Point（另一基点的泰勒级数）

基点在 \(b\)（而非 0）处的 Taylor 级数形如：

\[
f(x)
=f(b)+f'(b)(x-b)+\frac{f''(b)}{2}(x-b)^{2}+\frac{f^{(3)}(b)}{3!}(x-b)^{3}+\cdots.
\]

（讲义英文导语偶写 “base point at \(a\)”，随后公式一律用 \(b\)；此处统一为 \(b\)。）

\(\sqrt{x}\) 的 Taylor 级数：用 \(b=0\) 展开是坏主意，因为 \(\sqrt{x}\) 在 \(x=0\) 不可微。改用 \(b=1\)：

\[
x^{1/2}
=1+\frac12(x-1)+\frac{\bigl(\tfrac12\bigr)\bigl(\tfrac12-1\bigr)}{2!}(x-1)^{2}+\cdots.
\]
