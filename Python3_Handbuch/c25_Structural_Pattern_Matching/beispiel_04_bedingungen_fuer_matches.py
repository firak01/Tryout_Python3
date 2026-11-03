#!/usr/bin/env python

import math

class Konstanten:
    inf = math.inf
    minf = -math.inf

wert = 12345
match wert:
    case int() | float() | complex() if abs(wert) < Konstanten.inf:
        print(f"Hier haben wir die endliche Zahl {wert}.")
    case Konstanten.inf | Konstanten.minf:
        print("Das ist unendlich!")
    case _:
        print(f"{type(wert)}: {wert}")
