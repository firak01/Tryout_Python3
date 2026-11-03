#!/usr/bin/env python

class Konto:
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.max_tagesumsatz = max_tagesumsatz
        self.umsatz_heute = 0

    def __eq__(self, k2):
        return self.kontonummer == k2.kontonummer


if __name__ == "__main__":
    konto1 = Konto("Dagobert Duck", 1337, 9999999999999999)
    konto2 = Konto("Donald Duck", 1337, 1.5)
    konto3 = Konto("Gustav Gans", 2674, 50000)
    print(konto1 == konto2)
    print(konto1 == konto3)




