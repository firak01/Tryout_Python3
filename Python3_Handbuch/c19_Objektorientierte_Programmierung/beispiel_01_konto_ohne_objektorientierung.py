#!/usr/bin/env python

def neues_konto(inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
    return {
        "inhaber": inhaber,
        "kontonummer": kontonummer,
        "kontostand": kontostand,
        "max_tagesumsatz": max_tagesumsatz,
        "umsatz_heute": 0
    }


def geldtransfer(quelle, ziel, betrag):
    # Hier erfolgt der Test, ob der Transfer möglich ist
    if betrag < 0 or quelle["umsatz_heute"] + betrag > quelle["max_tagesumsatz"] or ziel["umsatz_heute"] + betrag > ziel["max_tagesumsatz"]:
        # Transfer unmöglich
        return False
    else:
        # Alles okay - auf geht's
        quelle["kontostand"] -= betrag
        quelle["umsatz_heute"] += betrag
        ziel["kontostand"] += betrag
        ziel["umsatz_heute"] += betrag
        return True


def einzahlen(konto, betrag):
    if betrag < 0 or konto["umsatz_heute"] + betrag > konto["max_tagesumsatz"]:
        # Tageslimit überschritten oder ungültiger Betrag
        return False
    else:
        konto["kontostand"] += betrag
        konto["umsatz_heute"] += betrag
        return True


def auszahlen(konto, betrag):
    if betrag < 0 or konto["umsatz_heute"] + betrag > konto["max_tagesumsatz"]:
        # Tageslimit überschritten oder ungültiger Betrag
        return False
    else:
        konto["kontostand"] -= betrag
        konto["umsatz_heute"] += betrag
        return True


def zeige_konto(konto):
    print(f"Konto von {konto['inhaber']}")
    print(f"Aktueller Kontostand: {konto['kontostand']:.2f} Euro")
    print(f"(Heute schon {konto['umsatz_heute']:.2f} von {konto['max_tagesumsatz']} Euro umgesetzt)")


if __name__ == "__main__":
    k1 = neues_konto("Heinz Meier", 567123, 12350.0)
    k2 = neues_konto("Erwin Schmidt", 396754, 15000.0)
    geldtransfer(k1, k2, 160)
    geldtransfer(k2, k1, 1000)
    geldtransfer(k2, k1, 500)
    einzahlen(k2, 500)
    zeige_konto(k1)
    zeige_konto(k2)
