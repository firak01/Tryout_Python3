#!/usr/bin/env python

import re

regexp = {
    "Name": r"([A-Za-z]+)\s([A-Za-z]+)",
    "Adr": r"([A-Za-z]+)\s(\d+)\s*(\d{5})\s([A-Za-z]+)",
    "Tel": r"(\+\d{2})\s(\d{4})\s(\d{3,})"
}


def lese_datei(dateiname):
    d = {}
    with open(dateiname) as f:
        for zeile in f:
            if ":" in zeile:
                key, d[key] = (s.strip() for s in zeile.split(":", 1))
            elif "key" in locals():
                d[key] += f"\n{zeile.strip()}"
    return d


def analysiere_daten(daten, regexp):
    for key in daten:
        if key not in regexp:
            return False
        m = re.match(regexp[key], daten[key])
        if not m:
            return False
        daten[key] = m.groups()
    return True


if __name__ == "__main__":
    daten = lese_datei("id.txt")
    if analysiere_daten(daten, regexp):
        print(daten)
    else:
        print("Die Angaben sind fehlerhaft")
