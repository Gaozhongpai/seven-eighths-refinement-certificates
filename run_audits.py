#!/usr/bin/env python3
"""Check the release snapshot, exact endpoint, and historical record consistency.

This program reads the supplied files. It does not run a proof kernel or
establish the analytic estimates in the manuscript.
"""

from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
PIN = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
TARGET = "OpenAINextStripAttempt.StrongerResult.zeta_nonzero"
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def check_snapshot():
    """Verify each packaged file against the published snapshot digest."""
    seen = set()
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, separator, name = line.partition("  ")
        require(separator and re.fullmatch(r"[0-9a-f]{64}", digest),
                "Malformed SHA256SUMS row")
        path = ROOT / name
        require(path.resolve().is_relative_to(ROOT), "Path escapes repository")
        require(name not in seen, f"Duplicate checksum entry: {name}")
        require(path.is_file(), f"Missing packaged file: {name}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual == digest, f"Snapshot hash mismatch: {name}")
        seen.add(name)
    require(seen, "Empty snapshot manifest")
    required = {
        "report.pdf", "paper/report.tex", "README.md", "REPORT.md",
        "PROVENANCE.json", "endpoint_certificate.py", "endpoint_certificate.json",
        "run_audits.py", "evidence/next_strip_verification_result.json",
        "adaptive_endpoint_certificate.py", "adaptive_endpoint_certificate.json",
        "seven_eighths_adaptive_moment.pdf", "paper/seven_eighths_adaptive_moment.tex",
        "METHOD_COMPARISON.md", "evidence/external_tracker_comparison.json",
        "methods/harmonic_mobius_ratio_recovery.md", "methods/hybrid_character_moment.md",
    }
    require(required <= seen, "Release manifest is incomplete")
    print(f"Snapshot integrity: PASS ({len(seen)} files)", flush=True)


def printed_axioms(text):
    pairs = re.findall(
        r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", text, re.S
    )
    return {name: {item.strip() for item in body.split(",")} for name, body in pairs}


def check_method_comparison():
    """Check reference arithmetic; reported external statuses are not replayed."""
    data = read_json("evidence/external_tracker_comparison.json")
    ours = Fraction(data["our_boundary"])
    require(ours == Fraction(2187392879, 2500000000), "Comparison boundary differs")
    refs = {row["id"]: row for row in data["records"]}
    require(len(refs) == len(data["records"]) == 5, "Reference IDs changed")
    for row in refs.values():
        reference = Fraction(row["theta"])
        require(ours-reference == Fraction(row["our_boundary_minus_reference"]),
                f"Reference difference is incorrect: {row['id']}")
    tighter = Fraction(refs["nielstron-20261009-tightening"]["theta"])
    council = Fraction(refs["proofcouncil-20261009"]["theta"])
    require(tighter < council < ours < Fraction(7, 8), "Reference ordering differs")
    ell = Fraction(11, 3)-4*tighter
    require(Fraction(1, 6) < ell < Fraction(1, 5)
            and 657*ell**3-954*ell**2+21*ell+20 > 0,
            "Reference rational does not have the stated strict cubic margin")
    require(data["additional_stacked_gain_proved"] is False
            and data["runs_Lean"] is False, "Reference scope was relabelled")
    print("Method comparison: PASS (exact reference arithmetic; no external replay)",
          flush=True)


def check_historical_records():
    """Check agreement between archived records; do not replay their proofs."""
    result = read_json("evidence/next_strip_verification_result.json")
    require(result["status"] == "PASS_NEXT_STANDARD_ZETA", "Unexpected archive status")
    require(result["target"] == TARGET and result["theta"] == "20999/24000",
            "Archived target differs from the recorded first-stage boundary")
    require(result["source_pin"] == PIN, "Wrong upstream source pin")
    require(result["default_Lean_kernel_replay"] is True,
            "Archive does not record default-kernel acceptance")
    require(result["extra_target_premises_allowed"] is False,
            "Archive permits an extra target premise")
    require(result["upstream_sources_unchanged"] == 3271
            and result["new_sources_unchanged"] is True,
            "Unexpected historical source-integrity record")
    for field in ("target_build_exit_code", "comparator_exit_code", "axiom_print_exit_code"):
        require(type(result[field]) is int and result[field] == 0,
                f"Archived command failed: {field}")

    evidence = ROOT / "evidence"
    comparator = (evidence / "next_zeta_comparator.log").read_text(encoding="utf-8")
    require("Lean default kernel accepts the solution" in comparator
            and "Your solution is okay!" in comparator,
            "Archived Comparator success markers missing")
    axiom_log = (evidence / "next_target_axioms.log").read_text(encoding="utf-8")
    require(printed_axioms(axiom_log).get(TARGET) == AXIOMS,
            "Archived zeta axiom closure differs")
    build = (evidence / "next_target_build.log").read_text(encoding="utf-8")
    require("Build completed successfully (7177 jobs)." in build,
            "Archived targeted build completion missing")
    family = printed_axioms(build)
    for name in ("beta_le_theta", "hecke_nonzero", "dirichlet_nonzero", "zeta_nonzero"):
        require(family.get("OpenAINextStripAttempt.StrongerResult." + name) == AXIOMS,
                f"Archived declaration/axiom record missing: {name}")

    control = read_json("evidence/conditional_negative_control_result.json")
    require(type(control["exit_code"]) is int and control["exit_code"] != 0
            and control["expected_rejection"] is True,
            "Extra-premise control was not rejected")
    rejection = (evidence / "conditional_negative_control_comparator.log").read_text(
        encoding="utf-8"
    )
    require("theorem statement do not match" in rejection,
            "Extra-premise rejection marker missing")

    manifest = read_json("evidence/proof_source_manifest.json")
    historical = read_json("evidence/next_strip_verification_source_manifest.json")
    recorded = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
    require(len(recorded) == len(manifest["files"]) == 117,
            "Unexpected extension source-manifest size")
    require(recorded == historical["new_source_sha256"],
            "Historical extension manifests disagree")
    require(historical["upstream_pin"] == manifest["upstream_source_pin"] == PIN,
            "Historical manifests disagree on upstream pin")
    print("Historical records: PASS (zeta replay; family compilation; rejected control)",
          flush=True)
    print("Proof sources are referenced by these manifests and are not bundled here.",
          flush=True)


def main():
    check_snapshot()
    subprocess.run([sys.executable, str(ROOT / "endpoint_certificate.py"), "--check"],
                   cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / "adaptive_endpoint_certificate.py"), "--check"],
                   cwd=ROOT, check=True)
    provenance=read_json("PROVENANCE.json")
    adaptive=read_json("adaptive_endpoint_certificate.json")
    require(provenance["boundary"]==adaptive["manuscript_boundary"],
            "Manuscript provenance and adaptive endpoint differ")
    require(provenance["archived_verified_boundary"]=="20999/24000",
            "Adaptive update must not relabel archived formal evidence")
    check_historical_records()
    check_method_comparison()
    print("All release checks passed. No Lean or kernel replay was run.")


if __name__ == "__main__":
    main()
