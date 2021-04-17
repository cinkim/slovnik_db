import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO
import tkinter.messagebox
from tkinter import messagebox
import prace_s_db as db

def nova_lekce(self):
        
    self.lekce_nova = tk.Toplevel()
    self.lekce_nova.title("Nová lekce")

    self.nadpis = tk.Label(self.lekce_nova, text="Jazyk: " + self.akt_jazyk.get() + "\nUčebnice:" + self.akt_ucebnice, font="Ariel 14", bg="red")
    self.nadpis.grid(row=0, columnspan=6, sticky=W+E)

    self.mezera = tk.Label(self.lekce_nova, text="", font="Ariel 10")
    self.mezera.grid(row=1, column=0)

    self.popisek = tk.Label(self.lekce_nova, text="Číslo lekce:", font="Ariel 10")
    self.popisek.grid(row=2, column=0)

    self.nova_lek_cislo = tk.Entry(self.lekce_nova, width=10)
    self.nova_lek_cislo.grid(row=2, column=1 )

    self.popisek = tk.Label(self.lekce_nova, text="Název lekce:", font="Ariel 10")
    self.popisek.grid(row=2, column=2)

    self.nova_lek = tk.Entry(self.lekce_nova, width=25)
    self.nova_lek.grid(row=2, column=3, columnspan=2 )

    self.Ulozit = tk.Button(self.lekce_nova, width=20, text="Uložit", fg="green", command=lambda: self.ulozit_lekci(self.akt_jazyk.get(), self.akt_ucebnice, self.nova_lek_cislo.get(), self.nova_lek.get()))
    self.Ulozit.grid(row=2, column=5, sticky=W)
    
    self.mezera = tk.Label(self.lekce_nova, text="", font="Ariel 10")
    self.mezera.grid(row=3, column=0)


    """
    self.Konec = tk.Button(self.lekce, width=20, text="Konec", fg="green", command=self.lekce_Konec)
    self.Konec.grid(row=4, column=3,  sticky=W)
    """









