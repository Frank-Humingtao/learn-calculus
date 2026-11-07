# MIT OCW 18.01 Lecture 38 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L35_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P35**（35-期末复习：幂级数与泰勒；合集最后一讲）对齐。对应的官方 PDF 实为 Fall 2006 **`lec38.pdf`（Lecture 38: Final Review）**。日历 **Lecture 8 / 17 / 27**＝Exam 1–3 空桩；**Ses #34 = Exam 4**（无本系列课堂录像），故 OCW **Video gallery** 常把同一堂课标为 **Lecture 39: Final Review**。对 \(n\ge27\) 有 **P35 ↔ OCW Lecture 38**（Pn ≈ lec\((n+3)\)；视频编号可能显示 39）。课堂口播（代课讲师；幂级数回顾＋\(e^x,1/(1+x),\sin,\cos,\ln,e^{-t^2},\operatorname{erf}\)；大量 Q&A；末推 18.02）与讲义的差异见同目录 [`MIT1801_L35_课上思路.md`](./MIT1801_L35_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec38.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。**`lec38.pdf` 通篇为方程与文字，无单独插图**；故本目录 `ocw_figs/` 为空（不发明图）。**本文件转写 `lec38.pdf` 全文。**

---

## Lecture 38: Final Review

（第 38 讲：期末复习）

18.01 Fall 2006

---

## Review: Differentiating and Integrating Series（复习：级数的求导与积分）

若

\[
f(x)=\sum_{n=0}^{\infty}a_n x^{n},
\]

则

\[
f'(x)=\sum_{n=1}^{\infty}n a_n x^{n-1},
\qquad
\int f(x)\,dx
=C+\sum_{n=0}^{\infty}\frac{a_n x^{n+1}}{n+1}.
\]

---

## Example 1: Normal (or Gaussian) Distribution.（例 1：正态／高斯分布）

\[
\begin{aligned}
\int_{0}^{x}e^{-t^{2}}\,dt
&=\int_{0}^{x}\Bigl(1-t^{2}+\frac{(-t^{2})^{2}}{2!}+\frac{(-t^{2})^{3}}{3!}+\cdots\Bigr)dt\\
&=\int_{0}^{x}\Bigl(1-t^{2}+\frac{t^{4}}{2!}-\frac{t^{6}}{3!}+\frac{t^{8}}{4!}-\cdots\Bigr)dt\\
&=x-\frac{x^{3}}{3}+\frac{1}{2!}\frac{x^{5}}{5}-\frac{1}{3!}\frac{x^{7}}{7}+\cdots.
\end{aligned}
\]

尽管 \(\int_{0}^{x}e^{-t^{2}}\,dt\) **不是**初等函数，我们仍可计算它。不过初等函数还是稍微方便一点。例如：

\[
\sin x=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\cdots
\implies
\sin\frac{\pi}{2}
=\frac{\pi}{2}-\frac{(\pi/2)^{3}}{3!}+\frac{(\pi/2)^{5}}{5!}-\cdots.
\]

但用数值办法去算 \(\sin(\pi/2)\) 是浪费时间——我们知道这个和就是很简单的东西，即

\[
\sin\frac{\pi}{2}=1.
\]

从级数展开式本身，完全看不出 \(\sin x\) 与角度有关。级数有时又复杂又反直觉。

尽管如此，我们仍可以把公式**反过来读**，得到 \(\pi/2\) 的一个公式。从 \(\sin(\pi/2)=1\) 出发，有

\[
\int_{0}^{1}\frac{dx}{\sqrt{1-x^{2}}}
=\sin^{-1}x\Big|_{0}^{1}
=\sin^{-1}1-\sin^{-1}0
=\frac{\pi}{2}-0=\frac{\pi}{2}.
\]

我们想找 \((1-x^{2})^{-1/2}\) 的级数，但先处理更简单的情形：

\[
\begin{aligned}
(1+u)^{-1/2}
&=1+\Bigl(-\frac12\Bigr)u
+\frac{\bigl(-\tfrac12\bigr)\bigl(-\tfrac12-1\bigr)}{1\cdot2}u^{2}
+\frac{\bigl(-\tfrac12\bigr)\bigl(-\tfrac12-1\bigr)\bigl(-\tfrac12-2\bigr)}{1\cdot2\cdot3}u^{3}
+\cdots\\
&=1-\frac12 u+\frac{1\cdot3}{2\cdot4}u^{2}-\frac{1\cdot3\cdot5}{2\cdot4\cdot6}u^{3}+\cdots.
\end{aligned}
\]

注意规律：分子是奇数，分母是偶数，符号交替。

