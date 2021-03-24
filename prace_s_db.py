import sqlite3

def pripojeni_db(db="db_slovnik.sqlite"):
    """
     - vytvori pripojeni a kruzor do databaze sqlite
    VSTUP: db - nepovinny udaj - cesta k db-souboru; kdyz se nezada, tak db = "db_slovnik.sqlite"
    VYSTUP: connection, cursor
    """
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    return connection, cursor

def create_sql_db():
    """
    - vytvori strukturu databaze, naplni nektere tabulky    
    VSTUP: bez parametru, natvrdo bere z SQL skritpu v akt.adr. - db_schema.sql, db_data.sql
    VYSTUP: pripravena db ve formatu sqlite
    """
    conn, cursor = pripojeni_db()
    print('Vytvařím databázi..')
    sql_file = open("db_schema.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

    print('Plním databázi...')
    sql_file = open("db_data.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
    
def pridat_studenta(jmeno_studenta, jazyky_ucebnice):
    """
    - vlozi noveho studenta a jeho jazyky+ucebnice
    VSTUP: jmeno_studenta - retezec
           jazyky_ucebnice - [("jazyk1","ucebnice1"), ("jazyk2","ucebnice2"), ...]
    VYSTUP: odpovidajici zaznamy v db
    """ 
    conn, cursor = pripojeni_db()
    # vloží nový záznam do tabulky osoby
    cursor.execute(f'''INSERT INTO OSOBY values (null,'{jmeno_studenta}', null) ''')
    # zjišťuje ID nově vložené osoby
    cursor.execute(f'''SELECT ID FROM OSOBY WHERE JMENO = '{jmeno_studenta}' ''')
    nova_osoba_id = cursor.fetchone()[0]       
    for jazyk,ucebnice in jazyky_ucebnice:
        print(jazyk, ucebnice)
        # zjišťuje ID jazyků, které má daný student
        # (jazyk v db musí existovat, uživatel vybírá z nabídky jazyků)
        cursor.execute(f'''SELECT ID FROM JAZYKY WHERE NAZEV = '{jazyk}'  ''')
        jazyk_id = cursor.fetchone()[0]

        try: # pokud skončí chybou, daná učebnice v db není
            cursor.execute(f'''SELECT ID FROM UCEBNICE WHERE NAZEV = '{ucebnice}'  ''')
            ucebnice_id = cursor.fetchone()[0]
            print("JAZYK_ID: ", jazyk_id,"UCEBNICE_ID: ", ucebnice_id)
            # vkláda jazyk a stávající učebnici nové osoby do vazebni tabulky osoby_jazyky
            cursor.execute(f'''INSERT INTO OSOBY_JAZYKY values ({nova_osoba_id},{jazyk_id}, {ucebnice_id}) ''')
        except:
            print("Učebnice není v db, musí se nová založit")    
            nova_ucebnice_id = uloz_novou_ucebnici(ucebnice, jazyk_id,cursor)
            cursor.execute(f'''INSERT INTO OSOBY_JAZYKY values ({nova_osoba_id},{jazyk_id}, {nova_ucebnice_id}) ''')
    conn.commit()


def uloz_novou_ucebnici(ucebnice, jazyk_id,cursor):
    # conn, cursor = pripojeni_db()
    # při vkládání nového studenta
    cursor.execute(f'''INSERT INTO UCEBNICE values (null,'{ucebnice}', {jazyk_id}) ''')
    return cursor.execute(f'''SELECT ID FROM UCEBNICE WHERE NAZEV = '{ucebnice}' ''').fetchone()[0]        
    # conn.commit()

def select_to_seznam(data):
    """
    pomocna funkce na prevod select s 1 sloupcem --> seznam
    """
    # [(jmeno1,), (jmeno2,), (jmeno3,)] --> [jmeno1, jemno2, jmeno3]
    seznam = []   
    for polozka in data:
        seznam.append(polozka[0])
    return seznam

def seznam_studentu():    
    """
    - seznam vsech studentu; 
    VSTUP: bez parametru
    VYSTUP: seznam studentu - [student1, student2]
    """  
    conn, cursor = pripojeni_db()
    cursor.execute(f''' SELECT jmeno from osoby''')     
    return select_to_seznam(cursor.fetchall())

def seznam_ucebnic(jazyk):
    """
     - seznam vsech ucebnic daneho jazyku
    VSTUP: jayzk - retezec
    VYSTUP: seznam ucebnic - [ucebnice1, ucebnice2,...]
    """
    conn, cursor = pripojeni_db()
    cursor.execute(f''' select u.nazev from ucebnice u
	                        join jazyky j on u.jazyk_id = j.id
                        where j.nazev = '{jazyk}' order by j.nazev''')     
    return select_to_seznam(cursor.fetchall())

def seznam_lekci(ucebnice):
    """
    - seznam vsech lekci dane ucebnice
    VSTUP: ucebnice - retezec
    VYSTUP: seznam dvojic - [(id1, lekce1),(id2, lekce2)]
    """
    conn, cursor = pripojeni_db()
    cursor.execute(f''' select l.id, l.nazev from ucebnice u
	                        join lekce l on l.ucebnice_id = u.id
                    where u.nazev = '{ucebnice}'
                    order by l.cislo
                    ''')     
    return cursor.fetchall()

def jazyky_studenta(jmeno_studenta):
    """
    - seznam vsech jazyku daneho studenta
    VSTUP: jmeno_studenta - retezec
    VYSTUP: [jazyk1, jazyk2, ....]
    """      
    conn, cursor = pripojeni_db()
    try:
        cursor.execute(f''' SELECT id from osoby where jmeno ='{jmeno_studenta}'  ''')
        id_studenta = cursor.fetchone()[0]
    except:
        return f"Student jménem {jmeno_studenta} není v databázi"
    cursor.execute(f''' SELECT j.nazev from jazyky j join osoby_jazyky oj on oj.jazyk_id = j.id where oj.osoba_id={id_studenta}''')    
    return select_to_seznam(cursor.fetchall())


# vypíše nápovědu ke konkrétní funkci
# help(jazyky_studenta)
# help(seznam_studentu)
