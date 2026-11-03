#!/usr/bin/env python

from argparse import ArgumentParser

calc = {
    "plus" : lambda a, b: a + b,
    "minus" : lambda a, b: a - b,
    "mal" : lambda a, b: a * b,
    "geteilt" : lambda a, b: a / b
}

parser = ArgumentParser()
parser.add_argument("-o", "--operation", default="plus")
parser.add_argument("op1", type=float)
parser.add_argument("op2", type=float)
args = parser.parse_args()

op = args.operation
if op in calc:
    print("Ergebnis:", calc[op](args.op1, args.op2))
else:
    parser.error(f"{op} ist keine Operation")
