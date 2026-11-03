'''
Created on 17.10.2026

Hier ein Phänomen, das Python die gleich id vergibt, obwohl die Variablen unterschiedlich sind.
Das macht es bei gleichem Wert.


@author: Fritz Lindhauer
'''
# Hier mit Strings arbeiten und zeigen wir die id sich ändert, wenn etwas verändert wird.
a="Wasser"
b=a

print(a)
print(type(a))
print(id(a)) # siehe da, a und b haben die gleiche id
idA = id(a)

print(b)
print(type(b))
print(id(b)) # siehe da, a und b haben die gleiche id
idB = id(b)
print(a)
print(b)
if idA==idB:
    print("ids von a und b sind gleich... erwartbar")
else:
    print("ids von a und b sind nicht gleich, sollte nicht sein")
    
# nun mit Stringverarbeitung
a+="flasche"
idA = id(a)
idB = id(b)
print(a)
print(b)
if idA==idB:
    print("ids von a und b sind nicht gleich, sollte nicht sein")
else:
    print("ids von a und b sind nicht mehr(!) gleich... erwartbar. Bei Strings wird mit += eine neue Instanz angelegt.")


    