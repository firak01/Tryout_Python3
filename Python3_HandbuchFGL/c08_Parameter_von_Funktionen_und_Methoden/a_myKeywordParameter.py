'''
Created on 18.10.2026

In Python gibt es das Konzept feste Parameter zu übergeben, die dann unabhängig von der Position im Methodenaufruf sind.
Das kann dazu verwendet werden "optionale Parameter" zu erstellen, die mit einem Defaultwert vesehen sind.


----------------------------------------------------------------------------------------------
In Java gibt es das Konzept feste Parameter zu übergeben nicht.
Hier kann man ähnliches mit Methodenüberladung erreichen... was ich intensiv in den JAZ - Projekten mache, z.B.:

public void begruessung(String name, String anrede) {
    System.out.println(anrede + " " + name + "!");
}

public void begruessung(String name) {
    begruessung(name, "Hallo"); // Standardwert
}

Aufrufe wären dann:
begruessung("Peter", "Guten Morgen");
begruessung("Peter"); // verwendet "Hallo"


@author: Fritz Lindhauer
'''

def begruessung(name, anrede="Hallo"):
    print(anrede + " " + name + "!")


# Aufruf mit beiden Parametern
begruessung("Peter", "Guten Morgen")

# Aufruf nur mit dem Pflichtparameter
begruessung("Peter")
