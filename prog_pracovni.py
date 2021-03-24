
import sqlite3
from os import path
import prace_s_db as d

#db = "db_slovnik"

#pokud db neexistuje - založí se schéma, vloží základní data
if path.exists("db_slovnik.sqlite") == False:
    d.create_sql_db()

#conn = sqlite3.connect(db)
#c = conn.cursor()

print()
print("Seznam studentů:")
print(d.seznam_studentu()) 
# načtu  všechny osoby z databáze --> seznam seznamů

student = "Lenka"
print(f"Seznam jazyků studenta: {student}")
print(d.jazyky_studenta(student))

jazyk = "AJ"
print(f"Seznam učebnic pro jazyk: {jazyk}")
print(d.seznam_ucebnic(jazyk))

ucebnice = "Happy Street 1"
print(f"Seznam lekcí v učebnici: {ucebnice}")
print(d.seznam_lekci(ucebnice))


"""
jmeno = "Filip"
jazyky_ucebnice = [("FJ","Francouz1")]
# jazyky_ucebnice = []

d.pridat_studenta(jmeno,jazyky_ucebnice)
"""

conn, cursor = d.pripojeni_db()
conn.close()


# print("********************************")
# vypíše nápovědu ke VŠEM funkcím z modulu d (resp. prace_s_db)
# help(d)


# vypíše nápovědu ke konkrétní funkci
# help(d.seznam_studentu)
