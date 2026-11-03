#!/usr/bin/env python

from struct import unpack

with open("kaffee.bmp", "rb") as f:
    f.seek(18)
    werte = unpack("iiHH", f.read(12))
    print("Breite:", werte[0], "px")
    print("Höhe:", werte[1], "px")
    print("Farbtiefe:", werte[3], "bpp")
