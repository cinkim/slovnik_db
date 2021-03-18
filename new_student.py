
import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox


def zaloz_studenta(self):
        self.st = tk.Toplevel()
        self.st.title("Nový student")

        self.newst = StringVar()
        self.new_st = tk.Entry(self.st, width=30, justify="center", textvariable=self.newst)
        self.new_st.grid(row=3, column=0, sticky=W)
        self.new_st.config(state=NORMAL)
        self.new_popis = tk.Label(self.st, text="Jméno studenta", width=20, font="Arial 8")
        self.new_popis.grid(row=3, column=1, sticky=W)


        self.button_uloz = tk.Button(self.st, text="Uložit", command=self.novy, fg="blue", font="Arial 8", width=20)
        self.button_uloz.grid(row=9, column=0, sticky=W)

        self.button_Konec = tk.Button(self.st, text="Konec", command=self.st.destroy, fg="red", font="Arial 8", width=20)
        self.button_Konec.grid(row=10, column=0, sticky=W)


def ulozit_noveho_studenta(self):
    new = self.new_st.get()
    with open("studenti.txt", mode="a", encoding="utf-8") as st:
        print(new, file=st)
    tk.messagebox.showwarning("Hotovo", "Přidán nový student.")
    self.newst.set("")
