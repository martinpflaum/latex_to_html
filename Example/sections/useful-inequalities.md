Some useful inequalities
========================

In this section we collect several inequalities from real analysis which
will be of use later in this monograph.

\[Young’s inequality\] \[thm:Youngs-inequality\] Let $a,b \geq 0$, and
assume that $p,q >0$ satisfy the relation $\frac 1p + \frac 1q =1$. Then
$$ab \leq \frac 1p a^p + \frac 1q b^q \: .$$ Equality holds if and only
if $a^p = b^q$.

Since the second derivative $\exp''$ of the exponential function attains
only positive values, the function $\exp$ is strictly convex that means
satisfies $$\exp \big( \lambda x + (1-\lambda) y \big) \leq 
   \lambda \exp ( x ) +   (1-\lambda)  \exp ( y )$$ for all $x,y\in \R$
and $\lambda \in [0,1]$ with equality holding true if and only if
$x = y$ or $\lambda \in \{ 1,0 \}$. Putting $x = p \ln a$,
$y = q \ln b$, and $\lambda = \frac 1p$ one obtains
$$ab = \exp\big( \lambda x + (1-\lambda) y \big)   \leq 
   \lambda \exp ( x ) +   (1-\lambda)  \exp ( y ) = \frac 1p a^p + \frac 1q b^q \: .$$
Equality holds if and only if $x = y$ which is equivalent to
$a^p = b^q$.

\[Cauchy–Schwarz inequality for sums\]
\[thm:Cauchy-Schwartz-inequality-for-sums\] Let
$z_1,\ldots,z_n, w_1,\ldots,w_n \in \C$. Then
$$\Big| \sum_{i=1}^n z_i \overline{w_i} \: \Big|^2 \leq \Big( \sum_{i1}^n |z_i|^2 \Big)  \Big( \sum_{i=1}^n |w_i|^2 \Big).$$
Equality holds true if and only if $z:= (z_1,\ldots ,z_n) \in \C^n$ and
$w:= (w_1,\ldots ,w_n)\in C^n$ are collinear, i.e. if and only if there
are $a,b \in \C$ such that $az = bw$.

Let us use the *inner product* notation
$$\langle z,w\rangle := \sum_{i=1}^n z_i \overline{w_i} \quad \text{for} \quad z,w\in \C^n.$$
Then the *norm*
$$\| z \| :=  \Big( \sum_{i=1}^n |z_i|^2\Big)^{\frac 12} = \langle z , z \rangle^{\frac 12}$$
is well-defined and non-negative for any $z\in \C^n$. If $\|z \| =0$ or
$\| w \|= 0$, then $z=0$ or $w=0$, and the claim is trivial. So we
assume $\|z \|, \| w \| > 0$ and compute $$\label{eq:inequality-chain}
\begin{split}
  0 \leq \, & \big\langle \|w\| z - \|z\| w , \|w\| z - \|z\| w \big\rangle  = 
  \sum_{i=1}^n \big( \|w\| z_i - \|z\| w_i \big)\big( \|w\| \overline{z_i} - \|z\| \overline{w_i} \big)  = \\ 
  = \, &   \sum_{i=1}^n \|w\|^2 z_i\overline{z_i} - \|w\| \|z\| z_i \overline{w_i}  -  \|w\| \|z\| w_i \overline{z_i} 
    +  \|z\|^2 w_i\overline{w_i}  = \\
  = \, &  2 \|z\|\|w\| \Big(  \|z\|\|w\| - \Re \langle z,w \rangle \Big) .
\end{split}$$ Now choose $c \in \C$ with $|c|=1$ such that
$ c \langle  z,w \rangle = |\langle  z,w \rangle|$. Replacing $z$ by
$cz$ in inequality and observing that $\|cz \|$ and $ \| w \| $ are
positive then entails
$$0 \leq \|c z\|\|w\| - \Re \langle c z,w \rangle  =  \|z\|\|w\| - \Re (c \langle z,w \rangle) =
  \|z\|\|w\| -  |\langle  z,w \rangle|,$$ which is the claimed
Cauchy–Schwartz inequality for sums in abbreviated form.

Equality holds true if and only if $\|w\| c z - \|z\| w =0$. So if
$\|z\|\|w\| =  |\langle  z,w \rangle| $, then $z$ and $w$ are collinear.
To show the converse, assume that $az =bw$ for some $a,b\in \C$. Because
we consider the non-trivial case where both $z$ and $w$ are non-zero, we
can assume without loss of generality that $b=1$. But then
$|\langle z,w \rangle |= |\langle z, az \rangle | = |a| \|z\|^2 = \|z\| \, \|w\|$,
hence equality holds in this case. The proof is finished.

\[Hölder’s inequality for sums\]

\[Minkowski’s inequality for sums\]
