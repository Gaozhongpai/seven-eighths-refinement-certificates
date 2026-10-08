# Historical verification records

These files preserve the 7 October 2026 verification run. The release checks
their hashes and internal agreement; they do not execute Lean.

| Record | Meaning |
|---|---|
| `next_strip_verification_result.json` | Completed standard-zeta target comparison and default-kernel replay |
| `next_zeta_comparator.log` | Successful comparison and kernel-acceptance log |
| `next_target_build.log` | Successful build, including the closed Hecke and Dirichlet declarations |
| `next_target_axioms.log` | Printed standard-zeta statement and its three permitted axioms |
| `conditional_negative_control_*` | Rejection of a statement with an extra old-half-plane premise |
| `*_source_manifest.json` | Agreeing hashes of the 117 extension sources used in the historical run |

The common boundary is `20999/24000`. Separate target comparison and kernel
replay were performed for standard zeta. The Hecke and Dirichlet declarations
compiled; separate Comparator runs for them are not recorded.

The `sorry` in the Comparator log belongs to its challenge placeholder, not
the accepted solution. The printed final target depends only on `propext`,
`Classical.choice` and `Quot.sound`. The analytic principal pole at one is
allowed; Mathlib assigns an auxiliary nonzero value there.

Some JSON fields retain historical `/tmp` log locations. Those locations are
provenance and are not needed to run this repository's checks.
The proof sources and upstream workspace are not bundled. Their original
archive is linked from the [research repository](https://github.com/Gaozhongpai/RH/tree/main/framework/programs/fixed_strip/verification/geometry_endpoint_verification_2026-10-07).
