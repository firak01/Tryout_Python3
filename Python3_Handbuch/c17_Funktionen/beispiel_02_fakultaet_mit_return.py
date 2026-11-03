#!/usr/bin/env python

def fak(zahl):
    ergebnis = 1
    for i in range(2, zahl + 1):
        ergebnis *= i
    return ergebnis

while True:
    eingabe = int(input("Geben Sie eine Zahl ein: "))
    print(fak(eingabe))

