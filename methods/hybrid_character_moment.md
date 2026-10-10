# A hybrid sextic-row and cubic-character moment

**9 October 2026 — conventional arithmetic proof, internally cross-reviewed.**
This combines a sextic large sieve with Wu's published Hecke subconvexity
to obtain a fixed-power improvement at low height in both exceptional
cubic-frequency configurations for the actual dense squarefree coefficient.
The row is unrestricted. This is an independent arithmetic input,
not the complete inverse estimate or a new fixed strip.
No Lean execution, priority claim or registry promotion is made.

## 1. Exact coefficient and statement

Work over \(F_0=\mathbb Q(\sqrt{-3})\), with norm \(N\), the program's
primary generators, and a fixed excluded set \(S\) containing primes
above \(2,3\) and the conductor of the fixed finite ray character \(\xi\).
A star restricts an ideal variable to squarefree ideals prime to \(S\).
The literal sextic symbol is \(\chi_{6,n}\), with zeros at nonunits;
write \(\chi_{3,n}=\chi_{6,n}^2\).
Fix \(h=+1\) or \(-1\), and \(\Theta_h(n)=\alpha(n)^h\).
This is the fixed angular Hecke character on primary ideals.

Let \(W\in C_c^\infty(I)\), \(I\subset(0,\infty)\) fixed.
For a common real norm twist \(|u|\le T\), \(T\ge1\), define
\[
 S_\kappa(p,q;u)=
 \sum_n^{*}\Theta_h(n)\xi(n)\chi_{6,n}(\kappa)
 \chi_{3,n}(wpq^2)1_{(n,e)=1}(Nn)^{iu}W(Nn/B).          \tag{HC.1}
\]
Here \(w,e\ne0\) are integral, \(R=N\operatorname{rad}(w)\),
and \(E=Ne\). They are respectively a numerator twist and a pure
excluded-prime mask; their costs are different.
The row \(\kappa\in\mathcal O\setminus\{0\}\) satisfies \(N\kappa\le K\).
It is not assumed squarefree or coprime to any frequency or mask.
All natural zeros in HC.1 remain.

Put
\[
 \alpha=\frac{103}{512},\qquad
 \mathcal R_1=
 B^{-1/3}+(B/K)^{1/3}
 +\left(\frac{B^{257/256}}K\right)^{256/615}
                     R^{103/615}T^{206/615}.
\]
**Theorem.** For every \(\varepsilon>0\), there exists a sufficiently
large fixed derivative order \(J\) such that, for \(K,B\ge2\),
\[
 \sum_{N\kappa\le K,\ \kappa\ne0}
       \sum_{Np\asymp B}^{*}|S_\kappa(p,1;u)|^2
 \ll (KBER(1+T))^\varepsilon
       \|W\|_{C^J(I)}^2 K B^{7/3}\mathcal R_1.           \tag{HC.2}
\]
Constants depend on \(F_0,S,\xi,I,\varepsilon\), and the fixed \(h\),
not on the moving rows, frequencies, conductor or masks.

At the second configuration, \(Np,Nq\asymp B^{1/3}\), \((p,q)=1\),
the elementary unrestricted-row estimate is
\[
 \sum_{\kappa}\sum_{p,q}^{*}|S_\kappa(p,q;u)|^2
 \ll (KBER)^\varepsilon\|W\|_\infty^2 K B^{7/3}
       \left(B^{-2/3}+K^{-1/3}+\frac{B^{1/3}}{\sqrt K}\right).
                                                               \tag{HC.3}
\]
It is uniform in the common \(u\), since the norm modulation has modulus one.
No prime-convolution or rough-support hypothesis is imposed.
The theorem requires the full smooth squarefree sum of HC.1, rather
than arbitrary coefficients substituted in its large-squarepart proof.

## 2. Published inputs and the conductor

