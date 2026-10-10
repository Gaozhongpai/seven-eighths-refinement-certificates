#!/usr/bin/env python3
"""Exact algebra for the two finite adaptive stages; no analytic proof or Lean.

The polynomial helpers are shared with the unchanged first-stage certificate.
Run with --write to regenerate the data; the default checks the stored file.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

from endpoint_certificate import (
    ALPHA, DELTA, X, Y, add, constant, multiply, polynomial,
    require, scale, serialize,
)

REPORT = Path(__file__).with_suffix('.json')


def stage(theta_input, p, margin):
    kappa = 2*theta_input-1
    c = 1/(3*kappa)
    h = F(13,16)+3*p/2
    d = polynomial({(0,0):F(5,2)-c,(0,1):1+2*c})
    pp = polynomial({(0,0):1-c/2,(0,1):2,(0,2):2*c})
    am = add(constant(ALPHA),scale(DELTA,-1))
    j = add(multiply(am,d),multiply(DELTA,pp))
    rn = add(scale(multiply(j,add(constant(1),scale(DELTA,-1))),2),
             multiply(am,DELTA,pp))
    # Derive 2J E from the literal main-paper endpoint, retaining R_*.
    e0 = add(constant(-F(1,48)-F(13,16)-p/4),
             multiply(DELTA,add(constant(F(2,3)),scale(X,F(1,6)),
                               scale(add(constant(1),X),p))))
    e_numerator = add(scale(multiply(j,e0),2),scale(rn,h))
    q = add(scale(e_numerator,-1),scale(j,-2*margin))
    # Compare with the separately displayed A_i,B_i,C_i formulas.
    ki = F(1,48)-5*p/4-margin
    vi = add(constant(F(1,16)),scale(Y,F(1,6)+p))
    a = add(scale(multiply(add(pp,scale(d,-1)),vi),2),scale(pp,h))
    b = add(scale(multiply(d,vi),2*ALPHA),
            scale(add(pp,scale(d,-1)),2*ki),scale(pp,-h*ALPHA))
    cc = scale(d,2*ALPHA*ki)
    reconstructed = add(multiply(a,DELTA,DELTA),multiply(b,DELTA),cc)
    require(q == reconstructed,'Literal endpoint and coefficient formulas differ')
    disc = add(scale(multiply(a,cc),4),scale(multiply(b,b),-1))
    a_lower = F(1,4)
    disc_lower = [F(1,100000000),F(1,25),F(19,100),F(13,50),F(3,40)]
    require(set(a)=={(0,k) for k in range(4)},'Wrong A degree')
    require(set(disc)=={(0,k) for k in range(5)},'Wrong discriminant degree')
    require(all(a[0,k]>=a_lower for k in range(4)),'A coefficient bound failed')
    require(all(disc[0,k]>disc_lower[k] for k in range(5)),
            'Discriminant coefficient bound failed')
    square = add(scale(multiply(a,DELTA),2),b)
    require(scale(multiply(a,q),4)==add(multiply(square,square),disc),
            'Completing-square identity failed')
    require(F(13,18)<=kappa<=F(3,4),'Extended-moment parameter out of range')
    require(d[0,0]>=2 and pp[0,0]>=F(10,13),'Positive denominator bound failed')
    theta = F(7,8)-p/4
    require(theta < theta_input,'Stage does not improve its input')
    return dict(input_boundary=str(theta_input),kappa=str(kappa),c=str(c),
                p=str(p),margin=str(margin),output_boundary=str(theta),
                prime_contour_reference=str((1+kappa)/2),
                A=serialize(a),B=serialize(b),C=serialize(cc),
                Q=serialize(q),four_AC_minus_B_squared=serialize(disc),
                A_coefficient_lower_bound=str(a_lower),
                discriminant_coefficient_lower_bounds=[str(x) for x in disc_lower],
                J_lower_bound='25/39')


def certificate():
    first = stage(F(20999,24000),F(1,5836),F(1,100000000))
    second = stage(F(first['output_boundary']),F(107121,625000000),F(1,1000000000))
    require(first['output_boundary']=='20425/23344','First adaptive boundary changed')
    require(second['output_boundary']=='2187392879/2500000000',
            'Final adaptive boundary changed')
    require(second['prime_contour_reference']==first['output_boundary'],
            'Second stage does not use its established input')
    return dict(status='PASS_EXACT_FINITE_ADAPTIVE_ENDPOINTS',
                archived_verified_boundary='20999/24000',
                manuscript_boundary=second['output_boundary'],
                stages=[first,second],runs_Lean=False,
                analytic_moment_or_continuation_verified=False,
                scope='Exact endpoint identities and rational coefficient positivity only. '
                      'The extended moment, source recovery and all-height family '
                      'continuation are proved in the manuscript and companion, '
                      'conditional on their named external inputs. This is not a formal replay.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--write',action='store_true')
    group.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=certificate()
    if args.write:
        REPORT.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:
        require(json.loads(REPORT.read_text())==data,'Adaptive certificate stale')
    print(data['status']+': '+data['manuscript_boundary'])


if __name__=='__main__':
    main()
