#!/usr/bin/env python

import functools

class Zitat:
    def __init__(self):
        self.quelle = "Unbekannt"

    def zitat(self, text):
        print(f"{self.quelle}: '{text}'")

    def setze_quelle(self, quelle):
        self.quelle = quelle

    setze_donald = functools.partialmethod(setze_quelle, "Donald Duck")
    setze_goofy = functools.partialmethod(setze_quelle, "Goofy")



if __name__ == "__main__":
    zitat = Zitat()
    zitat.setze_donald()
    zitat.zitat("Quack")


