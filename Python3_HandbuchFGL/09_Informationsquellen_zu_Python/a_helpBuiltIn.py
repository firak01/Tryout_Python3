'''
Created on 18.10.2026

In Python gibt es die Möglichkeit ein Built-In Hilfesystem verwenden.

Ergänzend gibt es im Plugin pyDev noch Hilfe, wenn man mit der Maus über ein Schlüsselwort, etc. stehenbleibt.

@author: Fritz Lindhauer
'''

# Ausgabe des Einleitungstexts und interaktive Eingabe
#help() #öffnet auf der Konsole eine Eingabemöglichkeit. Dann kann man ein Stichwort dazu eingeben. Z.B. For

# Stichwort gleich der Hilfefunktion übergeben
#help('pprint')

# Die Hilfe in dem Modul angeben
# Das Modul für die Hilfe zu importieren, braucht man wohl nicht, wenn man es als String übergibt, daher ... 
# #import pprint
# help('pprint.pprint')

# Übergibt man dies nicht als String, braucht man aber schon das Modul
import pprint
help(pprint.pprint)


#