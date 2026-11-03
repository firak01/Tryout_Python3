#!/usr/bin/env python

werte = ["Hallo", [], -5, 6, 3, float("-inf"), "Welt", {4, 6}]
letzte_endliche_zahl, letzter_string = None, None

for wert in werte:
    match wert:
        case (
            int() | float() | complex() as zahl
        ) if abs(wert) < float("inf"):
            letzte_endliche_zahl = zahl
        case str() as string:
            letzter_string = string

print(f"Letzte endliche Zahl: {letzte_endliche_zahl}")
print(f"Letzter String:       {letzter_string}")

