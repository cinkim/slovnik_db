import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES, VERTICAL
import tkinter.messagebox

import prace_s_db

def tes(self):
    self.top_test = tk.Toplevel()
    self.top_test.title("Testování")

    self.testovani = tk.LabelFrame(self.top_test, text="Testování studenta", font="Arial 14")
    self.testovani.grid(row=1, column=0, sticky=N)
    self.nastav = tk.Label(self.testovani, text=self.akt_student, font="Arial 14", fg="blue")
    self.nastav.grid(row=2, columnspan=2, sticky=W+E)

    self.Konec = tk.Button(self.testovani, text="Konec", command=self.top_test.destroy, fg="red", font="Arial 8", width=20)
    self.Konec.grid(row=11, columnspan=2, sticky=W+E)