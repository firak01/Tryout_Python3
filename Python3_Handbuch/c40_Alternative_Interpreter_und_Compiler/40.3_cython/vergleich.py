#!/usr/bin/env python

import beispiel_01_sortieren_python
import beispiel_02_sortieren_cython
import beispiel_03_sortieren_cython_2
import beispiel_04_sortieren_cython_3
import beispiel_05_sortieren_cython_4

import timeit
import random
import array


def erzeuge_liste():
    werte = array.array("i", range(1000))
    random.shuffle(werte)
    return werte


if __name__ == "__main__":
    t_py  = min(timeit.repeat("beispiel_01_sortieren_python.sortiere(werte)", globals=globals(), setup="werte = erzeuge_liste()", number=1, repeat=100))
    t_cy1 = min(timeit.repeat("beispiel_02_sortieren_cython.sortiere(werte)", globals=globals(), setup="werte = erzeuge_liste()", number=1, repeat=100))
    t_cy2 = min(timeit.repeat("beispiel_03_sortieren_cython_2.sortiere(werte)", globals=globals(), setup="werte = erzeuge_liste()", number=1, repeat=100))
    t_cy3 = min(timeit.repeat("beispiel_04_sortieren_cython_3.sortiere(werte)", globals=globals(), setup="werte = erzeuge_liste()", number=1, repeat=100))
    t_cy4 = min(timeit.repeat("beispiel_05_sortieren_cython_4.sortiere(werte)", globals=globals(), setup="werte = erzeuge_liste()", number=1, repeat=100))

    print("Python:", t_py)

    print("Cython #1:", t_cy1)
    print("Speedup 1:", t_py / t_cy1)

    print("Cython #2:", t_cy2)
    print("Speedup 2:", t_py / t_cy2)

    print("Cython #3:", t_cy3)
    print("Speedup 3:", t_py / t_cy3)

    print("Cython #4:", t_cy4)
    print("Speedup 4:", t_py / t_cy4)
