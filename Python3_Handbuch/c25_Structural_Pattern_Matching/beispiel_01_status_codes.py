#!/usr/bin/env python

from enum import Enum

class StatusCodes(Enum):
    OK = 0
    NETZWERKFEHLER = 1
    SYSTEMFEHLER = 2

status = StatusCodes.SYSTEMFEHLER
match status:
    case StatusCodes.OK:
        print("Operation erfolgreich abgeschlossen")
    case StatusCodes.NETZWERKFEHLER:
        print("Ein Netzwerkfehler ist aufgetreten")
    case StatusCodes.SYSTEMFEHLER:
        print("Es gab einen Systemfehler")
    case _:
        print(f"Unbekannter Status: {status}")