[Wu, Theorem 1.1, v6](https://arxiv.org/abs/1604.08551v6)
gives the hybrid bound for unitary Hecke characters over a fixed number
field, with exponent \(1/4-(1-2\theta)/16+\varepsilon\).
[Blomer–Brumley, Theorem 1](https://arxiv.org/abs/1003.0559)
allows \(\theta=7/64\), hence \(\alpha=103/512\).
The angular order and imaginary norm twist enter the analytic conductor.
No general-number-field \(3/16\) bound is asserted.

We also use the sextic large sieve in the program's fixed-field family:
\[
 \sum_{Ns\le M}^{*}
 \left|\sum_{Nn\asymp B}^{*}c_n\chi_{6,n}(s)\right|^2
 \ll (MB)^\varepsilon
           \bigl(M+B+(MB)^{2/3}\bigr)\sum_n|c_n|^2.       \tag{HC.4}
\]
This is [Blomer–Goldmakher–Louvel, Theorem 1.3](https://arxiv.org/abs/1112.1650),
for the order-six family over a field containing the sixth roots of unity.
Fixed supplementary/ray classes are split before applying it.

Write uniquely \(\kappa=\epsilon s a^2\), where \(s\) is squarefree,
\(a\) is arbitrary, and \(\epsilon\) is a unit.
Shared primes of \(s,a\) are allowed. On \(Na\asymp A\),
\(Ns\ll K/A^2\). Reciprocity expresses the finite factor of HC.1
as a unitary Hecke character whose primitive conductor satisfies
\[
 Q_\psi\ll_S Ns\,N\operatorname{rad}(a)\,Np\,R
                    \ll_S KBR/A                         \tag{HC.5}
\]
when \(Np\asymp B,q=1\).
Exponents at overlapping primes can cancel, reducing the primitive
conductor. Their original nonunit zeros are kept as deleted Euler factors.
The numerator twist \(w\) contributes its radical in HC.5;
it cannot be treated as an Euler-hole-only \(\varepsilon\) cost.

The primes of \(S\) in \(\kappa\), its unit, and reciprocity factors give
only a fixed finite family of ray twists. They do not change \(h\).
Thus the character \(\psi=\Theta_h\psi_{\rm fin}\) is always nonprincipal,
including when its finite part is principal.

## 3. Full squarefree Euler sum and large square parts

Let \(\mathcal D\) contain every original zero prime and the mask \(e\).
With the same deleted set in numerator and denominator, the complete
squarefree Dirichlet series is exactly
\[
 \sum_{\substack{n\ {\rm sf}\\(n,\mathcal D)=1}}
             \psi(n)(Nn)^{-z}
       =\frac{L_{F_0}^{\mathcal D}(z,\psi)}
                    {L_{F_0}^{\mathcal D}(2z,\psi^2)}.   \tag{HC.6}
\]
This formula does not restore a character at a canceled or ramified prime.
At \(\Re z=1/2+\delta\), the reciprocal denominator is bounded by
absolute convergence, independently of its conductor.
The numerator is the full primitive Hecke \(L\)-function times its
literal deleted Euler factors. Their product costs
\((N\mathcal D)^\varepsilon\).
In this family \(N\mathcal D\ll_S Ns\,Na\,Np\,R\,E\).

Smooth Mellin inversion moves HC.6 to \(1/2+\delta\).
The nonzero angular order prevents a numerator pole; the denominator
has no zeros on the deformation because \(\Re(2z)>1\).
Wu's bound, with the usual interpolation just to the right of the
central line, and Mellin decay give
\[
 |S_\kappa(p,1;u)|^2
 \ll \|W\|_{C^J}^2(KBER)^\varepsilon
     B(KBR/A)^{2\alpha}(1+T)^{4\alpha+\varepsilon}.        \tag{HC.7}
\]
The analytic conductor has archimedean factor
\(\ll_h(1+|t-u|)^2\); this is the source of the displayed height cost.
All moving masks and finite conductors are retained.

There are \(O(A)\) choices of \(a\), \(O(K/A^2)\) rows \(s\), and
\(O(B)\) frequencies \(p\). Hence the contribution of this \(A\)-dyad,
divided by the benchmark \(KB^{7/3}\), is at most
\[
 (KBER(1+T))^\varepsilon\|W\|_{C^J}^2
      \frac{K^{2\alpha}B^{2\alpha-1/3}R^{2\alpha}T^{4\alpha}}
                         {A^{1+2\alpha}}.               \tag{HC.8}
\]

## 4. Small square parts and the hybrid balance

For fixed \(a,p,q\), the factor \(\chi_{6,n}(a^2)\), all frequency
characters and all masks are column coefficients of modulus at most one.
They are fixed before summing the squarefree row \(s\).
HC.4 therefore bounds that row sum by
\[
 (KB)^\varepsilon B\bigl(K/A^2+B+(KB/A^2)^{2/3}\bigr).
\]
At \(p\asymp B,q=1\), after counting \(a,p\) and dividing by \(KB^{7/3}\),
the three costs are
\[
 \frac{B^{-1/3}}A,\qquad
 \frac{A B^{2/3}}K,\qquad
 (B/K)^{1/3}A^{-1/3}.                                   \tag{HC.9}
\]
There is no extra assumption \((s,a)=1\).
The first and third costs sum geometrically over the \(A\)-dyads.
For the middle cost take its minimum with HC.8.
The elementary bound
\(\min(cA,dA^{-1-2\alpha})
 \le c^{(1+2\alpha)/(2+2\alpha)}d^{1/(2+2\alpha)}\)
holds even if its crossing falls outside \(1\le A\ll\sqrt K\).
It gives
\[
 \left(\frac{B^{(10\alpha+1)/3}}K\right)^{1/(2+2\alpha)}
               R^{\alpha/(1+\alpha)}T^{2\alpha/(1+\alpha)}.
\]
For \(\alpha=103/512\), these exponents are exactly
\[
 \frac{10\alpha+1}3=\frac{257}{256},\quad
 \frac1{2+2\alpha}=\frac{256}{615},\quad
 \frac{\alpha}{1+\alpha}=\frac{103}{615},\quad
 \frac{2\alpha}{1+\alpha}=\frac{206}{615}.
\]
The remaining logarithmic dyad count is absorbed into the indicated
arbitrarily small loss. This proves HC.2.

For HC.3, summing HC.4 over all square parts gives
\[
 \sum_\kappa|\text{inner polynomial}|^2
 \ll (KB)^\varepsilon B
               \bigl(K+B\sqrt K+(KB)^{2/3}\bigr).
\]
Count the \(O(B^{2/3})\) pairs \(p,q\), and divide by \(KB^{7/3}\).
This proves HC.3 without a subconvexity or height hypothesis.

## 5. Positive power at the native binding scale

For a unit numerator twist \(w\), bounded masks and logarithmic height, HC.2 saves a fixed
power whenever \(K\ge B^{257/256+\eta}\), for fixed \(\eta>0\).
More generally its hybrid term requires the actual reserve against
\(B^{257/256}R^{103/256}T^{103/128}\).
The theorem does not discard these height or numerator costs.

At \(D=U^r,\ B=D,\ K=D^2/U,\ r=44411/39400\), the three relative
power savings, before arbitrarily small losses, are
\[
 r/3,\qquad (r-1)/3=5011/118200,\qquad
 (2r-1-257r/256)\,256/615=6041/118200 .
\]
The limiting one is \(5011/118200\approx0.04239425\).
This is a genuine moment estimate for the dense actual coefficient,
not an exponent fit or a prime-convolution replacement.
For larger height the factor in HC.2 must be charged explicitly.

## 6. Full frequency ranges and short-row recovery

The same proof gives an independent full-range moment. Let \(P,Q\ge1\),
put \(Z=P^{2/3}Q^{1/3}\), and retain all the hypotheses and natural zeros
of HC.1. For \(Np\asymp P,Nq\asymp Q,(p,q)=1\),
\[
\begin{aligned}
 \sum_\kappa\sum_{p,q}^{*}|S_\kappa(p,q;u)|^2
 &\ll (KBPQER(1+T))^\varepsilon\|W\|_{C^J}^2
                  KB^2(PQ^2)^{1/3}\,\mathcal R_{\rm gen},\\
 \mathcal R_{\rm gen}
 &=\frac ZB+\frac Z{(KB)^{1/3}}
 +\frac{P^{513/615}Q^{308/615}R^{103/615}T^{206/615}}
                  {(KB)^{256/615}} .                    \tag{HC.10}
\end{aligned}
\]
Here \(J\) is chosen sufficiently large, independently of the moving
lengths. The norm twist is common and the column remains the full
smooth squarefree sequence; no new coefficient class is admitted.

Indeed, count \(O(PQ)\) frequencies in the square-part dyad.
After dividing by \(KB^2(PQ^2)^{1/3}\), HC.4 gives the three costs
\[
 \frac Z{BA},\qquad \frac{AZ}K,\qquad
                    \frac Z{(KB)^{1/3}A^{1/3}}.
\]
The literal primitive conductor is at most \(C_S KPQR/A\),
with \(Q\), not \(Q^2\), entering the conductor.
The large-squarepart cost is therefore
\[
 \frac{K^{2\alpha}P^{2\alpha+2/3}Q^{2\alpha+1/3}
                         R^{2\alpha}T^{4\alpha}}
                    {BA^{1+2\alpha}}.
\]
Take its minimum with \(AZ/K\), as in §4.
The resulting \(P,Q\) exponents are
\((4+10\alpha)/(6+6\alpha)=513/615\) and
\((2+8\alpha)/(6+6\alpha)=308/615\).
The other two terms sum geometrically. This proves HC.10 and its
uniformity, including small neighborhoods of the two earlier endpoints.

This full-range estimate does not remove the short-row recovery cost.
In the proposed cubic-Gauss dispersion with auxiliary row \(F<B\),
the natural frequency range reaches \(H=B^2/F\).
At its edge \(P=H,Q=1\), restoring the original dispersion benchmark
\(\mathcal Q_{\rm disp}=F^{2/3}B^{5/3}\) returns, from the first two
terms of HC.10, respectively
\[
 \mathcal Q_{\rm disp}\frac{H^{2/3}}B=B^2,\qquad
 \mathcal Q_{\rm disp}\frac{H^{2/3}}{(KB)^{1/3}}
                                      =B^{8/3}K^{-1/3}. \tag{HC.11}
\]
For \(K=D^2/U,\ B=D/F\), the second is
\(D^2U^{1/3}/F^{8/3}\), at least \(D^2/U\) when \(F\le\sqrt U\);
the first is also at least \(D^2/U\).
These are the costs returned by this upper-bound method, not lower
bounds for the native signed sum. Earlier diagonal separation alone
does not license deleting the new large-sieve diagonal.
Further joint signed cancellation and fully paid recovery are needed.

## 7. Application boundaries

HC.6 uses a full smooth squarefree ideal sum. A rough restriction,
prime indicator, sharp norm cutoff or arbitrary new coefficient does
not inherit HC.7 without its own exact decomposition and recovery.
Additional row-dependent tests require a quantified common Fourier
majorant; a common norm twist is not replaced by independently
reselected row frequencies.

The moment may replace a character-moment step in a new argument.
It does not import the whole Patterson dispersion theorem outside that
theorem's row/column range, roughness, SW, prime-convolution or height
hypotheses. In particular it does not itself reconstruct the native
signed \(\mu(f')\) covariance, its coupled kernel, moving labels and caps.
The complete GF.2 gain \(\gamma=1/600\), the requested \(0.8749\) strip,
and RH remain unproved.

## 8. Finite-order characters: the zero-angular extension

Set \(h=0\) in HC.1, retaining the full smooth squarefree column,
coprime squarefree frequencies, common norm twist and all natural zeros.
Then **HC.2 and HC.3 hold unchanged**. The general-frequency statement
requires the principal contribution:
\[
 \sum_\kappa\sum_{p,q}^{*}|S_\kappa(p,q;u)|^2
 \ll (KBPQER(1+T))^\varepsilon\|W\|_{C^J}^2
 \left\{KB^2(PQ^2)^{1/3}\mathcal R_{\rm gen}
                         +\sqrt K\,B^2\right\}.          \tag{HC.12}
\]
This extends the character family, rather than its coefficient class.
For \(h=\pm1\) there is no added term.

To prove this, separate rows whose *finite* primitive inducing character
is principal. A nonzero norm twist does not remove this exception: its
numerator pole moves to \(1+iu\). Every other finite character has an
entire numerator in HC.6. The conductor, deleted factors and Wu bound
are unchanged, so the large-squarepart proof applies to these rows.
The small-squarepart sieve is a positive bound for all rows and hence
also for the nonprincipal subset. The balance in §4 then gives HC.10
for that subset. No Euler factors or original zero masks are restored.

For a principal finite character, every good prime \(\pi\notin S\)
must satisfy
\[
 v_\pi(\kappa)+2v_\pi(w)
       +2\,1_{\pi\mid p}+4\,1_{\pi\mid q}\equiv0\pmod6. \tag{HC.13}
\]
This is a necessary condition; the finite \(S\)-ray condition may
exclude further rows. Because \(p,q\) are squarefree and coprime,
the three allowed frequency choices are neither, \(p\), and \(q\).
They add \(0,2,4\), respectively. Thus every good valuation of
\(\kappa\) is even, and for fixed \(\kappa,w\) each good prime has
exactly one allowable choice. If the residue
\(v_\pi(\kappa)+2v_\pi(w)\) is \(0,2,4\), that choice is neither,
\(q\), \(p\), respectively. This includes primes dividing \(w\):
there is no extra number-of-prime-factors cost in \(R\).

Consequently \(\kappa=\epsilon b_S a^2\), where \(b_S\) belongs to
a fixed finite set of squarefree ideals supported on \(S\), and
\(a\) is arbitrary. There are \(O_S(\sqrt K)\) such rows and at most
one pair \((p,q)\) for each. Absolute ideal counting on the original
annulus gives \(|S_\kappa|\ll B\|W\|_\infty\), even with all deleted
primes. Their total energy is therefore
\(O_S(\sqrt K B^2\|W\|_\infty^2)\), which proves HC.12.
The coprimality of \(p,q\) is essential to this count.

At \(P=B,Q=1\), the added term is absorbed by the HC.2 term
\(KB^{7/3}(B/K)^{1/3}=K^{2/3}B^{8/3}\).
HC.3 already follows from the bounded-coefficient large sieve,
without a nonprincipal assumption. Both original configurations
therefore retain their stated fixed-power reserve at \(h=0\).
In general the added *relative* cost is
\[
 K^{-1/2}(PQ^2)^{-1/3},                                 \tag{HC.14}
\]
not \(K^{-1/2}B^{-1/3}\). It is absorbed by the second term of
HC.10 only when \(B^{1/3}\le K^{1/6}PQ\).
It cannot be omitted uniformly: with \(K=2,P=Q=1,w=\xi=1,u=0\)
and nonnegative nonzero \(W\), the \(\kappa=p=q=1\) summand is
\(\asymp B\), so its energy is \(\asymp B^2\). The three original
HC.10 costs are only \(B\), \(B^{5/3}\) and \(B^{974/615}\),
up to sufficiently small losses. A fixed nonunit-frequency example
also exists: take a good prime \(\pi\), \(w=\pi^2,p=\pi,q=1\)
and \(\kappa=1\). The finite character is principal away from its
literal zero at \(\pi\), and the same obstruction remains.

**Native consumer.** Equations (18.21)/(18.26) retain \(G\), outside HC.12.
Lemma 18.2's second Poisson returns ordinary ideal sums. Write
\(S_{\psi,\mathcal D}(C)=\sum_{(n,\mathcal D)=1}
\psi(n)(Nn)^{-1/2}W(Nn/C)\), and use a superscript sf for its
squarefree restriction. The exact decomposition is
\(S_{\psi,\mathcal D}(C)=\sum_{(a,\mathcal D)=1}\psi(a)^2(Na)^{-1}
S^{\rm sf}_{\psi,\mathcal D}(C/(Na)^2)\). Shared primes remain;
the recovered coefficient mass is \(O(\log(2+C))\).
The binding child is \(\sum_{h'}|S_1S_2\prod_iQ_i|^2\), with the original
common character, masks and profile measure. HC.12 controls one squarefree
factor; the live outer prime slots are not its inner cubic twists.
For the no-slot test \(B_1=B_2=\sqrt K,w=1\), fixed ray twists and
bounded heights, the normalized second moment is \(\ll K^{1+\varepsilon}\).
On finite-nonprincipal rows Wu gives the squared pointwise cost
\(K^{103/256+\varepsilon}\), so ordinary Cauchy–Schwarz gives
\(K^{359/256+\varepsilon}\). The finite-principal exception forces
every good row valuation to be divisible by six: at most
\(O_S(K^{1/6})\) rows, with fourth-moment cost \(K^{7/6}\).
The total upper-method cost is still \(K^{359/256+\varepsilon}\),
above the desired \(K^{1+\varepsilon}\), retaining square-part logs.
The \(6\kappa\) load in (18.38)–(18.40) is unchanged; no capacity gain follows.
