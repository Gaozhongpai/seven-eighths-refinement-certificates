# Seven-eighths refinement certificates

A draft paper and reproducible certificates accompanying Zhongpai Gao's
*A quantitative refinement of the seven-eighths zero-free half-plane*.

The draft refines the boundary in OpenAI's cubic-theta argument from
$7/8$ to

$$
\theta=\frac{20999}{24000}=\frac78-\frac1{24000}.
$$

Its theorem covers all Dirichlet $L$-functions and all finite-order Hecke
$L$-functions over $\mathbb Q(\sqrt{-3})$, including imprimitive
presentations. Principal poles at $s=1$ are allowed. The boundary is
independent of conductor and height; constants and thresholds in intermediate
estimates may depend on the fixed target.

Read the [12-page paper](report.pdf) or the shorter [technical report](REPORT.md).
This is an unsubmitted draft; independent mathematical and priority review
remain pending. It does not prove RH.

## Check the package

The audits require Python 3.10 or later and use only the standard library.
From the repository root, run:

```sh
python3 run_audits.py
```

This checks the release hashes, recomputes the exact endpoint certificate and
checks consistency of the archived verification records. It does not run Lean
or independently establish the analytic estimates in the paper.

| File | Purpose |
| --- | --- |
| [report.pdf](report.pdf) | The current manuscript. |
| [paper/report.tex](paper/report.tex), `paper/sections/` | Editable, standalone TeX sources. |
| [endpoint_certificate.py](endpoint_certificate.py) | Exact rational endpoint identities and the retained-bound limitation. |
| [endpoint_certificate.json](endpoint_certificate.json) | The certificate checked against those identities. |
| [run_audits.py](run_audits.py) | One-command arithmetic and archive checks. |
| `evidence/` | Historical build, axiom, zeta target-comparison, negative-control and source-manifest records. |
| [PROVENANCE.json](PROVENANCE.json), [SHA256SUMS](SHA256SUMS) | Source attribution and release integrity. |

For the arithmetic check alone, run `python3 endpoint_certificate.py --check`;
`--check` is also the default. Use `--write` to regenerate its JSON output.

## What the archived evidence establishes

The Hecke-supremum, Hecke, Dirichlet and standard-zeta declarations compiled in
the recorded proof build. Separate target comparison and default-kernel replay
were performed for standard zeta only. This package preserves those completed
records; its audits perform no new formal proof execution. OpenAI's proof
sources are identified by provenance rather than vendored here.

The external input is OpenAI's
[30 September 2026 preprint](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
pinned at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

## Build the paper

With [Tectonic](https://tectonic-typesetting.github.io/) installed:

```sh
mkdir -p build
cd paper
tectonic --outdir ../build report.tex
```

The output is `build/report.pdf`. The checked-in `report.pdf` records the
manuscript version accompanying these certificates.

## Repository

Repository: [seven-eighths-refinement-certificates](https://github.com/Gaozhongpai/seven-eighths-refinement-certificates).

For later updates to this checkout:

```sh
git push origin main
```

## Citation and license

Citation metadata are in [CITATION.cff](CITATION.cff). Identify the manuscript
version and repository commit when citing this work.

The author's certificate code and repository documentation use the
[MIT License](LICENSE). The manuscript retains the author's copyright;
third-party and historical evidence retain their original terms.
