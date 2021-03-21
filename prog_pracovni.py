
import sqlite3
from os import path
import prace_s_db as d


#pokud db neexistuje - založí se schéma, vloží základní data
if path.exists("db_slovnik.sqlite") == False:
    d.create_sql_db()

# založení nového studenta
novy = ["aaa",["AJ", "NJ", "FJ"]]

d.pridat_studenta(novy)

print()
print("Seznam studentů:")
print(d.seznam_studentu()) 
# načtu  všechny osoby z databáze --> seznam seznamů

student = "aaa"
print(f"Seznam jazyků studenta: {student}")
print(d.jazyky_studenta(student))

conn, cursor = d.pripojeni_db()
conn.close()