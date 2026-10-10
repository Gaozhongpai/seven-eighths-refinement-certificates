# Method comparison and possible combinations

**9 October 2026.** This package gives a conditional proof at
`2187392879/2500000000 = 0.8749571516`. It is numerically weaker than
the refinements currently listed by
[QRH Bounds](https://gtimg.github.io/QuasiRiemannTracker/).
The comparison below concerns mathematical estimates and their inputs;
it makes no priority claim.

## Where the adaptive arguments overlap

Both arguments use OpenAI's cubic-theta probe, its reciprocal Mellin
signal, reflection, detector moments and all-character transfer.
Our companion and ProofCouncil's development both extend the plain
moment below `kappa = 3/4`, down to `13/18`, under the family condition
`beta_* <= (1+kappa)/2`, retaining the masks, zeros and recovery costs.

| Step | This package | ProofCouncil |
| --- | --- | --- |
| Short inverse capacity | `(1-r)/2` | Same |
| Doubled plain capacity | `(1-2m)/(6*kappa)` | Same |
| Long inverse slope | `5/6` | Same |
| Witness crossing | `R_* = 1-delta + (5/6-delta)*delta*P/(2*J)` | Same |
| Choice of `kappa` | Previous established boundary; two finite steps | Dynamic family supremum, with its losses paid |
| Asymmetry | Fixed `b = 1/8` | Jointly optimized, approximately `0.1234056854` |

The matching formulas occur in our main paper's adaptive section and
companion, and in ProofCouncil's
[manuscript](https://github.com/GTimG/QuasiRiemannTracker/blob/40844a7614b67840801e65b836b3da2e1f7ff029/public/proofs/qrh-20261009/accepted-answer.tex),
especially its geometry, adaptive count and restricted exponent program.
The tracker publishes a separate
[proof map](https://github.com/GTimG/QuasiRiemannTracker/blob/40844a7614b67840801e65b836b3da2e1f7ff029/proofs/qrh-20261009/audit/DEPENDENCY_MAP.md).
Its OpenAI source pin differs from ours; this is a comparison of the
stated formulas and mathematical inputs, not a byte-identity assertion.

**The boundary gains cannot be added.** Our adaptive steps and the
tracker's optimization reuse the same capacity improvement. Adding their
numerical decrements would count that improvement twice. Jointly
optimizing these ingredients is legitimate, but the broader optimization
has already been carried out in the cited development.

## Different arithmetic inputs

The following research notes are separate from the adaptive paper.
Their proofs have internal model-assisted review; independent specialist
and priority reviews remain pending.

| Input | Proved scope in the note | What a combination still needs |
| --- | --- | --- |
| [Harmonic Mobius recovery](methods/harmonic_mobius_ratio_recovery.md), HR.8 | A growing nonprincipal reduced-numerator sector has energy `UX(X/D)^(1/4)`, at the stated profile and height costs | The larger reduced numerators, including balanced prime pairs, remain; this does not replace the complete long inverse moment |
| [Hybrid character moment](methods/hybrid_character_moment.md), HC.2–3 and HC.12 | Dense smooth squarefree columns and unrestricted sextic rows; angular order zero is included with its principal contribution | The native child is a mixed fourth moment with live outer prime slots; a single-column estimate does not enlarge that capacity |

HC.12 retains the principal cost `sqrt(K)*B^2` in the general frequency
range. Ordinary recovery and Cauchy–Schwarz give a balanced fourth-moment
upper cost `K^(359/256+epsilon)`, exceeding the desired `K^(1+epsilon)`.
That is the cost of this estimation method, not a lower bound for the
true signed source.

A successful combination must first prove an improved estimate for the
complete original inverse source, or for the mixed fourth moment, keeping
the masks, selected profiles and heights, residue terms and finite caps.
One can then recompute the detector count and the joint geometry.
No such complete extra gain has been established in this package.

## External comparison and evidence

The [reference snapshot](evidence/external_tracker_comparison.json)
records exact rational boundaries and their *reported* verification
statuses at tracker commit `40844a7614b67840801e65b836b3da2e1f7ff029`.
ProofCouncil reports `0.874957019421`; Nielstron's later tightening is
`0.874957019420098946128604623`, a change of about `9.01e-13` within
the existing argument. Its later
[three-kernel report](https://github.com/GTimG/QuasiRiemannTracker/blob/40844a7614b67840801e65b836b3da2e1f7ff029/public/proofs/nielstron-20261009-kernels/result.json)
records acceptance after the historical author-side report that still
said verification was pending. We did not rerun those checks.

The cited restricted program has a zero-margin boundary near
`0.87495701942009894612860385`. This is a limitation of that program,
not a lower bound for all possible zero-free arguments or an obstruction
to RH. Our fixed-asymmetry limit `0.87495715035054` is a narrower,
different parameter restriction.

Our stronger adaptive boundary has no new kernel replay. The historical
replayed standard-zeta boundary remains `20999/24000`; the conventional
full-family statement retains the named OpenAI inputs as hypotheses.
Publication here is not tracker admission or external mathematical review.
