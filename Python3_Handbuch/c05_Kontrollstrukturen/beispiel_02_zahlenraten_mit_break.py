#!/usr/bin/env python

geheimnis = 1337
versuch = -1

while versuch != geheimnis:
    versuch = int(input("Raten Sie: "))

    if versuch == 0:
        print("Das Spiel wird beendet")
        break
    elif versuch < geheimnis:
        print("Zu klein")
    elif versuch > geheimnis:
        print("Zu groß")

print("Sie haben es geschafft!")
