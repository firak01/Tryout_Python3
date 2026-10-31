'''
Created on 17.10.2026

In dem Buch: Python3_Handbuch fehlen einige Beispiele.
Insbesondere "Struktur" ist interessant, 
da ich die "ID" Funktion so nicht aus Java kenne.

"Identitäten werden immer dann wichtig, wenn man prüften möchte, 
 ob es sich um eine ganz bestimmte Instanz handelt und nicht nur um eine mit dem gleichen Typ und Wert."

@author: Fritz Lindhauer
'''
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
    print("ids von a und c sind gleich... q.e.d.")
else:
    print("ids von a und c sind nicht gleich... sollte nicht sein")
    
# und was ist mit b
idB = id(b)
if idA==idB:
    print("ids von a und b sind gleich... sollte nicht sein")
else:
    print("ids von a und b sind nicht(!) gleich... q.e.d.")

    





