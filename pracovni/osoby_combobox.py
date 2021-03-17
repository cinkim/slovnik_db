# -*- coding: utf-8 -*-
from tkinter import *


def vypis_osobu():
    vybrana_osoba = aktualni_osoba.get()
    print(vybrana_osoba)

hlavni_okno = Tk()
hlavni_okno.title("Slovník")

osoby = ["Adam", "Filip", "Pepa"]

aktualni_osoba = StringVar()   #promenna pro parametr variable v comboboxu

aktualni_osoba.set(osoby[0])   # nastavuje prvního ze seznamu jako vybraného

# lambda funkce jako parametr widgetů.... umožnuje spouštět funkce s parametrem i bez

for osoba in osoby:  
    Radiobutton(hlavni_okno, text=osoba, variable=aktualni_osoba, value=osoba, command=lambda: vypis_osobu()).pack(anchor=W)


mainloop()