---

## 续：\(u=-x^{2}\) 与 \(\pi/2\) 级数

现在令 \(u=-x^{2}\)：

\[
(1-x^{2})^{-1/2}
=1+\frac12 x^{2}+\frac{1\cdot3}{2\cdot4}x^{4}+\frac{1\cdot3\cdot5}{2\cdot4\cdot6}x^{6}+\cdots.
\]

\[
\int(1-x^{2})^{-1/2}\,dx
=C+\Biggl(x+\frac12\frac{x^{3}}{3}+\frac{1\cdot3}{2\cdot4}\frac{x^{5}}{5}+\frac{1\cdot3\cdot5}{2\cdot4\cdot6}\frac{x^{7}}{7}+\cdots\Biggr).
\]

\[
\frac{\pi}{2}
=\int_{0}^{1}(1-x^{2})^{-1/2}\,dx
=1+\frac12\cdot\frac13+\frac{1\cdot3}{2\cdot4}\cdot\frac15+\frac{1\cdot3\cdot5}{2\cdot4\cdot6}\cdot\frac17+\cdots.
\]

这里有一道较难的（可选）附加题：这个级数为什么收敛？提示：用洛必达法则看清各项衰减有多快。

---

## The Final Exam（期末考试相关）

再一次尝试澄清**加权平均**的概念。

### Weighted Average（加权平均）

函数 \(f\) 的加权平均定义为

\[
\operatorname{Average}(f)
=\frac{\displaystyle\int_{a}^{b}w(x)f(x)\,dx}{\displaystyle\int_{a}^{b}w(x)\,dx}.
\]

这里 \(\int_{a}^{b}w(x)\,dx\) 是总量，\(w(x)\) 是权重函数。

### Example：取自往年习题

若某粒子在 \(t\) 秒内衰变，你得到 \(\$t\)。你该付多少钱来玩这个游戏？已知粒子尚未衰变的可能性（权重函数）为

\[
w(x)=e^{-kt}.
\]

记住

\[
\int_{0}^{\infty}e^{-kt}\,dt=\frac{1}{k}.
\]

收益函数是 \(f(t)=t\)。期望（平均）收益为

\[
\frac{\displaystyle\int_{0}^{\infty}f(t)w(t)\,dt}{\displaystyle\int_{0}^{\infty}w(t)\,dt}
=\frac{\displaystyle\int_{0}^{\infty}t e^{-kt}\,dt}{\displaystyle\int_{0}^{\infty}e^{-kt}\,dt}
=k\int_{0}^{\infty}t e^{-kt}\,dt
=\int_{0}^{\infty}(kt)e^{-kt}\,dt.
\]

做换元：\(u=kt\)，\(du=k\,dt\)。于是

\[
\operatorname{Average}
=\int_{0}^{\infty}u e^{-u}\,\frac{du}{k}.
\]

在先前习题中已用分部积分算过 \(\int_{0}^{\infty}u e^{-u}\,du=1\)。因此

\[
\operatorname{Average}
=\int_{0}^{\infty}u e^{-u}\,\frac{du}{k}
=\frac{1}{k}.
\]

习题中算出钋-210（Polonium-210；PDF 原文排版作 “Polonium120”）的半衰期 \(H=(131)(24)(60)^{2}\) 秒，且

\[
k=\frac{\ln 2}{H}.
\]

故期望收益为

\[
\frac{1}{k}=\frac{H}{\ln 2},
\]

其中 \(H\) 是粒子半衰期（秒）。

你们大概在想：谁会拿粒子衰变来打赌？

事实上没人这么干。但有一个非常类似、在现实中有用的问题：**年金（annuity）**，本质上是退休金。你可以买一份年金，退休后每月领取定额；去世后给付停止。

你（以及付钱的一方）自然关心退休期间能期望拿到多少钱。此时 \(f(t)=t\) 表示最终到手的钱，\(w(t)=e^{-kt}\) 表示你在 \(t\) 年后仍在世的可能性。

若要双人年金（2-life annuity）？那就需要重积分——将在多元微积分（**18.02**）中学习。

本课的第一个目标是能对任何东西求导。在多元微积分里，你会学到另一个链式法则。那个链式法则会把（单变量）链式法则、积法则、商法则以及隐函数求导统一起来。

你或许可以说，多元链式法则是：

> One thing to rule them all  
> One thing to find them  
> One thing to bring them all  
> And in a matrix bind them.  
>
> （with apologies to JRR Tolkien）.

（一物以统御万物／一物以寻获万物／一物以召集万物／并在矩阵中束缚它们。——向 J. R. R. Tolkien 致歉。）
