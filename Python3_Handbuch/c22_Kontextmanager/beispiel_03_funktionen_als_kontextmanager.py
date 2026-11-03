#!/usr/bin/env python

import contextlib
import time

@contextlib.contextmanager
def laufzeit():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"Laufzeit: {time.perf_counter() - start:.2f} s")


if __name__ == "__main__":
    with laufzeit():
        x = 0
        for i in range(10000000):
            x += (-1) ** i * i  # Eine zeitaufwendige Berechnung

