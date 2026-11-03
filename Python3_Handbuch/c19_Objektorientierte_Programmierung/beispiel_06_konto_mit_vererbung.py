#!/usr/bin/env python

class VerwalteterGeldbetrag:
    def __init__(self, anfangsbetrag):
        self.betrag = anfangsbetrag

    def einzahlen_moeglich(self, betrag):
        return True

    def auszahlen_moeglich(self, betrag):
        return True

    def einzahlen(self, betrag):
        if betrag < 0 or not self.einzahlen_moeglich(betrag):
            return False
        else:
            self.betrag += betrag
            return True

    def auszahlen(self, betrag):
        if betrag < 0 or not self.auszahlen_moeglich(betrag):
            return False
        else:
            self.betrag -= betrag
            return True

    def zeige(self):
        print(f"Betrag: {self.betrag:.2f}")


class AllgemeinesKonto(VerwalteterGeldbetrag):
    def __init__(self, kundendaten, kontostand):
        super().__init__(kontostand)
        self.kundendaten = kundendaten

    def geldtransfer(self, ziel, betrag):
        if self.auszahlen_moeglich(betrag) and ziel.einzahlen_moeglich(betrag):
            self.auszahlen(betrag)
            ziel.einzahlen(betrag)
            return True
        else:
            return False

    def zeige(self):
        self.kundendaten.zeige()
        super().zeige()


class AllgemeinesKontoMitTagesumsatz(AllgemeinesKonto):
    def __init__(self, kundendaten, kontostand, max_tagesumsatz=1500):
        super().__init__(kundendaten, kontostand)
        self.max_tagesumsatz = max_tagesumsatz
        self.umsatz_heute = 0.0

    def transfer_moeglich(self, betrag):
        return (self.umsatz_heute + betrag <= self.max_tagesumsatz)

    def auszahlen_moeglich(self, betrag):
        return self.transfer_moeglich(betrag)

    def einzahlen_moeglich(self, betrag):
        return self.transfer_moeglich(betrag)

    def einzahlen(self, betrag):
        if super().einzahlen_moeglich(betrag):
            self.umsatz_heute += betrag
            return True
        else:
            return False

    def auszahlen(self, betrag):
        if super().auszahlen_moeglich(betrag):
            self.umsatz_heute += betrag
            return True
        else:
            return False

    def zeige(self):
        super().zeige()
        print(f"Heute schon {self.umsatz_heute:.2f} von {self.max_tagesumsatz:.2f} Euro umgesetzt")


class GirokontoKundendaten:
    def __init__(self, inhaber, kontonummer):
        self.inhaber = inhaber
        self.kontonummer = kontonummer

    def zeige(self):
        print("Inhaber:", self.inhaber)
        print("Kontonummer:", self.kontonummer)


class GirokontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz)


class VerwalteterBargeldbetrag(VerwalteterGeldbetrag):
    def __init__(self, bargeldbetrag):
        if bargeldbetrag < 0:
           bargeldbetrag = 0
        super().__init__(bargeldbetrag)

    def auszahlenMoeglich(self, betrag):
        return (self.betrag >= betrag)


class Geldboerse(VerwalteterBargeldbetrag):
    # TODO: Spezielle Methoden für eine Geldboerse
    pass


class Tresor(VerwalteterBargeldbetrag):
    # TODO: Spezielle Methoden für einen Tresor
    pass


class Girokonto(AllgemeinesKonto):
    def __init__(self, inhaber, kontonummer, kontostand):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand)


class NummernkontoKundendaten:
    def __init__(self, identifikationsnummer):
        self.identifikationsnummer = identifikationsnummer

    def zeige(self):
        print("Identifikationsnummer:", self.identifikationsnummer)


class Nummernkonto(AllgemeinesKonto):
    def __init__(self, identifikationsnummer, kontostand):
        kundendaten = NummernkontoKundendaten(identifikationsnummer)
        super().__init__(kundendaten, kontostand)


class NummernkontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):
    def __init__(self, kontonummer, kontostand, max_tagesumsatz):
        kundendaten = NummernkontoKundendaten(kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz)


if __name__ == "__main__":
    print("### Erstes Beispiel")
    k1 = GirokontoMitTagesumsatz("Heinz Meier", 567123, 12350.0)
    k2 = GirokontoMitTagesumsatz("Erwin Schmidt", 396754, 15000.0)
    k1.geldtransfer(k2, 160)
    k2.geldtransfer(k1, 1000)
    k2.geldtransfer(k1, 500)
    k2.einzahlen(500)
    k1.zeige()
    k2.zeige()

    print()
    print("### Zweites Beispiel")
    nk1 = Nummernkonto(113427613185, 5000)
    nk2 = NummernkontoMitTagesumsatz(45657364234, 12000, 3000)
    nk1.auszahlen(1000)
    nk2.einzahlen(1500)
    nk1.geldtransfer(nk2, 2000)
    nk1.zeige()
    nk2.zeige()
