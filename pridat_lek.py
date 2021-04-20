import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO
import tkinter.messagebox
from tkinter import messagebox
import prace_s_db as db

def nova_lekce(self):
        
    self.lekce_nova = tk.Toplevel()
    self.lekce_nova.title("Nová lekce")

    self.nadpis = tk.Label(self.lekce_nova, text="Jazyk: " + self.akt_j + "\nUčebnice:" + self.akt_ucebnice, font="Ariel 14", bg="red")
    self.nadpis.grid(row=0, columnspan=6, sticky=W+E)

    self.mezera = tk.Label(self.lekce_nova, text="", font="Ariel 10")
    self.mezera.grid(row=1, column=0)

    self.popisek = tk.Label(self.lekce_nova, text="Číslo lekce:", font="Ariel 10")
    self.popisek.grid(row=2, column=0)

    self.cl = StringVar()
    self.nova_lek_cislo = tk.Entry(self.lekce_nova, width=10, textvariable=self.cl)
    self.nova_lek_cislo.grid(row=2, column=1 )

    self.popisek = tk.Label(self.lekce_nova, text="Název lekce:", font="Ariel 10")
    self.popisek.grid(row=2, column=2)

    self.nl = StringVar()
    self.nova_lek = tk.Entry(self.lekce_nova, width=25, textvariable=self.nl)
    self.nova_lek.grid(row=2, column=3, columnspan=2 )

    self.Ulozit = tk.Button(self.lekce_nova, width=20, text="Uložit", fg="green", command=self.ulozit_lekci)
    self.Ulozit.grid(row=2, column=5, sticky=W)
    
    self.mezera = tk.Label(self.lekce_nova, text="", font="Ariel 10")
    self.mezera.grid(row=3, column=0)

    self.Konec = tk.Button(self.lekce_nova, width=20, text="Konec", fg="green", command=self.lekce_nova.destroy)
    self.Konec.grid(row=4, column=0,  sticky=W)


def smazat_Lek(self):
    print("Doprogramovat")

def ulozit_Lek(self):
    if (self.nova_lek.get() or self.nova_lek_cislo.get()) == "":
        tk.messagebox.showwarning("ERROR", "Vyplňte číslo a název lekce")
        return
    try:
        db.uloz_lekci(self.akt_j, self.akt_ucebnice, self.nova_lek.get(), int(self.nova_lek_cislo.get()))        
    except ValueError:
        tk.messagebox.showwarning("ERROR", "Zadej správně číslo lekce.")
        return
    
    self.nacti_lekce()
    self.cl.set("")
    self.nl.set("")
    # nastavení vybraného řádku právě vložené lekce child_id ... ITEM ID vložené lekce
    # child_id = self.tree_Lekce.get_children()[-1] # poslední řádek
    # child_id = self.tree_Lekce.get_children()[self.seznam_lekci.index((int(cislo),nazev))] # máme řazené tak hledá ID pro danou hodnotu
    # self.tree_Lekce.selection_set(child_id)










