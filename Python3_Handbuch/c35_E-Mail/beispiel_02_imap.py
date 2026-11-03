#!/usr/bin/env python

import imaplib

with imaplib.IMAP4("imap.hostname.de") as im:
    im.login("Benutzername", "Passwort")

    print("Vorhandene Mailboxen:")
    for mb in im.list()[1]:
        name = mb.split(b'"."')[-1]
        print(" - {}".format(name.decode().strip(' "')))

    mb = input("Welche Mailbox soll angezeigt werden: ")
    im.select(mb)
    status, daten = im.search(None, "ALL")
    for mailnr in daten[0].split():
        typ, daten = im.fetch(mailnr, "(RFC822)")
        print(f"{daten[0][1].decode()}\n+++\n")
    im.close()
