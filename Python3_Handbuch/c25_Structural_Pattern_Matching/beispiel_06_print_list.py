#!/usr/bin/env python

def print_list(x):
    match x:
      case []:
          print("(empty)")
      case [a]:
          print(f"[{a}]")
      case [a, b]:
          print(f"[{a}, {b}]")
      case [a, b, *rest]:
          print(f"[{a}, ..., {rest[-1]}]")

if __name__ == "__main__":
    print_list([1])
    print_list([1, 2])
    print_list(list(range(100)))


