#!/usr/bin/env python

class KontostandException(Exception):
    def __init__(self, kontostand, betrag):
        super().__init__(kontostand, betrag)
        self.kontostand = kontostand
        self.betrag = betrag

    def __str__(self):
        return f"Kontostand zu niedrig: Es werden {self.betrag - self.kontostand} € mehr benötigt"


class Konto:
    def __init__(self, betrag):
        self.kontostand = betrag

    def abheben(self, betrag):
        if betrag > self.kontostand:
            raise KontostandException(self.kontostand, betrag)
        self.kontostand -= betrag


if __name__ == "__main__":
    k = Konto(1000)
    try:
        k.abheben(2000)
    except KontostandException as e:
        print(f"Kontostand: {e.kontostand} €")
        print(f"Abheben von {e.betrag} € nicht möglich.")

    k.abheben(2000)
