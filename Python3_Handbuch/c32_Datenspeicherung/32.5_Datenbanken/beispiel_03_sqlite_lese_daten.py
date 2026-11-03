#!/usr/bin/env python

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect("lagerverwaltung.db")
    cursor = con.cursor()

    sql = """
        SELECT lager.fachnummer, lager.komponente, lieferanten.name 
        FROM lager, lieferanten 
        WHERE lieferanten.telefonnummer='011235813' AND
          lager.lieferant=lieferanten.kurzname"""
    cursor.execute(sql)
    print(cursor.fetchall())

