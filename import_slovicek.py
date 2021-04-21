import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

import pandas as pd
import pathlib
from prace_s_db import pripojeni_db


def import_sl(self):
    file_path = filedialog.askopenfilename()
    print(file_path)

    try:
        soubor_typ = pathlib.Path(file_path).suffix       
        if "xl" in soubor_typ:
            seznam_slov = pd.read_excel(file_path, engine = 'openpyxl')

        elif "csv" or "txt" in soubor_typ:
            seznam_slov = pd.read_csv(file_path, delimiter=';', usecols=(0,1))
    
    except ValueError:
        tk.messagebox.showwarning("ERROR", "Nepodporovaný typ souboru\naplikace podporuje pouze soubory typu\ncsv, txt, xls")
        return
    print("haha")
    """
    seznam_slov['lekce_id'] = lekce_id

    conn, cursor = pripojeni_db()
    seznam_slov.to_sql("SLOVICKA", conn, if_exists='append', index=False)
    """

#import_slovicek(99,soubor)

#conn, cursor = pripojeni_db()
#data = cursor.execute(f'SELECT count(*) FROM SLOVICKA WHERE lekce_id = "99";')
#print(data.fetchall())



