import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO
import tkinter.messagebox
from tkinter import messagebox
import prace_s_db as db

def nova_ucebnice(self): 
    self.ucebnice_nova = tk.Toplevel()
    self.ucebnice_nova.title("Nová učebnice")

    self.nadpis = tk.Label(self.ucebnice_nova, text="Jazyk: " + self.akt_jazyk.get(), font="Ariel 14", bg="red")
    self.nadpis.grid(row=0, columnspan=4, sticky=W+E)

    self.mezera = tk.Label(self.ucebnice_nova, text="", font="Ariel 10")
    self.mezera.grid(row=1, column=0)

    self.popisek = tk.Label(self.ucebnice_nova, text="Název učebnice:", font="Ariel 10")
    self.popisek.grid(row=2, column=0)

    self.nova_uc = tk.Entry(self.ucebnice_nova, width=25)
    self.nova_uc.grid(row=2, column=1, columnspan=2 )

    self.Ulozit = tk.Button(self.ucebnice_nova, width=20, text="OK", fg="green", command=lambda: self.ulozit_ucebnice(self.akt_jazyk.get(), self.nova_uc.get()))
    self.Ulozit.grid(row=2, column=3, sticky=W)

    
    self.mezera = tk.Label(self.ucebnice_nova, text="", font="Ariel 10")
    self.mezera.grid(row=3, column=0)













