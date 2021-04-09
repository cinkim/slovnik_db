import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES
import tkinter.messagebox

def nastav_studenta(self):
    self.top_student = tk.Toplevel()
    self.top_student.title("Nastavení studenta")

    self.nastaveni = tk.LabelFrame(self.top_student, text="Nastavení studenta", font="Arial 14")
    self.nastaveni.grid(row=1, column=0, sticky=N)
    self.nastav = tk.Label(self.nastaveni, text=self.akt_student, font="Arial 14", fg="blue")
    self.nastav.grid(row=2, columnspan=2, sticky=W+E)

    self.entr_1 = StringVar()
    self.vstup1 = tk.Entry(self.nastaveni, width=10, justify="center", textvariable=self.entr_1)
    self.vstup1.grid(row=3, column=0, sticky=W)
    self.popis1 = tk.Label(self.nastaveni, text="Libovolný text 1")
    self.popis1.grid(row=3, column=1, sticky=W)

    self.entr_2 = StringVar()
    self.vstup2 = tk.Entry(self.nastaveni, width=10, justify="center", textvariable=self.entr_2)
    self.vstup2.grid(row=4, column=0, sticky=W)
    self.popis2 = tk.Label(self.nastaveni, text="Libovolný text 2")
    self.popis2.grid(row=4, column=1, sticky=W)

    self.entr_3 = StringVar()
    self.vstup3 = tk.Entry(self.nastaveni, width=10, justify="center", textvariable=self.entr_3)
    self.vstup3.grid(row=5, column=0, sticky=W)
    self.popis3 = tk.Label(self.nastaveni, text="Libovolný text 3")
    self.popis3.grid(row=5, column=1, sticky=W)

    self.ulozit_nastaveni = tk.Button(self.nastaveni, text="Uložit nastavení", command=self.nastaveni, fg="blue", font="Arial 8", width=20)
    self.ulozit_nastaveni.grid(row=10, columnspan=2, sticky=W+E)

    self.ulozit_Konec = tk.Button(self.nastaveni, text="Konec", command=self.top_student.destroy, fg="red", font="Arial 8", width=20)
    self.ulozit_Konec.grid(row=11, columnspan=2, sticky=W+E)