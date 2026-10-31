#!/usr/bin/env python
woerter = {
    "Germany" : "Deutschland",
    "Spain" : "Spanien",
    "Greece" : "Griechenland"
}

with open("ausgabe.txt", "w") as fobj:
    for engl in woerter:
        fobj.write(f"{engl} {woerter[engl]}\n")

