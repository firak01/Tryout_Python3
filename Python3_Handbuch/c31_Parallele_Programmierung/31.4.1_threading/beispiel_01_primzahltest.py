#!/usr/bin/env python

import threading

class PrimzahlThread(threading.Thread):
    def __init__(self, zahl):
        super().__init__()
        self.zahl = zahl
    def run(self):
        i = 2
        while i*i <= self.zahl:
            if self.zahl % i == 0:
                print(f"{self.zahl} ist nicht prim, "
                     f"da {self.zahl} = {i} * {self.zahl // i}")
                return
            i += 1
        print(f"{self.zahl} ist prim")

if __name__ == "__main__":
    meine_threads = []
    eingabe = input("> ")
    while eingabe != "e":
        try:
            thread = PrimzahlThread(int(eingabe))
            meine_threads.append(thread)
            thread.start()
        except ValueError:
            print("Falsche Eingabe!")
        eingabe = input("> ")
    for t in meine_threads:
        t.join()


