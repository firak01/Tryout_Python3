#!/usr/bin/env python

import hashlib
import os

num_rounds = 500_000
salt = os.urandom(16)
pwhash = hashlib.pbkdf2_hmac("sha256", input("Setzen Sie Ihr Passwort: ").encode(), salt, num_rounds)

pwlogin = hashlib.pbkdf2_hmac("sha256", input("Passwort zur Anmeldung: ").encode(), salt, num_rounds)
if pwlogin == pwhash:
    print("Zugriff erlaubt")
else:
    print("Zugriff verweigert")

