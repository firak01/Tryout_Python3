# -*- coding: utf-8 -*-

'''
Angeregt aus dem Buch: "Python3: Das umfassende Handbuch"
In den Materialien zum Buch fehlende Beispiele zu einigen Kapiteln.

Merke:
Praktisches Beispiel für Tupel Packaging und Entpackaging mit * und Funktionen 
siehe hier: Tryout_Jython/Definitive_Guide_To_Jython\c04_Defining_Functions\Example_m_PassUnknownSequenceOfArguments.py

Created on 03.11.2026

@author: Fritz Lindhauer
'''

#Erzeuge eine neue Tupel Instanz mit runden Klammern
a=(1,2,3,4,5)

#Zugriff auf Inhalte mit eckigen Klammern und Index
wert=a[0]
print("%s" % wert) #Python3, Syntax. Hier ist print eine Funktion

#######################################################
#Erzeuge eine neue Tupel Instanz und lasse die Klammern weg
datum = 26, 7, 1987 #Das nennt das Buch "PACKAGING"
print(datum)

#"ENTPACKEN" geht dagegen so
(tag, monat, jahr) = datum #also ein Tupel mit Variablen zuweisen, das nennt das BUCH "UNPACKAGING"
print(tag)




