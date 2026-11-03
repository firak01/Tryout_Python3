#!/usr/bin/env python

import csv

daten = (
    {"marke": "Volvo", "modell": "P245", "leistung_in_ps": "130"},
    {"marke": "Ford", "modell": "Focus", "leistung_in_ps": "90"},
    {"marke": "Mercedes", "modell": "CLK", "leistung_in_ps": "250"},
    {"marke": "Audi", "modell": "A6", "leistung_in_ps": "350"}
)
with open("autos.csv", "w") as f_csv:
    writer = csv.DictWriter(f_csv, ["marke", "modell", "leistung_in_ps"])
    writer.writeheader()
    writer.writerows(daten)
