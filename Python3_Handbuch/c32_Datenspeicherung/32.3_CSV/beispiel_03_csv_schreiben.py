#!/usr/bin/env python

import csv

daten = (
    ["Volvo", "P245", "130"],
    ["Ford", "Focus", "90"],
    ["Mercedes", "CLK", "250"],
    ["Audi", "A6", "350"],
    )
with open("autos.csv", "w") as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(["marke", "modell", "leistung_in_ps"])
    writer.writerows(daten)
