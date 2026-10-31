'''
Created on 18.10.2026

Hier werden mehrere Optionale Parameter verwendet

@author: Fritz Lindhauer
'''
def berechne_preis(nettopreis, steuersatz=19, rabatt=0):
    preis_mit_steuer = nettopreis * (1 + steuersatz / 100)
    endpreis = preis_mit_steuer * (1 - rabatt / 100)

    return endpreis

# Aufrufe und Ausgabe
print(berechne_preis(100))
print(berechne_preis(100, 7))
print(berechne_preis(100, 19, 10))

# Python erlaubt es außerdem, Parameter beim Aufruf über ihren Namen anzugeben
print(berechne_preis(100, rabatt=10)) #gleiche Ausgabe wie vorher, weil steuersatz=19 default ist.