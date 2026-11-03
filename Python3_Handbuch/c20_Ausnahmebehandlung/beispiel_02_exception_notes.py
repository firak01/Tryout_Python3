#!/usr/bin/env python
from struct import unpack

def lese_infos_1(dateiname):
    with open(dateiname, "rb") as f:
        f.seek(18)
        breite, hoehe = unpack("ii", f.read(8))
        f.seek(2, 1)
        bpp = unpack("H", f.read(2))[0]
    return breite, hoehe, bpp

def lese_infos_2(dateiname):
    try:
        with open(dateiname, "rb") as f:
            f.seek(18)
            breite, hoehe = unpack("ii", f.read(8))
            f.seek(2, 1)
            bpp = unpack("H", f.read(2))[0]
        return breite, hoehe, bpp
    except Exception as e:
        e.add_note(f"Bearbeitete Datei: {dateiname}")
        raise

if __name__ == "__main__":
    dateien = ["kaffee.bmp", "ohne_daten.bmp"]
    infos = [lese_infos_2(dateiname) for dateiname in dateien]
    for breite, hoehe, bpp in infos:
        print(f"Breite: {breite} px")
        print(f"Höhe: {hoehe} px")
        print(f"Farbtiefe: {bpp} bpp")

