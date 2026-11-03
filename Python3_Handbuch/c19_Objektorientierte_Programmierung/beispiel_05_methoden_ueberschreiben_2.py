#!/usr/bin/env python

class A:
    def __init__(self):
        print("Konstruktor von A")
        self.x = 1337

    def m(self):
        print("Methode m von A. Es ist self.x =", self.x)


class B(A):
    def __init__(self):
        print("Konstruktor von B")
        super().__init__()
        self.y = 10000
    def n(self):
        print("Methode n von B. Es ist self.y =", self.y)
    def m(self):
        print("Methode m von B.")
        super().m()


if __name__ == "__main__":
    b = B()
    b.m()

