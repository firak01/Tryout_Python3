'''
Angeregt aus dem Buch: "Python3: Das umfassende Handbuch"
In den Materialien zum Buch fehlende Beispiele zu einigen Kapiteln.

Created on 17.10.2026

Hier ein Phänomen, das Python die gleich id vergibt, obwohl die Variablen unterschiedlich sind.
Das macht es bei gleichem Wert.


@author: Fritz Lindhauer
'''
a=1
b=1

print(a)
print(type(a))
print(id(a)) # siehe da, a und b haben die gleiche id
idA = id(a)

print(b)
print(type(b))
print(id(b)) # siehe da, a und b haben die gleiche id
idB = id(b)

if idA==idB:
    print("ids von a und b sind gleich... Überraschung!!! Soll auch so sein, da 'immutable' Variable.")
else:
    print("ids von a und b sind nicht gleich... sollte nicht so sein.")
    