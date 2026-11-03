#!/usr/bin/env python

class A:
    def __init__(self):
        print("Konstruktor von A")
        self.x = 1337

    def m(self):
        print("Methode m von A. Es ist self.x =", self.x)


class B(A):
    def n(self):
        print("Methode n von B")


if __name__ == "__main__":
    b = B()
    b.n()
    b.m()

