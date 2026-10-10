# A quantitative refinement of the seven-eighths zero-free half-plane

**Zhongpai Gao — revised 9 October 2026. DRAFT; unsubmitted and unranked.**

The [main paper](report.pdf) and [companion proof](seven_eighths_adaptive_moment.pdf)
give, conditional on the named inputs from OpenAI's September preprint,

$$
\Re s>\theta_*=\frac{2187392879}{2500000000}=0.8749571516.
$$

The assertion covers every Dirichlet $L$-function and every finite-order
Hecke $L$-function over $\mathbb Q(\sqrt{-3})$, including imprimitive
presentations, with principal poles at one allowed. Its boundary is
independent of conductor and height; estimate constants and thresholds
may depend on the target.

## The three stages

The construction compares one cubic-theta character sum with a common
Mellin signal containing $1/L$. A direct estimate contradicts the signal
only after every other row, residue and recovery cost has been paid.
The argument uses this construction throughout.

| Stage | Input | Change | Output boundary |
| --- | --- | --- | --- |
| First refinement | OpenAI's $7/8$ theorem and named estimates | Averaging perturbation $p=1/6000$; exact LOW, endpoint and recovery | $\theta_0=20999/24000$ |
| First adaptive step | Established $\theta_0$ | Plain capacity $\kappa_0=2\theta_0-1$; $p_1=1/5836$ | $\theta_1=20425/23344$ |
| Second adaptive step | Established $\theta_1$ | $\kappa_1=2\theta_1-1$; $p_2=107121/625000000$ | $\theta_*=2187392879/2500000000$ |

The first stage retains the original moment range. The companion extends
the plain moment to $13/18\le\kappa\le3/4$ under the global input
$\beta_*\le(1+\kappa)/2$. It proves admission of every recursive child,
keeps the common masks and character zeros, and allocates mesh, slot and
height losses in their required order. The actual witness count retains
both length inequalities and all complementary branches.

At each adaptive step the prime contour uses the preceding established
boundary. It never uses its own output. These are two finite steps, not an
infinite iteration or an improved long inverse moment.

## Exact endpoints and full recovery

For $\delta=2a-1$, $x\in[0,1/2]$, $y=1/2-x$ and $c=1/(3\kappa)$,
put $D=5/2-c+(1+2c)y$, $P=1-c/2+2y+2cy^2$ and
$\mathcal J=(5/6-\delta)D+\delta P$. The central relative exponent is

$$
E_p=-1/48+(2/3)\delta+\delta x/6-(13/16)(1-R_*)
+p\{-1/4+\delta(1+x)+(3/2)R_*\},
\quad R_*=1-\delta+\frac{(5/6-\delta)\delta P}{2\mathcal J}.
$$

Exact multiplication gives
$2\mathcal J(-E_p-m)=A\delta^2+B\delta+C$.
The coefficients of $A$ and $4AC-B^2$ satisfy the positive rational
bounds printed in the paper, so completing the square proves
$E_p<-m$ everywhere on the endpoint rectangle.
The two margins are $10^{-8}$ and $10^{-9}$.
[The adaptive certificate](adaptive_endpoint_certificate.py) independently
expands the literal exponent and compares these identities; it uses no
sampling or floating-point fit.

The main proof pays the Euler correction, residues, normalization, heights
and outer tails at both sets of scales. The small-row contour stays at
$7/8+8e$, with its additional shift cost explicitly charged. The resulting
common positive reserve gives all-height family continuation. Finite Euler
restoration covers induced presentations, and the norm-lift product
identity gives the Dirichlet assertion.

## Evidence and scope

The main and supplementary proofs retain the named OpenAI inputs as
hypotheses. Internal source review and PDF compilation are not independent
human refereeing or priority clearance. The exact scripts certify endpoint
algebra, not these analytic inputs.

The archived formal evidence covers $20999/24000$: family declarations
compiled, while separate target comparison and default-kernel replay
covered standard zeta only. No new Lean or kernel execution accompanies
the stronger adaptive theorem.

For fixed asymmetry $b=1/8$, the parameter ceiling at $\kappa=3/4$
is about $0.8749572006$.
Finite adaptive feedback approaches the loss-free value
$0.87495715035054$, which is not asserted as a theorem. The current gain
is small; reaching $0.8749$ requires an additional actual arithmetic
estimate. New character-moment tools and unresolved inverse covariance
research are outside this manuscript.

## Comparison with contemporary refinements

The [method comparison](METHOD_COMPARISON.md) records the overlap with
ProofCouncil's extended plain moment and witness balancing. That work
also optimizes the asymmetry, and its reported boundary is smaller than
ours. Nielstron's further tightening uses the same argument's remaining
numerical slack. These gains are not independent quantities that can be
added to the finite adaptive steps above. No priority or best-bound
claim is made here.

The separate [harmonic recovery](methods/harmonic_mobius_ratio_recovery.md)
and [hybrid character moment](methods/hybrid_character_moment.md) may be
inputs to a future combined argument. Their present scopes leave an
unpaid inverse complement or mixed fourth moment, respectively; no
complete extra gain has been proved.

[Provenance](PROVENANCE.json) records the pinned sources and snapshot hashes.
No journal submission or external certification is claimed.
