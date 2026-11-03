#!/usr/bin/env python

import re

with open("rheinwerk-verlag.html", "r") as f:
    html = f.read()

it = re.finditer(r"<a .*?href=[\"\'](.*?)[\"\'].*?>(.*?)</a>", html, re.I)

for n, m in enumerate(it):
    print(f"#{n} Name: {m.group(2)}, Link: {m.group(1)}")
