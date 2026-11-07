# MIT OCW 18.01 Lecture 34 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L31_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P31**（31-洛必达法则）对齐。对应的官方 PDF 实为 Fall 2006 **`lec34.pdf`（Lecture 34: Indeterminate Forms – L'Hôpital's Rule）**。日历 **Lecture 8 / 17 / 27**＝Exam 1–3 空桩；**Ses #34 = Exam 4**（无本系列课堂录像），故 OCW **Video gallery** 常把同一堂课标为 **Lecture 35: Indeterminate Forms**。对 \(n\ge27\) 有 **P31 ↔ OCW Lecture 34**（Pn ≈ lec\((n+3)\)；视频编号可能显示 35）。课堂口播（例题幂次／三角组合与讲义不尽相同；另有 Q&A、「勿当拐杖」）与讲义的差异见同目录 [`MIT1801_L31_课上思路.md`](./MIT1801_L31_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec34.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。**本 PDF 为纯文字／公式讲义，无插图**（`ocw_figs/` 为空；页渲染见 `ocw_pages/page-1.png`…`page-5.png`＝封面 + notes pp.1–4）。**本文件转写 `lec34.pdf` 全文。**

---

## Lecture 34: Indeterminate Forms - L'Hôpital's Rule

（第 34 讲：不定式——洛必达法则）

18.01 Fall 2006

---

### L'Hôpital's Rule（洛必达法则）

（两种正确拼写：“L'Hôpital” 与 “L'Hospital”）

有时我们会遇到**不定式（indeterminate forms）**。例如

\[
\frac{0}{0}
\qquad\text{与}\qquad
\frac{\infty}{\infty}.
\]

比方说，如何处理下面这个极限？

\[
\lim_{x\to 1}\frac{x^{3}-1}{x^{2}-1}=\frac{0}{0}\;??
\]

---

### Example 0.

处理办法之一是用**代数化简**：

\[
\lim_{x\to 1}\frac{x^{3}-1}{x^{2}-1}
=\lim_{x\to 1}\frac{(x-1)(x^{2}+x+1)}{(x-1)(x+1)}
=\lim_{x\to 1}\frac{x^{2}+x+1}{x+1}
=\frac{3}{2}.
\]

一般地，当 \(f(a)=g(a)=0\) 时，

\[
\lim_{x\to a}\frac{f(x)}{g(x)}
=\lim_{x\to a}\frac{\dfrac{f(x)-f(a)}{x-a}}{\dfrac{g(x)-g(a)}{x-a}}
=\frac{\displaystyle\lim_{x\to a}\dfrac{f(x)-f(a)}{x-a}}{\displaystyle\lim_{x\to a}\dfrac{g(x)-g(a)}{x-a}}
=\frac{f'(a)}{g'(a)}.
\]

这就是洛必达法则的**易版本（easy version）**：

\[
\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{f'(a)}{g'(a)}.
\]

**注意**：仅当 \(g'(a)\neq 0\) 时成立！

在 Example 0 中，

\[
f(x)=x^{3}-1,\quad g(x)=x^{2}-1,
\]

\[
f'(x)=3x^{2},\quad g'(x)=2x
\implies f'(1)=3,\; g'(1)=2.
\]

极限为 \(f'(1)/g'(1)=3/2\)。下面进入**完整的洛必达法则**。

---

### Example 1.

对

\[
\lim_{x\to 1}\frac{x^{15}-1}{x^{3}-1}
\]

应用洛必达法则（简称 “L'Hop”）得

\[
\lim_{x\to 1}\frac{x^{15}-1}{x^{3}-1}
=\lim_{x\to 1}\frac{15x^{14}}{3x^{2}}
=\frac{15}{3}=5.
\]

与用**线性近似**代替洛必达所得结果比较：

\[
x^{15}-1\approx 15(x-1)
\]

（此处 \(f(x)=x^{15}-1\)，\(a=1\)，\(f(a)=b=0\)，\(m=f'(1)=15\)，且 \(f(x)\approx m(x-a)+b\)。）同理

\[
x^{3}-1\approx 3(x-1).
\]

因此

\[
\frac{x^{15}-1}{x^{3}-1}\approx\frac{15(x-1)}{3(x-1)}=5.
\]

---

### Example 2.

对

\[
\lim_{x\to 0}\frac{\sin 3x}{x}
\]

应用 L'Hop 得

\[
\lim_{x\to 0}\frac{3\cos 3x}{1}=3.
\]

这与

\[
\left.\frac{d}{dx}\sin(3x)\right|_{x=0}
=\left.3\cos(3x)\right|_{x=0}=3
\]

相同。

---

### Example 3.

\[
\lim_{x\to\pi/4}\frac{\sin x-\cos x}{x-\pi/4}
=\lim_{x\to\pi/4}\frac{\cos x+\sin x}{1}
=\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}=\sqrt{2}.
\]

\[
f(x)=\sin x-\cos x,\quad f'(x)=\cos x+\sin x,
\qquad f'\Bigl(\frac{\pi}{4}\Bigr)=\sqrt{2}.
\]

**附注（Remark）**：导数

\[
\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x}
\]

**永远是** \(0/0\) 型极限。

---

### Example 4.

\[
\lim_{x\to 0}\frac{\cos x-1}{x}.
\]

用洛必达法则：

\[
\lim_{x\to 0}\frac{\cos x-1}{x}
=\lim_{x\to 0}\frac{-\sin x}{1}=0.
\]

