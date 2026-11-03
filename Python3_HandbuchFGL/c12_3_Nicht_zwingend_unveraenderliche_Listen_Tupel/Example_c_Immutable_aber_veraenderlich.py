# -*- coding: utf-8 -*-

'''
Angeregt aus dem Buch: "Python3: Das umfassende Handbuch"
In den Materialien zum Buch fehlende Beispiele zu einigen Kapiteln.

Tupel Instanz an sich ist unveränderbar.
Aber der Inhalt ist das nicht.

Created on 03.11.2026

@author: Fritz Lindhauer
'''

# Tupel Instanz erstellen
a=([],)

a[0].append("Und sie dreht sich doch!")

print(a)
print(a[0])