#!/usr/bin/env python

class Laenge:
    umrechnung = {
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001,
        "km" : 1000,
        "ft": 0.3048,   # Fuß
        "in": 0.0254,   # Zoll
        "mi": 1609.344  # Meilen
    }

    def __init__(self, zahlenwert, einheit):
        self.zahlenwert = zahlenwert
        self.einheit = einheit

    def __str__(self):
        return f"{self.zahlenwert:f} {self.einheit}"

    def __add__(self, other):
        z = self.zahlenwert * Laenge.umrechnung[self.einheit]
        z += other.zahlenwert * Laenge.umrechnung[other.einheit]
        z /= Laenge.umrechnung[self.einheit]
        return Laenge(z, self.einheit)

    def __sub__(self, other):
        z = self.zahlenwert * Laenge.umrechnung[self.einheit]
        z -= other.zahlenwert * Laenge.umrechnung[other.einheit]
        z /= Laenge.umrechnung[self.einheit]
        return Laenge(z, self.einheit)


if __name__ == "__main__":
    a1 = Laenge(5, "cm")
    a2 = Laenge(3, "dm")
    print(a1 + a2)
    print(a2 + a1)




