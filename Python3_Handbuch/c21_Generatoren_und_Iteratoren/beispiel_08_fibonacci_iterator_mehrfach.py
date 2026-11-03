#!/usr/bin/env python

class Fibonacci3:
    class FibonacciIterator:
        def __init__(self, max_n):
            self.max_n = max_n
            self.n, self.a, self.b = 0, 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.n < self.max_n:
                self.n += 1
                self.a, self.b = self.b, self.a + self.b
                return self.a
            else:
                raise StopIteration

    def __init__(self, max_n):
        self.max_n = max_n

    def __iter__(self):
        return self.FibonacciIterator(self.max_n)


if __name__ == "__main__":
    for f in Fibonacci3(14):
        print(f, end=" ")
    print()
    print(list(Fibonacci3(16)))
    print(sum(Fibonacci3(60)))
    print()

    l = Fibonacci3(3)
    for i in l:
        for j in l:
            print(i, j, end=", ")
    print()


