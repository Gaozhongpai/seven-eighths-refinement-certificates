# Seven-eighths refinement certificates

A draft paper and reproducible certificates accompanying Zhongpai Gao's
*A quantitative refinement of the seven-eighths zero-free half-plane*.

Conditional on the named inputs from OpenAI's unrefereed preprint, the
current main theorem gives

$$
\Re s>\theta_*=\frac{2187392879}{2500000000}=0.8749571516.
$$

It covers all Dirichlet $L$-functions and all finite-order Hecke
$L$-functions over $\mathbb Q(\sqrt{-3})$, including imprimitive
presentations, with principal poles at one allowed. The boundary is
independent of conductor and height; intermediate constants and thresholds
may depend on the fixed target.

Read the [19-page main paper](report.pdf), its
[10-page recursive moment proof](seven_eighths_adaptive_moment.pdf), or the
[short technical report](REPORT.md). The 9 October revision incorporates
the complete adaptive argument into the main theorem. This remains an
unsubmitted, unranked draft; independent human specialist and priority
reviews are pending. It does not prove RH.

The bound is superseded numerically by refinements listed on
[QRH Bounds](https://gtimg.github.io/QuasiRiemannTracker/).
Our adaptive plain-moment extension overlaps ProofCouncil's argument;
the improvements cannot be added. See the
[method comparison](METHOD_COMPARISON.md) for the matching formulas,
different arithmetic inputs and remaining recovery requirements.

The archived standard-zeta target/kernel evidence remains at
$20999/24000$. The stronger adaptive theorem has a conventional proof,
conditional on the stated inputs, with no new formal replay.

## Check the package

Python 3.10 or later is sufficient; all audits use the standard library.
From the repository root, run:

```sh
python3 run_audits.py
```

This checks release hashes, both exact endpoint certificates and agreement
between the historical records. It runs no Lean and does not independently
verify the analytic moment or continuation proofs.

| File | Purpose |
| --- | --- |
| [report.pdf](report.pdf) | Current main manuscript. |
| [seven_eighths_adaptive_moment.pdf](seven_eighths_adaptive_moment.pdf) | Full recursive plain-moment proof and witness count; part of the same paper. |
| `paper/report.tex`, `paper/sections/` | Main TeX sources. |
| `paper/seven_eighths_adaptive_moment.tex`, `paper/adaptive_sections/` | Supplementary TeX sources. |
| [endpoint_certificate.py](endpoint_certificate.py), [JSON](endpoint_certificate.json) | Original first-stage endpoint and retained-bound limitation. |
| [adaptive_endpoint_certificate.py](adaptive_endpoint_certificate.py), [JSON](adaptive_endpoint_certificate.json) | Two finite adaptive stages and the rational coefficient bounds printed in the paper. |
| [run_audits.py](run_audits.py) | One-command arithmetic and archive checks. |
| [METHOD_COMPARISON.md](METHOD_COMPARISON.md) | Overlap with contemporary refinements, exact reference boundaries and limits on combining the methods. |
| [Harmonic recovery](methods/harmonic_mobius_ratio_recovery.md) | A growing reduced-numerator sector; its complement remains open. |
| [Hybrid character moment](methods/hybrid_character_moment.md) | Full smooth squarefree columns, including finite-order characters with the principal contribution retained. |
| `evidence/` | Historical first-stage build, axioms, zeta comparison, negative control and source manifests. |
| [PROVENANCE.json](PROVENANCE.json), [SHA256SUMS](SHA256SUMS) | Source attribution and snapshot integrity. |

Each certificate supports `--check` (also the default) and explicit
regeneration with `--write`.

## External inputs and archived evidence

The input is OpenAI's
[30 September 2026 preprint](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
pinned at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
Its Theorem 1.1 and the named reused statements are explicit hypotheses,
not independently certified by this package.

The recorded first-stage proof build compiled the Hecke-supremum, Hecke,
Dirichlet and standard-zeta declarations. Separate target comparison and
default-kernel replay covered standard zeta only. These records concern
$20999/24000$, not the adaptive boundary. The upstream proof sources are
identified by provenance rather than vendored here.

The two arithmetic research notes are outside the main manuscript. They
have internal model-assisted review, with independent specialist and
priority reviews pending. Their parent-repository finite audits are not
bundled here. The release checks do not certify their analytic proofs or
establish an additional fixed-strip gain.

## Build the PDFs

With Tectonic installed:

```sh
mkdir -p build
cd paper
tectonic --outdir ../build report.tex
tectonic --outdir ../build seven_eighths_adaptive_moment.tex
```

The outputs are `build/report.pdf` and
`build/seven_eighths_adaptive_moment.pdf`. The checked-in copies identify
the manuscript version accompanying the certificates.

## Citation and license

[Citation metadata](CITATION.cff) identify the draft. Include the manuscript
version and repository commit when citing this work.

The author's certificate code and repository documentation use the
[MIT License](LICENSE). The manuscript retains the author's copyright;
third-party and historical evidence retain their original terms.
