# MIT OCW 18.01 Lecture 15 讲义 · 中文译本

> **编号说明（必读）**：本文件名写作 `OCW_18.01_L14_…`，是为与 Bilibili 合集 **BV1mNgm66EZu · P14**（14-微分与不定积分）对齐。对应的官方 PDF 实为 Fall 2006 **`lec15.pdf`（Lecture 15: Differentials and Antiderivatives）**。OCW 课程日历中的 **Lecture 8** 是 Exam 1，**没有**常规讲义 PDF / 本系列课堂录像；故 Bilibili P14 ↔ OCW Lecture 15。课堂口播与讲义数值主例等差异见同目录 [`MIT1801_L14_课上思路.md`](./MIT1801_L14_课上思路.md) §6。  
> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec15.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。本讲 PDF 无印刷图（仅文字与公式），故无 `ocw_figs/` 嵌入。

---

## Lecture 15: Differentials and Antiderivatives

（第 15 讲：微分与反导数）

18.01 Fall 2006

---

## Differentials（微分）

**新记号：**
\[
dy = f'(x)\,dx \qquad (y=f(x)).
\]

\(dy\) 与 \(f'(x)\,dx\) 都称为**微分（differentials）**。可以把
\[
\frac{dy}{dx}=f'(x)
\]
看作微分之商。其用途之一是线性近似：
\[
\frac{\Delta y}{\Delta x}\approx\frac{dy}{dx}.
\]

### Example 1. 近似 \(65^{1/3}\)

**Method 1（复习线性近似）**

\[
\begin{align*}
f(x)&=x^{1/3},\\
f'(x)&=\frac13 x^{-2/3},\\
f(x)&\approx f(a)+f'(a)(x-a),\\
x^{1/3}&\approx a^{1/3}+\frac13 a^{-2/3}(x-a).
\end{align*}
\]

好的基点是 \(a=64\)，因为 \(64^{1/3}=4\)。令 \(x=65\)：
\[
65^{1/3}=64^{1/3}+\frac13\cdot64^{-2/3}(65-64)
=4+\frac13\cdot\frac1{16}\cdot1
=4+\frac1{48}\approx4.02.
\]

类似地，
\[
(64.1)^{1/3}\approx4+\frac1{480}.
\]

**Method 2（复习）**
\[
65^{1/3}=(64+1)^{1/3}=\Bigl[64\Bigl(1+\frac1{64}\Bigr)\Bigr]^{1/3}
=64^{1/3}\Bigl(1+\frac1{64}\Bigr)^{1/3}
=4\Bigl(1+\frac1{64}\Bigr)^{1/3}.
\]

接着用近似 \((1+x)^{r}\approx1+rx\)，取 \(r=\frac13\)、\(x=\frac1{64}\)：
\[
65^{1/3}\approx4\Bigl(1+\frac13\cdot\frac1{64}\Bigr)=4+\frac1{48}.
\]

这与 Method 1 的结果相同。

**Method 3（用微分记号）**
\[
\begin{align*}
y&=x^{1/3}\Big|_{x=64}=4,\\
dy&=\frac13 x^{-2/3}\,dx\Big|_{x=64}
=\frac13\cdot\frac1{16}\,dx
=\frac1{48}\,dx.
\end{align*}
\]

我们要 \(dx=1\)，因为 \(x+dx=65\)。当 \(dx=1\) 时 \(dy=\frac1{48}\)。故
\[
65^{1/3}=4+\frac1{48}.
\]

三种方法背后共通的是
\[
y=x^{1/3},\qquad
\frac{dy}{dx}=\frac13 x^{-2/3}\Big|_{x=64}.
\]

---

## Anti-derivatives（反导数）

\[
F(x)=\int f(x)\,dx
\]
表示 \(F\) 是 \(f\) 的**反导数（antiderivative）**。

其它等价说法：
\[
F'(x)=f(x)\qquad\text{或}\qquad dF=f(x)\,dx.
\]

**例子：**

1. \(\displaystyle\int\sin x\,dx=-\cos x+c\)，其中 \(c\) 为任意常数。

2. \(\displaystyle\int x^{n}\,dx=\frac{x^{n+1}}{n+1}+c\)，当 \(n\neq-1\)。

3. \(\displaystyle\int\frac{dx}{x}=\ln|x|+c\)（处理了第 2 条中 \(n=-1\) 的例外）。

4. \(\displaystyle\int\sec^{2}x\,dx=\tan x+c\)。

5. \(\displaystyle\int\frac{dx}{\sqrt{1-x^{2}}}=\sin^{-1}x+c\)（这里 \(\sin^{-1}x\) 表示反正弦 / arcsin，**不是** \(1/\sin x\)）。

6. \(\displaystyle\int\frac{dx}{1+x^{2}}=\tan^{-1}(x)+c\)。

**性质 3 的证明**（PDF 标题写作 “Proof of Property 2”，正文实为上面第 3 条 \(\int dx/x\) 在 \(x<0\) 的验证。）

绝对值 \(|x|\) 对正负 \(x\) 都给出正确答案。现对 \(x<0\) 再核对一遍：
\[
\ln|x|=\ln(-x).
\]
令 \(u=-x\)，则
\[
\frac{d}{dx}\ln(-x)=\Bigl(\frac{d}{du}\ln u\Bigr)\frac{du}{dx}
=\frac1u\cdot(-1)
=\frac1{-x}\cdot(-1)
=\frac1x.
\]

---

## Uniqueness of the antiderivative up to an additive constant
（反导数在加一个常数意义下的唯一性）

若 \(F'(x)=f(x)\) 且 \(G'(x)=f(x)\)，则存在常数 \(c\) 使
\[
G(x)=F(x)+c.
\]

**证明：**
\[
(G-F)'=f-f=0.
\]

回顾：作为中值定理的推论，我们已证明「若一函数的导数恒为零，则它是常数」。故 \(G(x)-F(x)=c\)（某常数 \(c\)），亦即 \(G(x)=F(x)+c\)。

---

## Method of substitution（换元法）

### Example 1. \(\displaystyle\int x^{3}(x^{4}+2)^{5}\,dx\)

**换元：**
\[
u=x^{4}+2,\qquad du=4x^{3}\,dx,\qquad
(x^{4}+2)^{5}=u^{5},\qquad
x^{3}\,dx=\frac14\,du.
\]

故
\[
\int x^{3}(x^{4}+2)^{5}\,dx
=\frac14\int u^{5}\,du
=\frac{u^{6}}{4\cdot6}+c
=\frac{u^{6}}{24}+c
=\frac1{24}(x^{4}+2)^{6}+c.
\]

### Example 2. \(\displaystyle\int\frac{x}{\sqrt{1+x^{2}}}\,dx\)

另一条求反导数的路是「高级猜测（advanced guessing）」。先写
\[
\int\frac{x}{\sqrt{1+x^{2}}}\,dx=\int x(1+x^{2})^{-1/2}\,dx.
\]

**猜测：** \((1+x^{2})^{1/2}\)。验证：
\[
\frac{d}{dx}(1+x^{2})^{1/2}
=\frac12(1+x^{2})^{-1/2}\cdot(2x)
=x(1+x^{2})^{-1/2}.
\]

因此
\[
\int x(1+x^{2})^{-1/2}\,dx=(1+x^{2})^{1/2}+c.
\]

### Example 3. \(\displaystyle\int e^{6x}\,dx\)

**猜测：** \(e^{6x}\)。验证：
\[
\frac{d}{dx}e^{6x}=6e^{6x}.
\]

因此
\[
\int e^{6x}\,dx=\frac16 e^{6x}+c.
\]

### Example 4. \(\displaystyle\int x e^{-x^{2}}\,dx\)

**猜测：** \(e^{-x^{2}}\)。求导验证：
\[
\frac{d}{dx}e^{-x^{2}}=(-2x)e^{-x^{2}}.
\]

因此
\[
\int x e^{-x^{2}}\,dx=-\frac12 e^{-x^{2}}+c.
\]

### Example 5. \(\displaystyle\int\sin x\cos x\,dx=\frac12\sin^{2}x+c\)

另一个同样可接受的答案是
\[
\int\sin x\cos x\,dx=-\frac12\cos^{2}x+c.
\]

这看似矛盾，故验证：
\[
\frac{d}{dx}\sin^{2}x=(2\sin x)(\cos x),
\]
\[
\frac{d}{dx}\cos^{2}x=(2\cos x)(-\sin x).
\]

两者都对。消解「悖论」：两答之差是常数——
\[
\frac12\sin^{2}x-\Bigl(-\frac12\cos^{2}x\Bigr)
=\frac12(\sin^{2}x+\cos^{2}x)=\frac12.
\]

于是
\[
\frac12\sin^{2}x-\frac12
=\frac12(\sin^{2}x-1)
=\frac12(-\cos^{2}x)
=-\frac12\cos^{2}x.
\]

两答实际上等价：从一个答案到另一个，常数 \(c\) 平移了 \(\frac12\)。

### Example 6. \(\displaystyle\int\frac{dx}{x\ln x}\)（假定 \(x>0\)）

令 \(u=\ln x\)，则 \(du=\frac1x\,dx\)。代入得
\[
\int\frac{dx}{x\ln x}=\int\frac1u\,du=\ln u+c=\ln(\ln x)+c.
\]
