#!/usr/bin/env python

import contextlib

if __name__ == "__main__":
    stdout_umleiten = False
    with open("out.txt", "w") as f_out:
        if stdout_umleiten:
            kontext = contextlib.redirect_stdout(f_out)
        else:
            kontext = contextlib.nullcontext()

        with kontext:
            print("Bildschirm-")
            print("Ausgabe")
