'''
Created on 17.10.2026

Manche Variablen / Referenzen werden nicht mehr benötigt.
Der "Garbage Collector" sorgt (wie in Java) für das Freigeben des Speichers.

Damit der Garbage Collector diesen Speicher freigibt, dürfen keine Referenzen mehr darauf verweisen.
mit dem Schlüsselwort del wird die Referenz gelöscht.
Der Referenzzähler wird dann um 1 reduziert.
Ein Fehler wird geworfen, wenn solch eine gelöschte Referenzvariable wieder verwendet wird.

@author: Fritz Lindhauer
'''

# Wir nehmen den Code aus dem vorherigen Beispiel...
# Eine Struktur hat Wert...
a=1337
b=2674/a
print(b)

# Eine Struktur hat Typ...
typeA = type(a)
print(typeA)

# UND DAS INTERESSANTE: Eine Struktur hat ID
idA = id(a);
print(idA);

# ---------------------
# Nun mit Referenzen experimentieren
c=a
print(c)
print(type(c))
print(id(c)) # siehe da, a und c haben die gleiche id

idC = id(c)
if idA==idC:
    print("ids von a und c sind gleich... wie erwartet.")
else:
    print("ids von a und c sind nicht gleich... sollte nicht sein.")
    
# und was ist mit b
idB = id(b)
if idA==idB:
    print("ids von a und b sind gleich... sollte nicht sein")
else:
    print("ids von a und b sind nicht(!) gleich... wie erwartet")
    
# nun geben wir die Refernzen frei. Hinter del können meherere Referenzen mit Komma getrennt angegeben werden.
del a, b, c

# nun wird der Fehler erwartet: Name a is not defined
print(a)
