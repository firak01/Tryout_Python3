'''
Created on 18.10.2026

In Python gibt es die Möglichkeit komplexe Zahlen zu erzeugen und zu verwenden.
Das ist der eingebaute Datentyp: complex.

In Java gibt es keinen entsprechenden Datentypen.
Dort müsste man komplexe Zahlen beispielsweise durch eine eigene Klasse mit zwei Double-Werten realisieren. 

---------------------------------------------
1. Was ist der Imaginärteil einer Zahl?
Bei einer normalen Zahl wie 5 oder -3 sprechen wir von reellen Zahlen.
Es gibt aber auch Zahlen, die einen zusätzlichen Bestandteil besitzen: den Imaginärteil.
Eine komplexe Zahl hat allgemein die Form:

z = a + b*i


Dabei gilt:
- a ist der Realteil.
- b ist der Imaginärteil.
- i ist die imaginäre Einheit mit der Eigenschaft i^2=-1.

Ein Beispiel:
z = 3 + 4i

Der Realteil ist 3, der Imaginärteil ist 4. Wichtig: Der Imaginärteil ist nicht 4i  sondern nur die Zahl 4.

Aber warum braucht man so etwas?
Die imaginäre Einheit i wurde eingeführt, um beispielsweise die Gleichung
x^2=-1

lösen zu können.
Bei den reellen Zahlen gibt es dafür keine Lösung: Das Quadrat einer reellen Zahl ist immer größer oder gleich null.
Mit der imaginären Einheit gilt dagegen:

i^2=-1


In der Elektrotechnik, Mathematik und Physik sind komplexe Zahlen deshalb sehr nützlich.
Merksatz: Der Imaginärteil ist der Zahlenkoeffizient vor der imaginären Einheit. Bei 3 + 4j ist er also 4.0, nicht 4j



@author: Fritz Lindhauer
'''

# Hier wird eine komplexe Zahl erstellt
zahl = 3 + 4j

print(zahl)
print(zahl.real)
print(zahl.imag)


# negative und rein imaginäre Zahlen
zahl1 = 5 - 2j
zahl2 = 7
zahl3 = 6j

print(zahl1.real, zahl1.imag)
print(zahl2.real, zahl2.imag)
print(zahl3.real, zahl3.imag)


# rechnen mit komplexen Zahlen
a = 3 + 4j
b = 1 + 2j

print(a + b)

# Die Multiplikation funktioniert nach den üblichen algebraischen Regeln. Dabei ist insbesondere \(j^2=-1\) zu berücksichtigen.
print(a * b)

'''
Wie kommt Python auf dieses Ergebnis? Wir rechnen es Schritt für Schritt von Hand nach.
1. Schritt: Die beiden Zahlen aufschreiben
Wir haben zwei komplexe Zahlen:
\[
a = 3 + 4j
\]

\[
b = 1 + 2j
\]

Zur Erinnerung: j ist in Python die imaginäre Einheit. Für sie gilt:
\[
j^2 = -1
\]

Diese Regel ist der entscheidende Punkt bei der Multiplikation.
2. Schritt: Die Klammern miteinander multiplizieren
Wir schreiben die Multiplikation zunächst ganz normal mit Klammern auf:
\[
a \cdot b = (3+4j)(1+2j)
\]

Nun verwenden wir das Distributivgesetz. Das kennst du vermutlich bereits aus der Schulmathematik:
\[
(a+b)(c+d)=ac+ad+bc+bd
\]

Das bedeutet: Jeder Bestandteil der ersten Klammer wird mit jedem Bestandteil der zweiten Klammer multipliziert.
Die vier Multiplikationen
1. Real × Real
\(3 \cdot 1 = 3\)


2. Real × Imaginär
\(3 \cdot 2j = 6j\)


3. Imaginär × Real
\(4j \cdot 1 = 4j\)


4. Imaginär × Imaginär
\(4j \cdot 2j = 8j^2\)




Damit erhalten wir:
\[
3 + 6j + 4j + 8j^2
\]

3. Schritt: Die imaginäre Einheit berücksichtigen
Jetzt kommt die wichtige Besonderheit:
\[
j^2=-1
\]

Deshalb wird aus dem letzten Term:
\[
8j^2=8\cdot(-1)=-8
\]

Unsere Rechnung lautet jetzt:
\[
3 + 6j + 4j - 8
\]

Beachte: Aus der Multiplikation zweier imaginärer Bestandteile ist eine reelle Zahl geworden.
4. Schritt: Gleichartige Bestandteile zusammenfassen
Wir ordnen die reellen und imaginären Bestandteile:
\[
(3-8)+(6j+4j)
\]

Die reellen Zahlen ergeben:
\[
3-8=-5
\]

Die imaginären Bestandteile ergeben:
\[
6j+4j=10j
\]

Damit erhalten wir das Endergebnis:
\[
\boxed{-5+10j}
\]
'''