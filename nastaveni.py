import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES
import tkinter.messagebox

def nastav_studenta(self):
    self.top_student = tk.Toplevel()
    self.top_student.title("Nastavení studenta")

    self.nastaveni = tk.LabelFrame(self.top_student, text="Nastavení studenta", font="Arial 14")
    self.nastaveni.grid(row=1, column=0, sticky=N)
    self.nastav = tk.Label(self.nastaveni, text="Student", font="Arial 8")
    self.nastav.grid(row=2, column=0, sticky=N)

    

    """
    self.Student = tk.Label(self.top_student, text="Min. End Format Höhe", width=20, font="Arial 8")
    self.min_vyska_obalky.grid(row=0, column=0, sticky=W)
    """

    self.ulozit_nastaveni = tk.Button(self.nastaveni, text="Uložit nastavení", command=self.nastaveni, fg="blue", font="Arial 8", width=20)
    self.ulozit_nastaveni.grid(row=3, column=2, sticky=W)