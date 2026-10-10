# Harmonic Möbius cancellation in a reflected ratio family

**9 October 2026 — conventional arithmetic proof, with scoped recovery.**
The common divisor in the reflected Heath–Brown source has no surviving
character phase. Its signed sum gives a fixed-power coefficient saving,
and the complete growing family below is paid. The large reduced-numerator
complement remains open. This is not the complete inverse gain, a new
strip, a new engine, or a priority claim. No Lean execution is used.

The parent research repository's finite audit and stored controls
check source identities and exact exponents, not the analytic estimates.

## 1. The original source and inputs

Work over \(F=\mathbb Q(\sqrt{-3})\), with ideal norm \(N\).
Fix the original finite-order character \(\nu\) and its full defining
presentation, with excluded primes in \(S\), including those above \(2,3\).
The source is the unmarked inverse of the pinned
[OpenAI manuscript, §17](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf):
\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\epsilon_\chi},\qquad
 \epsilon_\chi\in\{1,-1\},\qquad
 M_u=D_u^{-1/2}\sum_n\mu(n)\psi_u(n)F_u(Nn/D_u),          \tag{HR.1}
\]
\[
 F_u(y)=W_1(y)V_{\le}(D_u y/D_{*,u})
                   y^{-\sigma_u+i\omega_u}.
\]
Here \(D_u\asymp D=U^r\), \(1\le r\le3/2\), and \(u\) runs over any
actual sixth-power-free detector fiber \(\mathcal C\), with \(0<Nu\ll U\).
Every selected \(\sigma_u,\omega_u,D_{*,u}\), bounded annular ratio,
zero extension and original profile measure is retained.
The negative character orientation uses conjugation with the same zeros,
never division at a nonunit. The original ideal variables are prime to
\(S\); primary generators are used
only to evaluate the literal symbol. Fixed unit/ray classes are all kept.

