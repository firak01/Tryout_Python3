#!/usr/bin/env python

class A:
    __match_args__ = ("x", "z")
    def __init__(self, x, y, z, a):
        self.x = x
        self.y = y
        self.z = z
        self.a = a


if __name__ == "__main__":
    a = A(1, 2, 3, 4)
    match a:
        case A(1, 3, y=2):
            print("Treffer!")

