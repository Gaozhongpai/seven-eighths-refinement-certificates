#!/usr/bin/env python3
"""Check the report's endpoint algebra using exact rational arithmetic.

Run ``python3 endpoint_certificate.py`` to check the stored certificate.
Run ``python3 endpoint_certificate.py --write`` to regenerate it explicitly.

This checks exponent identities and positivity after the analytic estimates
in the report have been supplied. It does not prove those estimates, transfer
an L-function theorem to a family, or run a proof kernel.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path
import sys


# A key (i, j) denotes the coefficient of delta**i * y**j.
Polynomial = dict[tuple[int, int], F]
ZERO = F(0)
ALPHA = F(5, 6)
PERTURBATION = F(1, 6000)
MARGIN = F(1, 200000)
CERTIFICATE = Path(__file__).with_name("endpoint_certificate.json")


class CertificateError(ValueError):
    """An exact identity, sign, or stored result failed to check."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def constant(value: F | int) -> Polynomial:
    value = F(value)
    return {(0, 0): value} if value else {}


def polynomial(coefficients: dict[tuple[int, int], F | int]) -> Polynomial:
    return {key: F(value) for key, value in coefficients.items() if value}


def add(*terms: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for term in terms:
        for key, value in term.items():
            result[key] = result.get(key, ZERO) + value
    return {key: value for key, value in result.items() if value}


def scale(term: Polynomial, scalar: F | int) -> Polynomial:
    scalar = F(scalar)
    return {key: value * scalar for key, value in term.items() if value * scalar}


def multiply(*terms: Polynomial) -> Polynomial:
    result = constant(1)
    for term in terms:
        product: Polynomial = {}
        for (i, j), value in result.items():
            for (k, l), other in term.items():
                key = (i + k, j + l)
                product[key] = product.get(key, ZERO) + value * other
        result = {key: value for key, value in product.items() if value}
    return result


def evaluate(term: Polynomial, delta: F, y: F) -> F:
    return sum(
        (coefficient * delta**i * y**j for (i, j), coefficient in term.items()),
        ZERO,
    )


def serialize(term: Polynomial) -> list[dict[str, int | str]]:
    return [
        {"delta_power": i, "y_power": j, "coefficient": str(coefficient)}
        for (i, j), coefficient in sorted(term.items())
    ]


DELTA = polynomial({(1, 0): 1})
Y = polynomial({(0, 1): 1})
X = add(constant(F(1, 2)), scale(Y, -1))
A_PARAMETER = scale(add(constant(1), DELTA), F(1, 2))


@dataclass(frozen=True)
class Geometry:
    p: F
    b: F
    ell: F
    h: F
    lx: F
    ly: F
    mass: F
    theta: F

    @classmethod
    def at(cls, p: F) -> Geometry:
        return cls(
            p=p,
            b=F(1, 8),
            ell=F(1, 6) + p,
            h=F(13, 16) + 3 * p / 2,
            lx=F(17, 48) - p / 2,
            ly=F(23, 48) - p / 2,
            mass=F(5, 6) - p,
            theta=F(7, 8) - p / 4,
        )


def count_polynomials() -> tuple[Polynomial, Polynomial, Polynomial, Polynomial]:
    """Return D_x, P_x, J, and the numerator 2J R_*.

    Keeping the denominator symbolic lets every following comparison use
    integer/Fraction coefficients, without sampling the parameter rectangle.
    """
    dx = polynomial({(0, 0): F(37, 18), (0, 1): F(17, 9)})
    px = polynomial({(0, 0): F(7, 9), (0, 1): 2, (0, 2): F(8, 9)})
    alpha_minus_delta = add(constant(ALPHA), scale(DELTA, -1))
    j = add(multiply(alpha_minus_delta, dx), multiply(DELTA, px))
    r_numerator = add(
        scale(multiply(j, add(constant(1), scale(DELTA, -1))), 2),
        multiply(alpha_minus_delta, DELTA, px),
    )
    published_j = scale(
        polynomial({(0, 0): 185, (0, 1): 170, (1, 0): -138,
                    (1, 1): 12, (1, 2): 96}),
        F(1, 108),
    )
    require(j == published_j, "The two expressions for J differ.")
    return dx, px, j, r_numerator


def endpoint_polynomial(p: F, margin: F) -> tuple[Polynomial, Polynomial]:
    """Derive Q = 10368 J (-E_theta(h) - margin) from the row exponent.

    The first computation uses the literal Mellin/slot exponent in the
    report. The second uses its independently written E_0 + p correction.
    Their equality is checked before extracting any displayed coefficients.
    """
    geometry = Geometry.at(p)
    _, _, j, r_numerator = count_polynomials()
    twice_j = scale(j, 2)
    q_amplitude = multiply(DELTA, X)
    z_line = F(17, 50)

    # E_theta(h) = a - theta + h(z_line - 1/6) - a*l_y - ell/2
    #              + q*ell + h(R_* + delta/2 - z_line).
    without_r = add(
        A_PARAMETER,
        constant(-geometry.theta + geometry.h * (z_line - F(1, 6))),
        scale(A_PARAMETER, -geometry.ly),
        constant(-geometry.ell / 2),
        scale(q_amplitude, geometry.ell),
        scale(add(scale(DELTA, F(1, 2)), constant(-z_line)), geometry.h),
    )
    literal_numerator = add(
        multiply(twice_j, without_r), scale(r_numerator, geometry.h)
    )

    # E_0 = -1/48 + 2 delta/3 + delta*x/6 - (13/16)(1-R_*).
    # E_theta(h) = E_0 + p(-1/4 + delta(1+x) + 3R_*/2).
    e0_without_r = add(
        constant(-F(1, 48) - F(13, 16)),
        scale(DELTA, F(2, 3)),
        scale(q_amplitude, F(1, 6)),
    )
    perturbation_without_r = add(
        constant(-F(1, 4)), multiply(DELTA, add(constant(1), X))
    )
    alternative_numerator = add(
        multiply(twice_j, add(e0_without_r, scale(perturbation_without_r, p))),
        scale(r_numerator, F(13, 16) + 3 * p / 2),
    )
    require(literal_numerator == alternative_numerator,
            "The literal high exponent and E_0+p expression differ.")
    q = scale(add(literal_numerator, scale(twice_j, margin)), -5184)
    return j, q


def check_interval_bounds() -> dict[str, object]:
    """Certify J's bounds by exact factorizations on the closed rectangle."""
    dx, px, j, _ = count_polynomials()
    require(add(constant(3), scale(dx, -1)) ==
            scale(add(constant(1), scale(Y, -2)), F(17, 18)),
            "D_x upper-bound factorization failed.")
    require(add(constant(2), scale(px, -1)) ==
            scale(multiply(add(constant(1), scale(Y, -2)),
                           add(constant(11), scale(Y, 4))), F(1, 9)),
            "P_x upper-bound factorization failed.")
    require(all(value >= 0 for value in add(dx, constant(-F(37, 18))).values()),
            "D_x lower-bound coefficients failed.")
    require(all(value >= 0 for value in add(px, constant(-F(7, 9))).values()),
            "P_x lower-bound coefficients failed.")
    require(j == add(multiply(add(constant(ALPHA), scale(DELTA, -1)), dx),
                     multiply(DELTA, px)), "J convex-combination identity failed.")
    # Nonnegative weights sum to alpha on 0 <= delta <= alpha. Hence
    # J >= alpha*(7/9), and J <= alpha*3. This also gives t_* in [1,3/2].
    require(ALPHA * F(7, 9) == F(35, 54), "J lower bound failed.")
    require(ALPHA * 3 == F(5, 2), "J upper bound failed.")
    return {
        "parameter_rectangle": {"delta": ["0", str(ALPHA)], "y": ["0", "1/2"]},
        "D_x_bounds": ["37/18", "3"],
        "P_x_bounds": ["7/9", "2"],
        "J_bounds": ["35/54", "5/2"],
        "proof": "J=(5/6-delta)D_x+delta P_x; both weights are nonnegative.",
        "upper_bound_factorizations": [
            "3-D_x=17(1-2y)/18", "2-P_x=(1-2y)(11+4y)/9"
        ],
        "balanced_cutoff_bounds": ["1", "3/2"],
    }


def check_geometry() -> dict[str, object]:
    geometry = Geometry.at(PERTURBATION)
    require(geometry.mass + geometry.ell == 1, "M+ell=1 failed.")
    require(geometry.lx + geometry.ly == geometry.mass, "l_x+l_y=M failed.")
    require(geometry.ly - geometry.lx == geometry.b, "Fixed skew failed.")
    require(geometry.h == 1 - geometry.lx + geometry.ell, "Frequency geometry failed.")
    principal_constant = -F(5, 6) + geometry.lx / 3 + geometry.ell / 6
    require(principal_constant == -F(11, 16), "Principal exponent changed.")
    low = geometry.lx / 2 + geometry.b / 12
    require(low == geometry.theta + principal_constant,
            "The LOW exponent does not cross C(theta).")
    require(low == F(3, 16) - PERTURBATION / 4, "The LOW decrease differs.")
    margins = {
        "rescaled_X": geometry.lx - geometry.ell,
        "rescaled_Y": geometry.ly - geometry.ell,
        "rescaled_mass": geometry.mass - 2 * geometry.ell,
        "third_additive_Gram_term": geometry.ly - geometry.ell - 11 * geometry.b / 6,
        "moment_length": 5 * geometry.ell - geometry.h,
        "compensated_subset_cost": 1 - 5 * geometry.ell,
        "floor_endpoint": F(7, 1200) - 15 * PERTURBATION / 8,
        "delta_alpha_endpoint": F(1, 48) + ALPHA / 16 - 15 * PERTURBATION / 8,
        "intermediate_endpoint": F(49, 14400) - 139 * PERTURBATION / 150,
        "small_rows_beyond_one_sixteenth":
            F(63, 800) - F(51, 100) * PERTURBATION - PERTURBATION / 4 - F(1, 16),
        "principal_w_residue": geometry.ly / 20,
        "principal_z_residue": geometry.h / 600,
    }
    require(all(margin > 0 for margin in margins.values()), "A scale margin is not positive.")
    require(all(margins[key] > MARGIN for key in
                ("floor_endpoint", "delta_alpha_endpoint", "intermediate_endpoint")),
            "An auxiliary endpoint margin does not exceed the central margin.")
    return {
        "p": str(geometry.p), "b": str(geometry.b), "ell": str(geometry.ell),
        "h": str(geometry.h), "l_x": str(geometry.lx), "l_y": str(geometry.ly),
        "M": str(geometry.mass), "theta": str(geometry.theta),
        "improvement_over_seven_eighths": str(F(7, 8) - geometry.theta),
        "principal_exponent": "C(s)=s-11/16",
        "LOW_exponent": str(low), "LOW_equals_C_theta": True,
        "positive_scale_margins": {key: str(value) for key, value in margins.items()},
    }


def check_discriminant(q: Polynomial) -> dict[str, object]:
    require(all(i <= 2 for i, _ in q), "Q is not quadratic in delta.")
    a = {(0, j): value for (i, j), value in q.items() if i == 2}
    b = {(0, j): value for (i, j), value in q.items() if i == 1}
    c = {(0, j): value for (i, j), value in q.items() if i == 0}
    discriminant = add(scale(multiply(a, c), 4), scale(multiply(b, b), -1))
    expected_a = scale(polynomial({(0, 0): 51021, (0, 1): 131008,
                                  (0, 2): 94028, (0, 3): 32032}), F(6, 125))
    expected_b = scale(polynomial({(0, 0): 5918793, (0, 1): 9423268,
                                  (0, 2): 650644}), -F(1, 3125))
    expected_c = scale(polynomial({(0, 0): 37, (0, 1): 34}), F(6186, 625))
    expected_discriminant = scale(polynomial({
        (0, 0): 1254989151, (0, 1): 10600196228952,
        (0, 2): 50726295758792, (0, 3): 69061294318816,
        (0, 4): 19787957489264,
    }), F(1, 9765625))
    for name, actual, expected in (
        ("A", a, expected_a), ("B", b, expected_b), ("C", c, expected_c),
        ("4AC-B^2", discriminant, expected_discriminant),
    ):
        require(actual == expected, f"The published {name} coefficients differ.")
    require((0, 0) in a and all(value > 0 for value in a.values()), "A positivity failed.")
    require((0, 0) in discriminant and all(value > 0 for value in discriminant.values()),
            "Discriminant positivity failed.")
    square = add(scale(multiply(a, DELTA), 2), b)
    require(scale(multiply(a, q), 4) == add(multiply(square, square), discriminant),
            "Completing the square failed.")
    return {
        "Q": serialize(q), "A": serialize(a), "B": serialize(b), "C": serialize(c),
        "four_AC_minus_B_squared": serialize(discriminant),
        "identity": "4AQ=(2A delta+B)^2+(4AC-B^2)",
        "positive_coefficient_proof":
            "A and 4AC-B^2 have positive coefficients and positive constants for y>=0.",
        "conclusion_from_supplied_row_formula":
            "E_theta(h)<-1/200000 on 0<=delta<=5/6, 0<=y<=1/2.",
    }


def check_fixed_skew_ceiling() -> dict[str, object]:
    """Check the y=0 obstruction for the unchanged count bound and fixed skew."""
    # At margin zero and y=0, Q=(2448+6048p)delta^2
    #                            +(-1896+11520p)delta+370-22200p.
    a0, a1 = F(2448), F(6048)
    b0, b1 = -F(1896), F(11520)
    c0, c1 = F(370), -F(22200)
    coefficients = [
        4 * a0 * c0 - b0**2,
        4 * (a0 * c1 + a1 * c0) - 2 * b0 * b1,
        4 * a1 * c1 - b1**2,
    ]
    require(coefficients == [576 * F(49), -576 * F(286020), -576 * F(1162800)],
            "Fixed-skew discriminant polynomial differs.")
    for p in (ZERO, PERTURBATION, F(1, 250), F(1, 50)):
        _, q = endpoint_polynomial(p, ZERO)
        require({key: value for key, value in q.items() if key[1] == 0} == polynomial({
            (2, 0): a0 + a1 * p, (1, 0): b0 + b1 * p, (0, 0): c0 + c1 * p,
        }), "The fixed-skew specialization differs.")

    def sign_polynomial(p: F) -> F:
        return F(49) - 286020 * p - 1162800 * p**2

    # Isolate the positive root on a fixed rational grid, using only integers.
    denominator = 10**15
    left, right = 0, denominator // 1000
    while right - left > 1:
        middle = (left + right) // 2
        if sign_polynomial(F(middle, denominator)) > 0:
            left = middle
        else:
            right = middle
    lower, upper = F(left, denominator), F(right, denominator)
    require(sign_polynomial(lower) > 0 > sign_polynomial(upper),
            "The fixed-skew root bracket failed.")
    require(PERTURBATION < lower, "The chosen perturbation exceeds its certified ceiling.")
    for p in (lower, upper):
        vertex = -(b0 + b1 * p) / (2 * (a0 + a1 * p))
        require(0 < vertex < ALPHA, "The ceiling obstruction lies outside the rectangle.")
    return {
        "specialization": "y=0; margin=0; fixed b=1/8 and unchanged R_*",
        "Q_at_y_zero":
            "(2448+6048p)delta^2+(-1896+11520p)delta+370-22200p",
        "four_AC_minus_B_squared": "576(49-286020p-1162800p^2)",
        "positive_root_p_bracket": [str(lower), str(upper)],
        "corresponding_theta_bracket":
            [str(F(7, 8) - upper / 4), str(F(7, 8) - lower / 4)],
        "scope":
            "Obstruction to strict negativity using this fixed-skew row bound; not a bound on zeros or other methods.",
    }


def check_adverse_examples() -> list[dict[str, str]]:
    controls = []
    delta, y = F(7, 18), ZERO
    _, _, j, r_numerator = count_polynomials()
    j_value = evaluate(j, delta, y)
    r_value = evaluate(r_numerator, delta, y) / (2 * j_value)
    require(r_value == F(2363, 3546), "The adverse example count exponent differs.")
    for theta, expected in (
        (F(437, 500), F(36187, 5804802)),
        (F(87, 100), F(37487, 1195002)),
    ):
        p = 4 * (F(7, 8) - theta)
        geometry = Geometry.at(p)
        _, q = endpoint_polynomial(p, ZERO)
        q_value = evaluate(q, delta, y)
        endpoint = -q_value / (10368 * j_value)
        require(endpoint > 0, "An adverse endpoint is not positive.")
        require(endpoint / geometry.h == expected, "The adverse row reduction differs.")
        controls.append({
            "theta": str(theta), "p": str(p), "delta": str(delta), "y": str(y),
            "a": str((1 + delta) / 2), "q_amplitude": str(delta / 2),
            "R_star": str(r_value), "high_endpoint": str(endpoint),
            "row_exponent_reduction_needed_to_reach_zero": str(endpoint / geometry.h),
        })
    return controls


def generate_certificate() -> dict[str, object]:
    bounds = check_interval_bounds()
    geometry = check_geometry()
    _, q = endpoint_polynomial(PERTURBATION, MARGIN)
    return {
        "schema_version": 1,
        "status": "PASS_exact_endpoint_arithmetic",
        "arithmetic": "Python standard-library fractions.Fraction; no floating point",
        "scope":
            "Exact exponent identities, interval bounds, and polynomial positivity only. "
            "The certificate does not establish analytic row estimates, an L-function "
            "nonvanishing theorem, theorem-family transfer, or proof-kernel verification.",
        "geometry": geometry,
        "count_denominator_bounds": bounds,
        "endpoint": {
            "margin": str(MARGIN),
            "literal_high_formula":
                "a-theta+h(17/50-1/6)-a*l_y-ell/2+delta*x*ell+h(R_*+delta/2-17/50)",
            "independent_formula":
                "-1/48+2delta/3+delta*x/6-(13/16)(1-R_*)"
                "+p(-1/4+delta(1+x)+3R_*/2)",
            "formula_identity_checked": True,
            "definition": "Q=10368J(-E_theta(h)-margin)",
            **check_discriminant(q),
        },
        "fixed_skew_ceiling": check_fixed_skew_ceiling(),
        "adverse_unchanged_bound_examples": check_adverse_examples(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Check the stored JSON (the default).")
    mode.add_argument("--write", action="store_true", help="Explicitly regenerate the stored JSON.")
    args = parser.parse_args()
    try:
        result = generate_certificate()
        if args.write:
            CERTIFICATE.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                                   encoding="utf-8")
            action = "Wrote"
        else:
            require(CERTIFICATE.exists(), "Stored certificate missing; use --write to generate it.")
            stored = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
            require(stored == result, "Stored certificate differs from the exact calculation.")
            action = "Checked"
    except (CertificateError, OSError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"{action} {CERTIFICATE.name}: PASS")
    print("theta = 20999/24000 = 7/8 - 1/24000; endpoint margin = 1/200000")
    print("Scope: exact arithmetic only; analytic estimates are not checked here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
