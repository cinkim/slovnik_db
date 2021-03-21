import sqlite3

def pripojeni_db(db="db_slovnik.sqlite"):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    return connection, cursor

def create_sql_db():
    conn, cursor = pripojeni_db()
   
    print('Vytvařím databázi..')
    sql_file = open("db_schema.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

    print('Plním databázi...')
    sql_file = open("db_data.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    
"""
def pridat_studenta(nova_osoba): 
    # vloží novou osobu do db --> nova_osoba = seznam údajů o sobě [jmeno, [ID_jazyku]]    
    conn, cursor = pripojeni_db()
    cursor.execute(f'''INSERT INTO OSOBY values (null,'{nova_osoba[0]}') ''')
    # zjišťuje si ID nově vložené osoby
    cursor.execute(f'''SELECT ID FROM OSOBY WHERE JMENO = '{nova_osoba[0]}' ''')
    nova_osoba_id = cursor.fetchone()[0]
    
    # vkláda jazyky nové osoby do vazebni tabulky osoby_jazyky
    for i in nova_osoba[1]:      
        cursor.execute(f'''INSERT INTO OSOBY_JAZYKY values ({nova_osoba_id},{nova_osoba[1][i-1]}) ''')
    conn.commit()
"""

def pridat_studenta(nova_osoba): 
    # vloží novou osobu do db --> nova_osoba = seznam údajů o sobě [jmeno, [nazev_jazyku]]    
    conn, cursor = pripojeni_db()
    cursor.execute(f'''INSERT INTO OSOBY values (null,'{nova_osoba[0]}') ''')
    # zjišťuje si ID nově vložené osoby
    cursor.execute(f'''SELECT ID FROM OSOBY WHERE JMENO = '{nova_osoba[0]}' ''')
    nova_osoba_id = cursor.fetchone()[0]
    
    
    for jazyk in nova_osoba[1]:
        # zjišťuje ID jazyků, které má daný student
        cursor.execute(f'''SELECT ID FROM JAZYKY WHERE NAZEV = '{jazyk}'  ''')
        jazyk_id = cursor.fetchone()[0]
        # vkláda jazyk nové osoby do vazebni tabulky osoby_jazyky
        cursor.execute(f'''INSERT INTO OSOBY_JAZYKY values ({nova_osoba_id},{jazyk_id}) ''')
    conn.commit()



def select_to_seznam(data):
    seznam = []   
    for polozka in data:
        seznam.append(polozka[0])
    return seznam

def seznam_studentu():      
    conn, cursor = pripojeni_db()
    cursor.execute(f''' SELECT jmeno from osoby''')
      
    return select_to_seznam(cursor.fetchall())

def jazyky_studenta(jmeno_studenta):      
    conn, cursor = pripojeni_db()
    try:
        cursor.execute(f''' SELECT id from osoby where jmeno ='{jmeno_studenta}'  ''')
        id_studenta = cursor.fetchone()[0]
    except:
        return f"Student jménem {jmeno_studenta} není v databázi"
    cursor.execute(f''' SELECT j.nazev from jazyky j join osoby_jazyky oj on oj.jazyk_id = j.id where oj.osoba_id={id_studenta}''')
    
    return select_to_seznam(cursor.fetchall())




