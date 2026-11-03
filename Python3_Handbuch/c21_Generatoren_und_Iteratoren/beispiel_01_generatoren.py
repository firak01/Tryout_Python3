#!/usr/bin/env python

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


def generator_mit_mehreren_yields():
    a = 10
    yield a
    yield a * 2
    b = 5
    yield a + b


def namen(auch_jungen=True):
    yield "Ella"
    yield "Lina"
    if not auch_jungen:
        return
    yield "Phillip"
    yield "Sven"


if __name__ == "__main__":
    for i in square_generator(10):
        print(i, end=" ")
    print()

    for i in generator_mit_mehreren_yields():
        print(i, end=" ")
    print()

    print(list(namen()))
    print(list(namen(False)))