The inputs are the ordinary Hecke functional equation, the
[order-six large sieve, BGL Theorem 1.3](https://arxiv.org/abs/1112.1650),
and the pinned external \(7/8\) zero-free assertion for \(\zeta_F\).
Only this conservative boundary, not a later manual refinement, is used.
All constants may depend on the fixed field, presentation and tests.

Write \(R_{\mathrm{def},u}=\operatorname{rad}(Su)\) for the full original
zero support. Let \(\psi_{0,u}\) be the primitive inducing character and
\(E_u\) the redundant deleted-prime product, so
\[
 L(s,\psi_u)=L(s,\psi_{0,u})
                 \prod_{p\mid E_u}(1-\psi_{0,u}(p)(Np)^{-s}).
\]
Each prime of \(u\) outside \(S\) is primitive because \(u\) is
sixth-power-free. Consequently \(E_u\) is supported in the fixed \(S\)
datum; it is not a new growing puncture. The functional-equation scale
\(Q_u\), including the fixed discriminant convention, satisfies
\(Q_u NE_u\ll_\nu U\). The sets \(R_{\mathrm{def},u}\) and \(E_u\)
have different roles and will not be identified.

The estimates below are on nonprincipal inducing rows. A principal row
retains the residue described in §2 and its existing exceptional-row
payment. No principal pole is discarded.

## 2. Smooth Heath–Brown identity

Fix \(\chi\in C^\infty([0,\infty))\), equal to one on \([0,1]\),
zero on \([2,\infty)\). Put
\(\mu_Z(n)=\mu(n)\chi(Nn/Z)\) on ideals prime to \(S\).
Choose \(Z\asymp\sqrt D\) with \(Z^2\) above every original annular
support and \(2Z\) below it; this is possible for all sufficiently
large \(D\). Bounded \(D\) retains the existing finite-size payment.
The convolution identity is
\[
 \mu-2\mu_Z+\mu_Z*\mu_Z*1
               =(\mu-\mu_Z)*(\mu-\mu_Z)*1.
\]
The right side is supported on \(Nn>Z^2\). Thus on the original annulus
\(\mu=-\mu_Z*\mu_Z*1\). All convolutions here are in the good-ideal
semigroup. Shared primes have not been removed: at a repeated prime the
four coefficients \(+1,-1,-1,+1\) cancel with the same character value.

Set \(\lambda_Z=\mu_Z*\mu_Z\). Mellin inversion gives the exact source
\[
 M_u=-D_u^{-1/2}\int_{(c)}
   \widetilde F_u(s)D_u^s L(s,\psi_u)
   \left(\sum_n\mu_Z(n)\psi_u(n)(Nn)^{-s}\right)^2
                         \frac{ds}{2\pi i},\qquad c>1.   \tag{HR.2}
\]
At a zero of \(L\) this integrand is holomorphic. If the inducing
character is principal, contour passage through \(s=1\) instead retains
the literal contribution
\(-\operatorname{Res}_{s=1}L(s,\psi_u)\,
 D_u^{1/2}\widetilde F_u(1)P_{Z,u}(1)^2\).
Holomorphy at zeros does not itself give a fixed-power estimate.

The principal rows can be paid directly in the **original**, recombined
source. They are supported entirely on the fixed \(S\) datum, hence form
a fixed finite set. Their Möbius series is \(1/\zeta_F^{R_{\mathrm{def},u}}(s)\).
Moving its smooth Mellin contour to \(7/8+\delta\) gives
\[
 \sum_{u\in\mathcal C_{\rm pr}}|M_u|^2
       \ll D^{3/4+\varepsilon}\mathcal H_J.
\]
The zeta pole at one is a reciprocal zero. Uniformly in \(1\le r\le3/2\),
the target exponent \(h(r)\) of §6 exceeds \(3r/4\) by at least
\(497/2000\). This does not bound individual principal \(M_{u,X}\)
pieces or delete their residue in a decomposed HB formula.

## 3. Reflection and the exact reduced-ratio coefficient

Use the normalization
\[
 L(s,\psi_{0,u})=\varepsilon_u Q_u^{1/2-s}G(s)
                                  L(1-s,\overline{\psi_{0,u}}),
 \qquad |\varepsilon_u|=1.
\]
The gamma quotient is the ordinary finite-order Hecke quotient; all
fixed ray calibrations are contained in the actual inducing character
and root number. Define the common radial transform by
\[
 C_u^\#(z)=\int_{(1/2)}
       \widetilde F_u(1-w)G(1-w)z^{-w}\frac{dw}{2\pi i}.
\]
This is the ordinary radial Fourier/Hankel transform for the finite-order
archimedean type \(h_\infty=0\), in the same fixed discriminant calibration.
The plain factor at scale \(C\) has raw prefactor \(C/\sqrt{Q_u}\);
centrally normalized, its dual scale is \(Q_u/C\).
Expansion of every deleted Euler factor before reflection gives
\[
 \begin{split}
 M_u={}&-\varepsilon_u\sqrt{D_u/Q_u}
 \sum_{e\mid E_u}\frac{\mu(e)\psi_{0,u}(e)}{Ne}
 \sum_{\substack{x,y\\(x,y)=1}}
 \frac{S_Z(x;R_{\mathrm{def},u})}{Nx}
       \psi_u(x)\overline{\psi_{0,u}(y)}\\
 &\hspace{25mm}\cdot
 C_u^\#\!\left(\frac{Ny\,D_u}{Nx\,Q_u\,Ne}\right).
                                                               \tag{HR.3}
 \end{split}
\]
This follows by writing \(ab=t x\), \(c'=t y\), with
\(t=(ab,c')\), in the reflected free factor. Its kernel is independent
of \(t\), and the two character values on \(t\) cancel on retained units.
The exact coefficient is
\[
 S_Z(x;R)=\sum_t\frac{\lambda_Z(t x)}{Nt}1_{(t,R)=1}.       \tag{HR.4}
\]
There is no condition \((t,y)=1\), nor a new condition \((t,x)=1\).
Their primes may overlap. The primitive \(y\) has its original primitive
zeros; it is not individually punctured at every prime of \(E_u\).
The complete \(e\)-sum restores the original free-factor zero extension.

Since \(a,b\) are squarefree, \(x\) is cube-free. On the retained
\((x,R)=1\) support write uniquely \(x=x_1x_2^2\), with \(x_1,x_2\)
squarefree and coprime. Define
\[
 P_T^{R}(1)=\sum_{(a,R)=1}\frac{\mu(a)}{Na}\chi(Na/T).
\]
Extracting the full \(x\)-prime supports of \(a,b\) proves
\[
 \boxed{\displaystyle
 S_Z(x;R)=
 \sum_{\substack{d,e\mid x_1\\[d,e]=x_1}}
 \frac{\mu(d)\mu(e)Nx_1}{Nd\,Ne}
 P_{Z/(Nx_2Nd)}^{R\operatorname{rad}x}(1)
 P_{Z/(Nx_2Ne)}^{R\operatorname{rad}x}(1).}              \tag{HR.5}
\]
HR.5 is asserted only for \((x,R)=1\). At a nonunit \(x\), the term
in HR.3 vanishes through \(\psi_u(x)\); \(S_Z(x;R)\) itself need not vanish.
A prime in \(x_2\) belongs to both Möbius factors. A prime in \(x_1\)
belongs to the first, second, or both, with coefficients
\(-1,-1,+1/Np\). The remaining two Möbius sums are independent and
may share primes outside \(x\). This proves HR.5 without an arbitrary
coefficient substitution or a Gauss-spin assumption.

## 4. The signed harmonic saving

The Mellin transform of \(\chi\) continues across zero with a simple
pole there. In
\[
 P_T^R(1)=\int_{(c)}
       \widetilde\chi(w)T^w/\zeta_F^R(1+w)\,
                                      \frac{dw}{2\pi i},
\]
that pole cancels the reciprocal-zeta zero at \(w=0\). The external
\(7/8\) input permits the line \(\Re w=-1/8+\delta\). The fixed-field
reciprocal has polynomial vertical growth on this separated line;
the smooth Mellin decay pays it. The deleted Euler product is
\(\ll_{\delta,\varepsilon}(NR)^\varepsilon\).
For all positive \(T\), with empty small supports interpreted literally,
\[
 |P_T^R(1)|\ll_{\varepsilon,S,\chi}
             (NR\max\{1,T\})^\varepsilon T^{-1/8+\varepsilon}.
\]
In HR.5 the absolute local factor is
\[
 Nx_1\prod_{p\mid x_1}
       \{2(Np)^{-7/8}+(Np)^{-7/4}\}
 \ll_\varepsilon (Nx_1)^{1/8+\varepsilon}.
\]
The \(x_2\) factors contribute \((Nx_2)^{1/4}\).
Choosing subsidiary contour losses after the requested \(\varepsilon\)
therefore gives
\[
 \boxed{|S_Z(x;R_{\mathrm{def},u})|
       \ll (UD)^\varepsilon (Nx/D)^{1/8}.}              \tag{HR.6}
\]
Only constants change because \(Z^2\asymp D\). This is cancellation in
the actual common-factor coefficient before taking its norm.

## 5. Complete profile and short-dual recovery

Let \(M_{u,X}\) be HR.3 restricted by a fixed smooth partition to
\(Nx\asymp X\). It retains every \(e,y\) term and the entire transform.
For \(X\ll D/\sqrt U\) the effective plain scale satisfies
\[
       Y_{u,e,x}=Q_u Ne\,Nx/D_u\ll_\nu UX/D\ll\sqrt U.
\]
The classical sextic large sieve on squarefree columns, with unrestricted
rows obtained by \(u=v b^2\), gives the factor
\(U+B\sqrt U+(UB)^{2/3}\). A full ideal plain is recovered by
\(y=s a^2\), \(s\) squarefree, with no \((s,a)=1\) condition.
The centrally normalized \(a\)-weights are \(1/Na\), so their harmonic
sum is logarithmic. The annular normalized norm is consequently
\[
 (UB)^\varepsilon
       \{U^{1/2}+U^{1/4}B^{1/2}+U^{1/3}B^{1/3}\}
                  \|W\|_{C^J}.                         \tag{HR.7}
\]
The literal \((x,y)=1\) projector may be retained in the squarefree
coefficient, or restored with its finite Euler children of normalized
mass \(\sum_{d\mid\operatorname{rad}x}(Nd)^{-1/2}
\ll_\varepsilon(Nx)^\varepsilon\); their lengths only decrease.
Dual primes in \(S\) are restored by all \(S\)-supported power children,
with fixed convergent mass \(\sum_b(Nb)^{-1/2}\).
All natural zeros are preserved in both decompositions.

The transform is bounded on small radial annuli and rapidly decreasing
on large ones. At \(B=Y2^j\) the central annular weight is \(2^{j/2}\).
For \(j<0\) its fixed seminorm is bounded; for \(j>0\) it is
\(\ll_A2^{-Aj}\). Applied to HR.7, the three sums have weights
\(2^{j/2},2^j,2^{5j/6}\), respectively. A fixed \(A>1+\varepsilon\)
pays them all. Because \(Y\le\sqrt U\), the full normalized plain norm
is \(\ll U^{1/2+\varepsilon}\) times those fixed seminorms.
This also covers \(Y<1\) by the exact rapidly decreasing positive tail;
below-unit children are not declared empty.

Split \(Q_u\) into dyads and recover its bounded ratios, the original
selected \(\sigma_u,\omega_u\), and \(D_u/D\) using the common finite
Sobolev/Mellin measure. The derivative orders are fixed before the
corresponding polynomial height exponent. Write \(\mathcal H_J\) for
the resulting literal original profile and height cost, together with
the fixed \(\chi\) seminorms. It is not assigned zero cost.

After HR.6, triangle over \(x\) is now legitimate. For a fixed \(e\)
the norm is bounded by
\[
 \sqrt{D/Q}\,\frac1{Ne}\,
 X\frac{(X/D)^{1/8}}{X}
 \sqrt{UQ\,Ne\,X/D}\,\mathcal H_J^{1/2}
 =\frac{\sqrt{UX}}{\sqrt{Ne}}(X/D)^{1/8}
                                      \mathcal H_J^{1/2}.
\]
Every \(e\mid E_u\) is in the fixed \(S\) datum. Their complete finite
mass, all conductor dyads and the \(x\)-partition losses are paid.
Write \(\mathcal C_{\mathrm{np}}\) for the nonprincipal inducing rows of
the original fiber. We obtain the actual recovered-family estimate
\[
 \boxed{\sum_{u\in\mathcal C_{\mathrm{np}}}|M_{u,X}|^2
        \ll (UD)^\varepsilon UX(X/D)^{1/4}\mathcal H_J.} \tag{HR.8}
\]
It holds uniformly with the original selected data. The same bound
with the largest \(X\) pays a lower ball after logarithmic dyad recovery.

## 6. Paid exponent range and the surviving complement

At the binding \(r=44411/39400\), the complete reduced-numerator family
\(Nx\le U^{3/10}\) has HR.8 exponent
\[
 1+\frac3{10}-\frac14\left(r-\frac3{10}\right)
 =\frac{172289}{157600}=1.0932043147\ldots.
\]
The required inverse exponent is \(261061/236400\); the difference is
exactly \(1051/94560>0\). The family has a growing nonempty dual range
above \(X\asymp D/U\), with all smaller reflected tails also included.

For the whole bounded \(r\)-range, put
\[
 h(r)=\max\{1,(1+5r)/6-1/600\},\qquad
 \beta(r)=\frac45\{h(r)-1+r/4\}
 =\begin{cases}
 r/5,&r\le501/500,\\
 (13r-10)/15-1/750,&r\ge501/500.
 \end{cases}
\]
Uniformly, \(r-1<\beta(r)<r-1/2\) for \(1\le r\le3/2\).
For any sufficiently small fixed \(\eta>0\), HR.8 therefore pays the
entire family \(Nx\le U^{\beta(r)-\eta}\) by
\(U^{h(r)-5\eta/4+\varepsilon}\mathcal H_J\).
This is a uniform component payment, not the complete \(h(r)\) estimate.

The large-\(x\) complement is explicit. For distinct good prime ideals
\(Np,Nq\in(Z/2,Z]\), with \((pq,R)=1\), all remaining cutoff factors
are units, since the first nonunit good ideal has norm at least \(7\).
Thus
\[
             S_Z(pq;R)=2\chi(Np/Z)\chi(Nq/Z)\ne0.
\]
These balanced prime-pair numerators have size \(\asymp D\). Their dual
plain has length \(\asymp Q_u Ne\ll_\nu U\), and \(\asymp U\) on
full-conductor rows \(Q_u\asymp U\). Its exact coprime selector remains.
The harmonic common-factor saving does not pay this surviving covariance.
The complete original source is the paid ratio family plus this retained
complement and any retained principal residue; no full inverse
\(\gamma=1/600\), complete-source contraction or stronger strip follows.

## 7. Higher-order opening retains a balanced prime face

**9 October 2026 — exact higher-order source check.** Fix an integer
\(J\ge2\). For this representation choose a new
\(Z_J\asymp D^{1/J}\) with \(Z_J^J\) covering the original annulus,
and put \(\mu_{Z_J}(n)=\mu(n)\chi(Nn/Z_J)\).
This is not §2's unchanged \(\sqrt D\) cutoff when \(J>2\).
With \(E=\delta-1*\mu_{Z_J}\), the identity
\[
 \mu=\sum_{j=1}^J(-1)^{j-1}\binom Jj
                \mu_{Z_J}^{*j}*1^{*(j-1)}+\mu*E^{*J}
\]
is exact; its remainder has support \(Nn>Z_J^J\).
The \(j=1\) term is unreflected and retained, even where the
original-annulus support test makes it zero.

For \(j\ge2\), put \(k=j-1\), \(\lambda_j=\mu_{Z_J}^{*j}\) and
\(\tau_k=1^{*k}\). On nonprincipal inducing rows expand
\[
 \prod_{p\mid E_u}(1-\psi_{0,u}(p)(Np)^{-s})^k
       =\sum_e b_{k,u}(e)\psi_{0,u}(e)(Ne)^{-s}.
\]
Here \(v_p(e)\le k\), and \(b_{k,u}(p^a)=(-1)^a\binom ka\);
these fixed deleted-Euler children need not be squarefree.
The functional equation gives the exact reflected \(j\)-term
(before its Heath–Brown binomial coefficient)
\[
 \varepsilon_u^k\sqrt{D_u/Q_u^k}
 \sum_e\frac{b_{k,u}(e)\psi_{0,u}(e)}{Ne}
 \sum_{(x,y)=1}\frac{\psi_u(x)\overline{\psi_{0,u}(y)}}{Nx}
 S_{j,Z_J}(x,y;R_{\mathrm{def},u})
 C^\#_{j,u}\!\left(\frac{NyD_u}{NxQ_u^kNe}\right),
\]
where the full common-factor coefficient and transform are
\[
 S_{j,Z_J}(x,y;R)=
       \sum_t\frac{\lambda_j(tx)\tau_k(ty)}{Nt}1_{(t,R)=1},
 \qquad
 C^\#_{j,u}(z)=\int_{(1/2)}
   \widetilde F_u(1-w)G(1-w)^kz^{-w}\frac{dw}{2\pi i}.
\]
No \((t,y)=1\) or new dual puncture has been inserted.
All original profiles, primitive zeros, fixed Euler children and
the common coprime selector remain. Principal residues are retained
in the original recombination. For \(k>1\), this gamma-power transform
can have logarithmic origin terms; HR.7–8's profile payment is not
automatically licensed for it. Its dual scale is \(Q_u^kNe\,Nx/D_u\).

Take \(x=\prod_{i=1}^Jp_i\), with distinct good primes
\(Np_i\in(Z_J/2,Z_J]\), \((x,R)=1\), and \(Z_J\) sufficiently large.
Two such primes cannot fit one cutoff of support \(Nn\le2Z_J\).
Each of the \(J\) factors must therefore contain exactly one \(p_i\).
Since the first nonunit good ideal has norm at least seven, no factor
can contain an additional good ideal. Thus \(t=1\),
\(\lambda_J(x)=(-1)^JJ!\), and \(\lambda_j(tx)=0\) for \(j<J\).
On retained \((x,y)=1\), the last binomial sign consequently gives
the coefficient \(-J!\tau_{J-1}(y)\). Such a prime-norm subwindow
may be chosen inside the original annulus; \(Nx\asymp D\).

In the unreflected full balanced block with free unit factors,
one short-inverse second moment and absolute bounds for the other
actual Möbius factors give the method cost
\[
 U D^{1-1/J},\qquad
 1+r(1-1/J)=
 \begin{cases}123211/78800,&J=2,\\103511/59100,&J=3,\end{cases}
 \quad(r=44411/39400).
\]
Both exceed the required \(261061/236400\); these are upper-bound
costs, not source lower bounds. Higher order raises this unpaid
prime face, while \(\tau_{j-1}(ty)\) couples the common factor to the
dual output and prevents reusing HR.5's independent harmonic sums.
Cross-\(j\) packets have different root powers, gamma kernels and
ratio scales and must remain in the whole source. Their possible
signed cancellation is not ruled out. No full-source impossibility,
new gain, target, paper or engine follows from this check.