---

### Example 5.

\[
\lim_{x\to 0}\frac{\cos x-1}{x^{2}}.
\]

\[
\lim_{x\to 0}\frac{\cos x-1}{x^{2}}
=\lim_{x\to 0}\frac{-\sin x}{2x}
=\lim_{x\to 0}\frac{-\cos x}{2}
=-\frac{1}{2}.
\]

与**二次近似**核对。记得当 \(x\approx 0\) 时

\[
\cos x\approx 1-\frac{1}{2}x^{2},
\]

于是

\[
\frac{\cos x-1}{x^{2}}
\approx\frac{\bigl(1-\tfrac12 x^{2}\bigr)-1}{x^{2}}
=\frac{-\tfrac12 x^{2}}{x^{2}}
=-\frac{1}{2}.
\]

---

### Example 6.

\[
\lim_{x\to 0}\frac{\sin x}{x^{2}}.
\]

由洛必达法则

\[
\lim_{x\to 0}\frac{\sin x}{x^{2}}
=\lim_{x\to 0}\frac{\cos x}{2x}.
\]

若再应用一次洛必达，会得到

\[
\lim_{x\to 0}\frac{-\sin x}{2}=0.
\]

但这与线性近似所得不一致：

\[
\frac{\sin x}{x^{2}}\approx\frac{x}{x^{2}}=\frac{1}{x}\to\infty
\quad(x\to 0^{+}).
\]

澄清这一表面上的悖论：注意

\[
\lim_{x\to 0}\frac{\cos x}{2x}=\frac{1}{0},
\]

该极限**不是** \(0/0\) 型，因而**不能**使用洛必达法则。要点是：**look before you L'Hôp!**（先看清再洛必达！）

---

### More “interesting” cases that work  
（更多「有趣」且适用的情形）

洛必达法则亦可用于 \(\infty/\infty\) 型，或 \(x\to\infty\)、\(x\to-\infty\)。下面用于**增长率**：\(x\)、\(e^{ax}\)、\(\ln x\) 谁更快趋于 \(\infty\)？

#### Example 7.

对 \(a>0\)，

\[
\lim_{x\to\infty}\frac{e^{ax}}{x}
=\lim_{x\to\infty}\frac{a e^{ax}}{1}=+\infty.
\]

故 \(e^{ax}\) 比 \(x\) 增长更快（\(a>0\)）。

#### Example 8.

\[
\lim_{x\to\infty}\frac{e^{ax}}{x^{10}}
\xrightarrow{\text{L'Hôpital}}
\lim_{x\to\infty}\frac{a e^{ax}}{10 x^{9}}
=\lim_{x\to\infty}\frac{a^{2} e^{ax}}{10\cdot 9\, x^{8}}
=\cdots
=\lim_{x\to\infty}\frac{a^{10} e^{ax}}{10!}=\infty.
\]

可以连用洛必达十次。但有更好的办法：

\[
\Bigl(\frac{e^{ax}}{x^{10}}\Bigr)^{1/10}=\frac{e^{ax/10}}{x},
\]

\[
\lim_{x\to\infty}\frac{e^{ax}}{x^{10}}
=\lim_{x\to\infty}\Bigl(\frac{e^{ax/10}}{x}\Bigr)^{10}
=\infty^{10}=\infty.
\]

#### Example 9.

\[
\lim_{x\to\infty}\frac{\ln x}{x^{1/3}}
=\lim_{x\to\infty}\frac{1/x}{\tfrac13 x^{-2/3}}
=\lim_{x\to\infty}3x^{-1/3}=0.
\]

综合前面诸例（\(x\to\infty\)，\(a>0\)）：

\[
\ln x\;\ll\; x^{1/3}\;\ll\; x\;\ll\; x^{10}\;\ll\; e^{ax}.
\]

---

### 其它不定式

洛必达法则直接适用于 \(0/0\) 与 \(\infty/\infty\)。但有时还会遇到其它不定极限，例如

\[
1^{\infty},\qquad 0^{0},\qquad 0\cdot\infty.
\]

用代数、指数与对数把它们改写成洛必达可用的形式。

#### Example 10. \(\displaystyle\lim_{x\to 0} x^{x}\)（\(x>0\)）

因为指数在变，用底数 \(e\)：

\[
\lim_{x\to 0} x^{x}=\lim_{x\to 0} e^{x\ln x}.
\]

先求指数的极限

\[
\lim_{x\to 0} x\ln x.
\]

这是 \(0\cdot\infty\) 型。我们希望改成 \(0/0\) 或 \(\infty/\infty\)。

尝试写成 \(0/0\)：

\[
\frac{x}{1/\ln x}.
\]

但我们不知道如何求 \(\lim_{x\to 0} 1/\ln x\)，故此路不有用。

改为 \(\infty/\infty\)：

\[
\frac{\ln x}{1/x}.
\]

用洛必达法则：

\[
\lim_{x\to 0} x\ln x
=\lim_{x\to 0}\frac{\ln x}{1/x}
=\lim_{x\to 0}\frac{1/x}{-1/x^{2}}
=\lim_{x\to 0}(-x)=0.
\]

因此

\[
\lim_{x\to 0} x^{x}
=\lim_{x\to 0} e^{x\ln x}
=e^{\lim_{x\to 0}(x\ln x)}
=e^{0}=1.
\]
