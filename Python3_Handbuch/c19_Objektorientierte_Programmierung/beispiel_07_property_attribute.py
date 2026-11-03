#!/usr/bin/env python

class A1:
    def __init__(self):
      self._x = 100

    def get_x(self):
      return self._x

    def set_x(self, wert):
      if wert < 0:
        return
      self._x = wert


class A2:
    def __init__(self):
        self.x = 100

    def get_x(self):
        print("Getter gerufen")
        return self._x

    def set_x(self, wert):
        print("Setter gerufen")
        if wert < 0:
            return
        self._x = wert

    x = property(get_x, set_x)


if __name__ == "__main__":
    a = A1()
    print(a.get_x())
    a.set_x(300)
    print(a.get_x())
    a.set_x(-20)
    print(a.get_x())

    print()

    a = A2()
    a.x = 300
    print(a.x)
    a.x = -20
    print(a.x)

