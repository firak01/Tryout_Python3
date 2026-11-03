#!/usr/bin/env python

class MeinLogging:
    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def eintrag(self, text):
        self.f.write(f"==> {text}\n")

    def __enter__(self):
        self.f = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()


if __name__ == "__main__":
    with MeinLogging("logfile.txt") as log:
        log.eintrag("Hallo Welt")
        log.eintrag("Na, wie gehts?")
