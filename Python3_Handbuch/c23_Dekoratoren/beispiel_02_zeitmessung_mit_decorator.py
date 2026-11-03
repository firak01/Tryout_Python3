#!/usr/bin/env python

import time
import random
import functools

def mit_zeitmessung(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            e = time.perf_counter()
            print(f"Laufzeit von {fn.__name__}: {e - t}s")
    return wrapper

@mit_zeitmessung
def schlafe_ein_wenig():
    time.sleep(random.randint(1, 3))

@mit_zeitmessung
def schlafe_so_viel(n):
    time.sleep(n)

@mit_zeitmessung
def schlafe_sehr_wenig(wach_bleiben=False):
    if not wach_bleiben:
        time.sleep(0.1)


if __name__ == "__main__":
    schlafe_ein_wenig()
    schlafe_so_viel(1)
    schlafe_sehr_wenig(wach_bleiben=True)

