#!/usr/bin/env python
from struct import unpack

with open("kaffee.bmp", "rb") as f:
    f.seek(18)
    breite, hoehe = unpack("ii", f.read(8))
    f.seek(2, 1)
    bpp = unpack("H", f.read(2))[0]

print("Breite:", breite, "px")
print("Höhe:", hoehe, "px")
print("Farbtiefe:", bpp, "bpp")
