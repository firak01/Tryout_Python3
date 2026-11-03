#!/usr/bin/env python

class A:
    def m(cls):
        print("Ich bin", cls)
    m = classmethod(m)


class B(A):
    pass


class C(A):
    pass


if __name__ == "__main__":
    A.m()
    a = A()
    b = B()
    c = C()
    a.m()
    b.m()
    c.m()


