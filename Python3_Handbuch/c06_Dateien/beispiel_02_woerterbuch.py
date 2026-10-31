#!/usr/bin/env python

woerter = {}
with open("woerterbuch.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        zuordnung = line.split(" ")
        if len(zuordnung) == 2:    # betrachte nur gültige Zeilen
            woerter[zuordnung[0]] = zuordnung[1]

while True:
    wort = input("Geben Sie ein Wort ein: ")
    if wort in woerter:
        print("Das deutsche Wort lautet:", woerter[wort])
    else:
        print("Das Wort ist unbekannt")
