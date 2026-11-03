#!/usr/bin/env python

import csv

with open("autos.csv") as f_csv:
     sample = f_csv.read(1024)
     dialect = csv.Sniffer().sniff(sample)

print("Trennzeichen:", dialect.delimiter)
print("Spaltenkoepfe vorhanden:", csv.Sniffer().has_header(sample))

with open("autos.csv") as f_csv:
     reader = csv.reader(f_csv, dialect)
     for row in reader:
          print(row)

