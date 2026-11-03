#!/usr/bin/env python

import multiprocessing


class PrimzahlProzess(multiprocessing.Process):
    def __init__(self, zahl, einauslock):
        super().__init__()
        self.zahl = zahl
        self.ein_aus_lock = einauslock

    def run(self):
        i = 2
        while i * i <= self.zahl:
            if self.zahl % i == 0:
                with self.ein_aus_lock:
                    print(f"{self.zahl} ist nicht prim, "
                          f"da {self.zahl} = {i} * {self.zahl // i}")
                return
            i += 1
        with self.ein_aus_lock:
            print(f"{self.zahl} ist prim")


if __name__ == "__main__":
    meine_prozesse = []
    ein_aus_lock = multiprocessing.Lock()
    eingabe = input("> ")
    while eingabe != "e":
        try:
            prozess = PrimzahlProzess(int(eingabe), ein_aus_lock)
            meine_prozesse.append(prozess)
            prozess.start()
        except ValueError:
            with ein_aus_lock:
                print("Falsche Eingabe!")
        with ein_aus_lock:
            eingabe = input("> ")
    for p in meine_prozesse:
        p.join()

