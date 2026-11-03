#!/usr/bin/env python

import email

mail = """Subject: Hallo Welt
From: Donald Duck <don@ld.de>
To: Onkel Dagobert <d@gobert.de>

Hallo Welt
"""

msg = email.message_from_string(mail)
print(msg["From"])

