import pandas as pd
import pathlib
from prace_s_db import pripojeni_db

soubor = 'test_excel.xlsx'

def import_slovicek(lekce_id, soubor):
    try:
        soubor_typ = pathlib.Path(soubor).suffix
        
        if "xl" in soubor_typ:
            seznam_slov = pd.read_excel(soubor, engine = 'openpyxl')

        elif "csv" or "txt" in soubor_typ:
            seznam_slov = pd.read_csv(soubor, delimiter=';', usecols=(0,1))
            

        seznam_slov['lekce_id'] = lekce_id

        conn, cursor = pripojeni_db()
        seznam_slov.to_sql("SLOVICKA", conn, if_exists='append', index=False)
        

    except ValueError:
            print("Nepodporovaný formát. Podporované formáty jsou xls,xlsx,csv,txt")


#import_slovicek(99,soubor)

#conn, cursor = pripojeni_db()
#data = cursor.execute(f'SELECT count(*) FROM SLOVICKA WHERE lekce_id = "99";')
#print(data.fetchall())



