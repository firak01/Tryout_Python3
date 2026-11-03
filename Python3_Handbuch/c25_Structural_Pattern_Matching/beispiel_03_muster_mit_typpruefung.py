#!/usr/bin/env python

class A:
    pass

wert = 3.14
match wert:
    case str():
        print(f"Der String lautet: {wert}")
    case int() | float() | complex():
        print(f"Hier haben wir die Zahl {wert}.")
    case list():
        print(f"Eine Liste: {wert}")
    case A():
        print("Meine Klasse A :-)")
    case _:
        print(f"{type(wert)}: {wert}")
