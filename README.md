# PYZTryoutPython
Python3 FGL

u.a. Ergänzungen zu den Beispiele aus dem Buch "Python 3 - Das umfassende Handbuch" (6. Auflage)<br>
Bzw. sinnvoller Code / Tests in den Kapiteln<br>
oder umfangreichere Anpassungen, z.B. aufgrund der dann im Buch verwendeten neuere Syntax.

Merke:<br>
Unterhalb des Source Folders sind keine Packages angelegt sondern einfache Folder.<br>
Packages haben sehr strikte Namenskonventionen und es würde auch eine pyInit - Routine bereitgestellt(durch pyDev)<BR>

Auch bei einfachen Folder gibt es Probleme beim Umbenennen von Datein, wenn die Folder mit einer Zahl anfangen.
Darum beginnen sie mit c = chapter (Kapitel).

------------
Für die Benennung der pyDev Package-Namen:
Es gab Probleme beim import, wenn der Packagname openai lautete.

Was ist hier passiert?
Du hattest ursprünglich ein lokales Python-Package namens openai. Damit gab es zwei gleichnamige Pakete:
- Dein lokales Package unter tryout\openai
- Das installierte OpenAI-SDK unter site-packages\openai
Python importierte das lokale Package zuerst. Durch die Umbenennung hast du diesen Namenskonflikt beseitigt.
Eclipse hat beim Refactoring allerdings auch die Importanweisungen angepasst. Das ist bei einer Paketumbenennung grundsätzlich beabsichtigt, aber hier unerwünscht: import openai soll weiterhin das externe OpenAI-SDK laden und nicht auf dein umbenanntes Testpaket verweisen.
Was du daraus für deine Python-Projekte mitnehmen kannst
1. Keine lokalen Packages nach externen Bibliotheken benennen. Das gilt beispielsweise für openai, requests, json, typing oder logging.
2. Nach einem Refactoring externe Imports kontrollieren. Eclipse kann nicht immer erkennen, ob eine Importanweisung auf ein externes Paket oder ein eigenes Projektmodul zielt.
3. Den Importpfad prüfen, wenn ein unerklärlicher Fehler auftritt. print(openai.__file__) war hier der entscheidende Diagnosehinweis.
Dein abschließender Test bestätigt nun alle drei Punkte:
- SDK-Version: 3.37.0
- Importpfad: C:\python\3.13.17\Lib\site-packages\openai\__init__.py
- Versionsattribut vorhanden: True