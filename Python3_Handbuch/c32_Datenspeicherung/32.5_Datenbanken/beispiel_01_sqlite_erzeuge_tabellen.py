#!/usr/bin/env python

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect("lagerverwaltung.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE lager (
        fachnummer INTEGER, seriennummer INTEGER, 
        komponente TEXT, lieferant TEXT, reserviert INTEGER)""")

    cursor.execute("""CREATE TABLE lieferanten (
        kurzname TEXT, name TEXT, telefonnummer TEXT)""")

    cursor.execute("""CREATE TABLE kunden (
        kundennummer INTEGER, name TEXT, anschrift TEXT)""")

