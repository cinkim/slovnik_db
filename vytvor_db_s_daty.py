import sqlite3

db = "c:/DB/database_slovnik"

conn = sqlite3.connect(db)
c = conn.cursor()


print('Vytvařím databázi..', end="")
sql_file = open("db_schema.sql")
sql_as_string = sql_file.read()
c.executescript(sql_as_string)
print('Hotovo')

print('Plním databázi...', end="")
sql_file = open("db_data.sql")
sql_as_string = sql_file.read()
c.executescript(sql_as_string)
print('Hotovo')


c.execute(''' SELECT Count(*) from osoby ''')
print("Databáze obsahuje ", c.fetchone()[0], "osob")

c.execute(''' SELECT Count(*) from ucebnice ''')
print("Databáze obsahuje ", c.fetchone()[0], "učebnic")



c.execute(''' SELECT Count(*) from lekce ''')
print("Databáze obsahuje ", c.fetchone()[0], "lekcí")

c.execute(''' SELECT Count(*) from slovicka ''')
print("Databáze obsahuje ", c.fetchone()[0], "slovíček")

