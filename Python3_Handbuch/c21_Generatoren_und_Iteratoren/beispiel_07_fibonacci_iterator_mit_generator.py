#!/usr/bin/env python

class Fibonacci2:
    def __init__(self, max_n):
        self.max_n = max_n

    def __iter__(self):
        a, b = 0, 1
        for n in range(self.max_n):
            a, b = b, a + b
            yield a


if __name__ == "__main__":
    for f in Fibonacci2(14):
        print(f, end=" ")
    print()
    print(list(Fibonacci2(16)))
    print(sum(Fibonacci2(60)))


