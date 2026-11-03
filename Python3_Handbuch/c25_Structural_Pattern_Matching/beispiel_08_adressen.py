#!/usr/bin/env python

adressen = [
    {"type": "DE", "name": "DeepL SE", "strasse": "Maarweg 165",
     "ort": "Köln", "PLZ": 50825},
    {"type": "US", "name": "Linux Foundation", "street": "548 Market St",
     "town": "San Francisco", "state": "CA", "ZIP": "94104"},
    {"irgendwas": "nochwas"},
]

def drucke_adresse(adresse):
    match adresse:
        case {
            "type": ("DE" | "Deutschland" | "Germany"),
            "name": str(name),
            "strasse": str(strasse),
            "ort": str(ort),
            "PLZ": (str() | int()) as plz
        }:
            print(name)
            print(strasse)
            print(f"{plz} {ort}")
            print("Germany")
        case {
            "type": ("US" | "USA" | "United States"),
            "name": str(name), "street": str(strasse),
            "town": str(town),
            "state": str(state),
            "ZIP": (str() | int()) as zip_code
        }:
            print(name)
            print(strasse)
            print(f"{town} {state} {zip_code}")
            print("USA")
        case x:
           print(f"Unbekanntes Datenformat: {x}")


if __name__ == "__main__":
    for adresse in adressen:
        drucke_adresse(adresse)
        print()
