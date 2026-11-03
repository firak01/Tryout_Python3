#!/usr/bin/env python

def fliegen(orte):
    print("Wir fliegen nach:", ", ".join(orte))

def laufen(orte: list[str]):
    print("Wir laufen nach:", ", ".join(orte))

if __name__ == "__main__":
    fliegen(["Rom", "Paris", "New York"])
    fliegen([0, 1, 2])
    fliegen(4)
    laufen(["Rom", "Paris", "New York"])
    laufen([0, 1, 2])
    laufen(4)
