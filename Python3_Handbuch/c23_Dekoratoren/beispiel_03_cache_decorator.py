#!/usr/bin/env python

import time
import random
import functools

class CacheDecorator:
    def __init__(self):
        self.cache = {}
        self.func = None

    def cached_func(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
            print("Ergebnis berechnet")
        else:
            print("Ergebnis geladen")
        return self.cache[args]

    def __call__(self, func):
        self.func = func
        return self.cached_func


@CacheDecorator()
def fak(n):
    ergebnis = 1
    for i in range(2, n+1):
        ergebnis *= i
    return ergebnis


if __name__ == "__main__":
    print(fak(10))
    print(fak(20))
    print(fak(20))
    print(fak(10))

