#!/usr/bin/env python

import csv

with open("namen.csv") as f_csv:
    reader = csv.reader(f_csv)
    for zeile in reader:
        print(zeile)
