#!/usr/bin/env python

import cmd
import time

class MeineKonsole(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "==> "
        self.start_time = None

    def do_date(self, prm):
        d = time.localtime()
        print(f"Heute ist der {d[2]:02}.{d[1]:02}.{d[0]:02}")
        return False

    def help_date(self):
        print("Gibt das aktuelle Datum aus")

    def do_time(self, prm):
        z = time.localtime()
        print(f"Es ist {z[3]:02}:{z[4]:02}:{z[5]:02} Uhr")
        return False

    def do_timer(self, prm):
        if prm == "start":
            self.start_time = time.perf_counter()
        elif prm == "get" and self.start_time is not None:
            delta = int(time.perf_counter() - self.start_time)
            print(f"Es sind {delta} Sekunden vergangen.")

    def do_exit(self, prm):
        print("Auf Wiedersehen")
        return True


if __name__ == "__main__":
    konsole = MeineKonsole()
    konsole.cmdloop()
