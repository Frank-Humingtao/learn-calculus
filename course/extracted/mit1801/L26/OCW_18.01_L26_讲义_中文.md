# MIT OCW 18.01 Lecture 29 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L26_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P26**（26-部分分式积分）对齐。对应的官方 PDF 实为 Fall 2006 **`lec29.pdf`（Lecture 29: Partial Fractions）**。OCW 课程日历中的 **Lecture 8** 是 Exam 1、**Lecture 17** 是 Exam 2、**Lecture 27** 是 Exam 3，**都没有**常规讲义 PDF / 本系列课堂录像（lec27 为空桩／Exam stub）；故对 \(n\ge16\) 有 Bilibili **P26 ↔ OCW Lecture 29**（Pn ≈ lec\((n+2)\)；跳过空的 lec27）。课堂口播（Jerison：遮盖法、重复／二次因子、假分数长除）与讲义的差异见同目录 [`MIT1801_L26_课上思路.md`](./MIT1801_L26_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec29.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。**本讲义 PDF 无插图**（`ocw_figs/` 为空；见该目录说明）。

---

## Lecture 29: Partial Fractions

（第 29 讲：部分分式）

18.01 Fall 2006

---

我们继续上一讲开始的**有理函数积分**讨论。有理函数定义为两多项式之比：

\[
\frac{P(x)}{Q(x)}.
\]

我们已经看过例子

\[
\int\Bigl(\frac{1}{x-1}+\frac{3}{x+2}\Bigr)dx=\ln|x-1|+3\ln|x+2|+c.
\]

同一问题可以伪装成：

\[
\frac{1}{x-1}+\frac{3}{x+2}
=\frac{(x+2)+3(x-1)}{(x-1)(x+2)}
=\frac{4x-1}{x^{2}+x-2},
\]

于是要积

\[
\int\frac{4x-1}{x^{2}+x-2}\,dx=\ ???
\]

**目标**：找出一种系统办法，把 \(\dfrac{P(x)}{Q(x)}\) **拆成更简单的块**。

首先，对分母 \(Q(x)\) 做因式分解：

\[
\frac{4x-1}{x^{2}+x-2}
=\frac{4x-1}{(x-1)(x+2)}
=\frac{A}{x-1}+\frac{B}{x+2}.
\]

---

### 慢法求 \(A,B\)

有一种慢法：两边同乘 \((x-1)(x+2)\) 清掉分母：

\[
4x-1=A(x+2)+B(x-1).
\]

由此得到

\[
4=A+B,\qquad -1=2A-B.
\]

再解这个二元一次方程组。若未知数有 3、4 个或更多，这种方法会非常耗时。

---

### 更快：遮盖法（cover-up method）

更快的办法称为 **「遮盖法」**。两边同乘 \((x-1)\)：

\[
\frac{4x-1}{x+2}=A+\frac{B}{x+2}(x-1).
\]

令 \(x=1\) 使 \(B\) 项消失：

\[
\frac{4-1}{1+2}=A\Longrightarrow A=1.
\]

最快的做法是在心里做，或在纸上把划掉的因子真正「遮住」。例如求 \(B\)：遮住分母中的 \((x+2)\)（并遮住右边 \(A\) 项里相应因子），隐含地乘以 \((x+2)\) 并令 \(x=-2\)：

\[
\frac{4(-2)-1}{-2-1}=B\Longrightarrow B=3.
\]

到目前为止，所述方法适用于：**\(Q(x)\) 完全分解为互不相同的线性因子，且 \(\deg P<\deg Q\)**。

---

### 重复因子

若 \(Q\) 的因子有重复，做法稍有不同。例如：

\[
\frac{x^{2}+2}{(x-1)^{2}(x+2)}
=\frac{A}{x-1}+\frac{B}{(x-1)^{2}}+\frac{C}{x+2}.
\]

对 \((x-1)\) 的**最高次**项用遮盖法：

\[
\frac{x^{2}+2}{x+2}=B+[\text{stuff}](x-1)
\quad\xrightarrow{x\to1}\quad
\frac{1^{2}+2}{1+2}=B\Longrightarrow B=1.
\]

（隐含：乘以 \((x-1)^{2}\)，再取 \(x\to1\) 的极限。）

\(C\) 也可用遮盖：令 \(x=-2\)，

\[
\frac{(-2)^{2}+2}{(-2-1)^{2}}=C\Longrightarrow C=\frac{2}{3}.
\]

于是

\[
\frac{x^{2}+2}{(x-1)^{2}(x+2)}
=\frac{A}{x-1}+\frac{1}{(x-1)^{2}}+\frac{2/3}{x+2}.
\]

\(A\) **不能**用遮盖求。改代一个好算的 \(x\)，例如 \(x=0\)：

\[
\frac{2}{(-1)^{2}\cdot2}
=\frac{A}{-1}+1+\frac{1}{3}
\Longrightarrow 1=1+\frac13-A
\Longrightarrow A=\frac13.
\]

完整答案：

\[
\frac{x^{2}+2}{(x-1)^{2}(x+2)}
=\frac{1}{3(x-1)}+\frac{1}{(x-1)^{2}}+\frac{2}{3(x+2)}.
\]

---

### 不可约二次因子

并非所有多项式都能完全分解为实线性因子（除非引入复数）。例如：

\[
\frac{1}{(x^{2}+1)(x-1)}
=\frac{A_{1}}{x-1}+\frac{B_{1}x+C_{1}}{x^{2}+1}.
\]

\(A_{1}\) 仍用遮盖：

\[
\frac{1}{1^{2}+1}=A_{1}\Longrightarrow A_{1}=\frac12.
\]

于是

\[
\frac{1}{(x^{2}+1)(x-1)}
=\frac{1/2}{x-1}+\frac{B_{1}x+C_{1}}{x^{2}+1}.
\]

代 \(x=0\)：

\[
\frac{1}{1\cdot(-1)}=-\frac12+\frac{C_{1}}{1}
\Longrightarrow C_{1}=-\frac12.
\]

再代一个不等于 \(0,1\) 的值，例如 \(x=-1\)：

\[
\frac{1}{2\cdot(-2)}
=\frac{1/2}{-2}+\frac{B_{1}(-1)-1/2}{2}
\Longrightarrow 0=-\frac{B_{1}-1/2}{2}
\Longrightarrow B_{1}=-\frac12.
\]

（亦可两边清分母后比较系数，此处略。）

现在积分：

\[
\int\frac{dx}{(x^{2}+1)(x-1)}
=\frac12\int\frac{dx}{x-1}
-\frac12\int\frac{x\,dx}{x^{2}+1}
-\frac12\int\frac{dx}{x^{2}+1}
\]
\[
=\frac12\ln|x-1|-\frac14\ln|x^{2}+1|-\frac12\tan^{-1}x+c.
\]

---

### 高次线性幂

若遇到

\[
\int\frac{dx}{(x-1)^{10}},
\]

其实很容易：

\[
\int\frac{dx}{(x-1)^{10}}=-\frac{1}{9}(x-1)^{-9}+c.
\]

---

### 高次二次幂：三角换元

若遇到

\[
\int\frac{dx}{(x^{2}+1)^{10}},
\]

用三角换元：

\[
x=\tan u,\qquad dx=\sec^{2}u\,du,
\]

以及恒等式 \(\tan^{2}u+1=\sec^{2}u\)，得到

\[
\int\frac{\sec^{2}u\,du}{(\sec^{2}u)^{10}}=\int\cos^{18}u\,du.
\]

由此可用「两讲前」引入的方法继续计算。
