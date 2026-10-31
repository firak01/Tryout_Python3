#!/usr/bin/env python

geheimnis = 1337
#original aus dem Buch: while (versuch := int(input("Raten Sie: "))) != geheimnis:
#ABER := als Walrus-Operator gibt es erst ab Python 3.8.
#DARUM muss der Code angepasst werden

geheimnis = 1337
versuch = int(input("Raten Sie: "))

while versuch != geheimnis:
    if versuch == 0:
        print("Das Spiel wird beendet")
        break
    elif versuch < geheimnis:
        print("Zu klein")
    elif versuch > geheimnis:
        print("Zu groß")
else:
    print("Sie haben es geschafft!")
