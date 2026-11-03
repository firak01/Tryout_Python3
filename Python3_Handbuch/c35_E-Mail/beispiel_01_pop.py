#!/usr/bin/env python

import poplib

pop = poplib.POP3("pop.server.de")
pop.user("Benutzername")
pop.pass_("Passwort")

for i in range(1, pop.stat()[0]+1):
    for zeile in pop.retr(i)[1]:
        print(zeile)
    print("***")

pop.quit()
