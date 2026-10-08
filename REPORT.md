# A quantitative refinement of the seven-eighths zero-free half-plane

**Zhongpai Gao — 7 October 2026. Draft; independent review pending.**

The [manuscript](report.pdf) builds on OpenAI's released cubic-theta proof of
a zero-free half-plane. It claims the slightly stronger boundary

$$
\Re s>\theta,\qquad
\theta=\frac{20999}{24000}=\frac78-\frac1{24000}.
$$

The same family is covered: every Dirichlet $L$-function and every
finite-order Hecke $L$-function over $\mathbb Q(\sqrt{-3})$, including
imprimitive presentations. Principal poles at one are allowed. The boundary
is independent of conductor and height, although intermediate estimate
constants and thresholds may depend on the target.

## Where the improvement comes from

The construction has a low estimate and a principal contribution. A
contradiction becomes possible when the principal contribution exceeds the
low estimate, provided every other row and every recovery cost have been
paid. The refinement changes the averaging scales while retaining the
original arithmetic coefficients and moment inputs.

Set

$$
p=1/6000,\quad \ell=1/6+p,\quad h=13/16+3p/2,
\quad l_x=17/48-p/2,\quad l_y=23/48-p/2.
$$

The principal exponent remains $C(s)=s-11/16$. The complete low estimate
becomes $Z^{3/16-p/4+\varepsilon}$, including every marked and rescaled
term. Their crossing is therefore $\theta=7/8-p/4$.

The high rows require a sharper calculation. Instead of replacing the
balanced row estimate by a uniform perturbation loss, the proof retains its
two endpoint variables. For its relative exponent $E_p$, an exact identity
gives

$$
10368J(-E_p-m)=A\delta^2+B\delta+C,
\qquad m=1/200000,
$$

where $J>0$, $A>0$, and $4AC-B^2>0$ throughout the required parameter
rectangle. The last inequality follows from a polynomial with positive
rational coefficients. Completing the square proves $E_p\le-m$.
[The certificate](endpoint_certificate.py) checks these identities with exact
arithmetic; no numerical grid or random-sign assumption supplies the margin.

The manuscript then pays the contour shifts, finite Euler corrections,
normalizer, height cutoffs and outer tails at the new scales. The retained
margin permits continuation of the same common signal. Finite Euler factors
restore imprimitive Hecke presentations. The norm-lift product identity
transfers Hecke nonvanishing to Dirichlet functions.

## Evidence and limits

Three kinds of evidence should be distinguished. The arithmetic script
certifies the displayed endpoint identities. The manuscript gives the
analytic argument and identifies its substantial unchanged OpenAI inputs.
The archive preserves a completed formal build: declarations for the Hecke
supremum, Hecke family, Dirichlet family and standard zeta compiled; separate
target comparison and default-kernel replay were performed for standard zeta
only. Its axiom record lists `propext`, `Classical.choice` and `Quot.sound`.
The package audit checks those records and their hashes; it runs no new Lean
proof and does not replace independent review of the analytic interfaces.

The gain is small. With the fixed skew and unchanged balanced witness
estimate, the loss-free crossing cannot be pushed below approximately
$0.8749572006$. This is a limit of that inequality, not a limit on other
arithmetic methods. Further progress requires a genuinely stronger row
estimate. The draft makes no claim to RH, priority or external certification.

The source version and attribution are recorded in
[PROVENANCE.json](PROVENANCE.json).
