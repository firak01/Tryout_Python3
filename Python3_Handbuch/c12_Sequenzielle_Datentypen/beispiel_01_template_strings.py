#!/usr/bin/env python

'''

Merke:
Eclipse202312 nutzt pyDev 13.1, damit wird Python >3.4.4 verwendet
Daher funktioniert es unter Eclipse202312 Interpolation zu importieren

Aber zur Laufzeit gibt es Probleme:
    from string.templatelib import Interpolation
ModuleNotFoundError: No module named 'string.templatelib'; 'string' is not a package

Lösung: 
Schiebe Python Interpreter 3.4.4 in der Liste der Interpreter nach ganz oben. Damit gilt dieser als Default.
Aber trotzdem noch Probleme:
    print(f"[{t}]: {m}")
                      ^
    SyntaxError: invalid syntax
    
Lösung: 
Das spezielle, hier genutzte String Literal gibt es erst ab Python 3.6
Schiebe Python Interpreter 3.6.8 in der Liste der Interpreter nach ganz oben. Damit gilt dieser als Default.

Aber trotzdem noch Probleme:
    match item:
             ^
    SyntaxError: invalid syntax
    
Lösung: Das Schlüsselwort Match gibt es ab Python 3.10


Lösung: Das Beispiel in der Anaconda Umgebung laufen lassen
Also Anaconda Prompt starten und nicht nur einfach python eingeben, sonder den Pfad zu dieser Datei.
python "C:\1fgl\repo\Eclipse202312\Tryout_Python3\Python3_Handbuch\c12_Sequenzielle_Datentypen\beispiel_01_template_strings.py"

Ergebnis:
[2026-11-03 11:58:46]: Die Werte lauten: p=12, q=5.7
[2026-11-03 11:58:46]: Die Werte lauten: p=12, q=5.7
[2026-11-03 11:58:46]: Die Werte lauten: p=12, q=5.7

###########################################################
Merke:
Das Modul Interpolation gibt es wohl unter Python 3.4.4 nicht
pyDev 2.7 unter Eclipse 4.7 (Oxygen) nutzt aber Python 3.4.4, dort keine Lösung möglich.


'''

import datetime
from string.templatelib import Interpolation

def log_1(m):
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{t}]: {m}")

def log_2(template):
    parts = []
    for item in template:
        if isinstance(item, Interpolation):
            parts.append(f"{item.value} ({type(item.value)})")
        else:
            parts.append(item)
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{t}]:", "".join(parts))

def log_3(template):
    parts = []
    for item in template:
        match item:
            case Interpolation(value):
                parts.append(f"{value} ({type(value)})")
            case str() as s:
                parts.append(s)
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{t}]:", "".join(parts))


if __name__ == "__main__":
    p = 12
    q = 5.7
    log_1(f"Die Werte lauten: {p=}, {q=}")
    log_2(f"Die Werte lauten: {p=}, {q=}")
    log_3(f"Die Werte lauten: {p=}, {q=}")
