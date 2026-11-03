#!/usr/bin/env python

import hashlib

def mein_datei_hash(dateiname, puffer_groesse=1024):
    with open(dateiname, "rb") as f:
        h = hashlib.md5(f.read(puffer_groesse))
        while daten := f.read(puffer_groesse):
            h.update(daten)
    return h


if __name__ == "__main__":
    if mein_datei_hash("datei1.txt") == mein_datei_hash("datei2.txt"):
        print("Die Dateien sind gleich")
    else:
        print("Die Dateien sind verschieden")
