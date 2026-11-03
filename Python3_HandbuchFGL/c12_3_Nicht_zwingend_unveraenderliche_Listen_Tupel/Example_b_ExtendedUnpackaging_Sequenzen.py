# -*- coding: utf-8 -*-

'''
"Extended Unpackaging" gibt es erst ab Python3.

Startet man das hier als Jython-Projekt mit Python2, bekommt man z.B. folgenden Fehler:

    wertPre, *andere, wertPost = zahlen
           ^
#SyntaxError: no viable alternative at input '*'

Merke:
Praktisches Beispiel für Tupel Packaging und Entpackaging mit * und Funktionen 
siehe hier: Tryout_Jython/Definitive_Guide_To_Jython\c04_Defining_Functions\Example_m_PassUnknownSequenceOfArguments.py


Created on 03.11.2026

@author: Fritz Lindhauer
'''

#Erstes Beispiel, einfaches Tupel
a=(1,2,3,4,5)   
wertPre, *anders, wertPost = a
print(wertPre)
print(anders)
print(wertPost)


##########################################
#Wir brauchen eine Sequenz, mit eckigen Klammern
zahlen = [11,18,12,15,10]

#"ENTPACKEN mit Übergabe von Stern * beim Entpacken, (siehe auch Tryout_Jython/Definitive_Guide_To_Jython\c04_Defining_Functions\Example_m_PassUnknownSequenceOfArguments.py )
wertPre, *andere, wertPost = zahlen
print(wertPre)
print(anders)
print(wertPost)


