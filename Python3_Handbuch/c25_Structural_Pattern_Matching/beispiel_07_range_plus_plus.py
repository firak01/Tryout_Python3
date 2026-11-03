#!/usr/bin/env python

import math
import itertools

def range_plus_plus(*args):
    match args:
        case []:
            return
        case [e, int(a), *rest] if e is ...:
            yield from range(a + 1)
            yield from range_plus_plus(*rest)
        case [int(a), e, int(b), *rest] if e is ...:
            yield from range(a, b + 1)
            yield from range_plus_plus(*rest)
        case [int(a), e, math.inf] if e is ...:
             yield from itertools.count(start=a)
        case [int(a), *rest]:
            yield a
            yield from range_plus_plus(*rest)
        case _:
            raise ValueError(f"Ungültige Range: {args}")

if __name__ == "__main__":
    print(list(range_plus_plus(1, ..., 4, 10, ..., 14)))
