# MIT OCW 18.01 Lecture 7 讲义 · 中文译本

> **来源**：https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/lec7.pdf  
> **课程**：18.01 Single Variable Calculus，Fall 2006  
> **说明**：英文原文具有权威性；本文件为中文学习转写。引用与条款见 http://ocw.mit.edu/terms 。数学式保留 LaTeX。本讲 PDF 无印刷图（仅文字与公式），故无 `ocw_figs/` 嵌入。

---

## Lecture 7: Continuation and Exam Review

（第 7 讲：续讲与考试复习）

18.01 Fall 2006

---

## Hyperbolic Sine and Cosine（双曲正弦与双曲余弦）

双曲正弦（读作 “sinsh”）：

\[
\sinh(x)=\frac{e^x-e^{-x}}{2}.
\]

双曲余弦（读作 “cosh”）：

\[
\cosh(x)=\frac{e^x+e^{-x}}{2}.
\]

求导：

\[
\frac{d}{dx}\sinh(x)
=\frac{d}{dx}\frac{e^x-e^{-x}}{2}
=\frac{e^x-(-e^{-x})}{2}
=\cosh(x).
\]

同理，

\[
\frac{d}{dx}\cosh(x)=\sinh(x).
\]

（注意：这与 \(\dfrac{d}{dx}\cos(x)\) 不同——后者带负号。）

**重要恒等式**：

\[
\cosh^2(x)-\sinh^2(x)=1.
\]

**证明**：

\[
\begin{aligned}
\cosh^2(x)-\sinh^2(x)
&=\Bigl(\frac{e^x+e^{-x}}{2}\Bigr)^2
-\Bigl(\frac{e^x-e^{-x}}{2}\Bigr)^2\\
&=\frac14\bigl(e^{2x}+2+e^{-2x}\bigr)
-\frac14\bigl(e^{2x}-2+e^{-2x}\bigr)
=\frac14(2+2)=1.
\end{aligned}
\]

**为何叫「双曲」？**  
令 \(u=\cosh(x)\)，\(v=\sinh(x)\)，则

\[
u^2-v^2=1,
\]

这是双曲线方程。普通三角函数是「圆」函数：若 \(u=\cos(x)\)，\(v=\sin(x)\)，则

\[
u^2+v^2=1,
\]

这是圆的方程。

---

## Exam 1 Review（第一次考试复习）

### General Differentiation Formulas（通用求导公式）

\[
\begin{aligned}
(u+v)'&=u'+v',\\
(cu)'&=cu',\\
(uv)'&=u'v+uv'\quad\text{（积法则）},\\
\Bigl(\frac{u}{v}\Bigr)'&=\frac{u'v-uv'}{v^2}\quad\text{（商法则）},\\
\frac{d}{dx}f\bigl(u(x)\bigr)&=f'\bigl(u(x)\bigr)\cdot u'(x)\quad\text{（链式法则）}.
\end{aligned}
\]

记忆商法则的一种方式：改写

\[
\Bigl(\frac{u}{v}\Bigr)'=(uv^{-1})',
\]

再对之施用积法则与链式法则。

---

### Implicit differentiation（隐函数求导）

若要从形如

\[
y^3+3xy^2=8
\]

的方程求 \(y'\)，不必先解出 \(y\) 再求导，而是对整式取 \(\dfrac{d}{dx}\)。本例：

\[
\begin{aligned}
3y^2 y'+6xy\,y'+3y^2&=0,\\
(3y^2+6xy)y'&=-3y^2,\\
y'&=\frac{-3y^2}{3y^2+6xy}.
\end{aligned}
\]

注意：\(y'\) 的公式同时含 \(x\) 与 \(y\)。隐函数求导对求反函数的导数特别有用。

例如：

\[
y=\sin^{-1}x\quad\Rightarrow\quad\sin y=x.
\]

隐式求导得 \((\cos y)y'=1\)，于是

\[
y'=\frac{1}{\cos y}=\frac{1}{\sqrt{1-x^2}}.
\]

---

### Specific differentiation formulas（具体求导公式）

你需要掌握下列函数的导数公式，并会从已有信息推出它们：

\[
x^n,\;\sin^{-1}x,\;\tan^{-1}x,\;\sin x,\;\cos x,\;\tan x,\;\sec x,\;e^x,\;\ln x.
\]

例如，计算 \(\dfrac{d}{dx}\sec x\)：

\[
\frac{d}{dx}\sec x
=\frac{d}{dx}\frac{1}{\cos x}
=\frac{-(-\sin x)}{\cos^2 x}
=\tan x\sec x.
\]

也可能要求你用下列信息求 \(\dfrac{d}{dx}\sin x\) 或 \(\dfrac{d}{dx}\cos x\)：

\[
\lim_{h\to0}\frac{\sin h}{h}=1,
\qquad
\lim_{h\to0}\frac{\cos h-1}{h}=0.
\]

记住导数的定义：

\[
\frac{d}{dx}f(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}.
\]

---

### Tying up a loose end（收尾一个遗留问题）

如何求 \(\dfrac{d}{dx}x^r\)，其中 \(r\) 为实数（不必有理）？此前我们只用隐式求导处理了有理情形。现有两种做法：

#### 方法一：底 \(e\)

\[
x=e^{\ln x},
\qquad
x^r=(e^{\ln x})^r=e^{r\ln x}.
\]

\[
\begin{aligned}
\frac{d}{dx}x^r
&=\frac{d}{dx}e^{r\ln x}
=e^{r\ln x}\cdot\frac{d}{dx}(r\ln x)
=e^{r\ln x}\cdot\frac{r}{x}\\
&=x^r\cdot\frac{r}{x}
=r x^{r-1}.
\end{aligned}
\]

#### 方法二：对数微分

\[
(\ln f)'=\frac{f'}{f}
\quad\Leftrightarrow\quad
f'=f\,(\ln f)'.
\]

取 \(f=x^r\)：\(\ln f=r\ln x\)，\((\ln f)'=r/x\)，故

\[
f'=x^r\cdot\frac{r}{x}=r x^{r-1}.
\]

---

### 兑现第一讲的承诺

第一讲曾许诺：你们将学会对「任何东西」求导——哪怕复杂如

\[
\frac{d}{dx}e^{x\tan^{-1}x}.
\]

现在就来做！一般地，

\[
\frac{d}{dx}e^{uv}=e^{uv}\frac{d}{dx}(uv)=e^{uv}(u'v+uv').
\]

代入 \(u=x\)，\(v=\tan^{-1}x\)：

\[
\boxed{
\frac{d}{dx}e^{x\tan^{-1}x}
=e^{x\tan^{-1}x}
\Bigl(\tan^{-1}x+x\cdot\frac{1}{1+x^2}\Bigr).
}
\]
