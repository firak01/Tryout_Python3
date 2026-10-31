#!/usr/bin/env python

import datetime
from string.templatelib import Interpolation

def log_1(m):
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{t}]: {m}")

def log_2(template):
    parts = []
    for item in template:
        if isinstance(item, Interpolation):
            parts.append(f"{item.value} ({type(item.value)})")
        else:
            parts.append(item)
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{t}]:", "".join(parts))

def log_3(template):
    parts = []
    for item in template:
        match item:
            case Interpolation(value):
                parts.append(f"{value} ({type(value)})")
            case str() as s:
                parts.append(s)
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{t}]:", "".join(parts))


if __name__ == "__main__":
    p = 12
    q = 5.7
    log_1(f"Die Werte lauten: {p=}, {q=}")
    log_2(t"Die Werte lauten: {p=}, {q=}")
    log_3(t"Die Werte lauten: {p=}, {q=}")
