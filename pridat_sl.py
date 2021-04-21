import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO
import tkinter.messagebox
from tkinter import messagebox

def new_words(self):
        self.words = tk.Toplevel()
        self.words.title("Nová slovíčka")
        try:
                pozor = "POZOR: Ukládáš data do"
                jaz = self.akt_j + ":  " + self.akt_ucebnice
                lek = "Lekce: " + self.akt_Lekce
        except AttributeError:
                tk.messagebox.showwarning("ERROR", "Nejsou vybrané všechny parametry.")
                return
        self.nadpis = tk.Label(self.words, text=pozor, font="Ariel 14", bg="red")
        self.nadpis.grid(row=1, columnspan=3, sticky=W+E)

        self.struktura = tk.Label(self.words, text=jaz, font="Ariel 14", bg="red")
        self.struktura.grid(row=2, columnspan=3, sticky=W+E)

        self.struktura = tk.Label(self.words, text=lek, font="Ariel 14", bg="red")
        self.struktura.grid(row=3, columnspan=3, sticky=W+E)

        self.mez1 = tk.Label(self.words, text="")
        self.mez1.grid(row=4, column=0)

        self.mez = tk.Label(self.words, text="X", width=5)
        self.mez.grid(row=12, column=1)
        """
        self.jinak = tk.Label(self.words, text="", font="Ariel 10")
        self.jinak.grid(row=11, column=2)
        """
        self.w1 = StringVar()
        self.wc = tk.Entry(self.words, width=40, justify="center", textvariable=self.w1)
        self.wc.grid(row=12, column=0, sticky=W)
        self.wc.config(state=NORMAL)

        self.w2 = StringVar()
        self.wnc = tk.Entry(self.words, width=40, justify="center", textvariable=self.w2)
        self.wnc.bind("<Return>", self.dalsi_slovo)
        self.wnc.grid(row=12, column=2, sticky=W)
        self.wnc.config(state=NORMAL)

        self.tree_slovicka = ttk.Treeview(self.words, column=("česky", "nečesky"), height=20, selectmode='browse')
        self.tree_slovicka['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_slovicka.grid(row=13, columnspan=3)
        
        self.tree_slovicka.heading("#0", text="#\n ")
        self.tree_slovicka.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_slovicka.heading("česky", text="Česky\n ")
        self.tree_slovicka.column("česky", minwidth=0, width=270, stretch=NO, anchor='center')

        self.tree_slovicka.heading("nečesky", text="Nečesky\n ")
        self.tree_slovicka.column("nečesky", minwidth=0, width=270, stretch=NO, anchor='center')

        self.mez = tk.Label(self.words, text="", height=1)
        self.mez.grid(row=17, column=0)

        self.Ulozit = tk.Button(self.words, width=20, text="Uložit", fg="green", command=self.ulozit)
        self.Ulozit.grid(row=17, column=0, sticky=W)
        self.nacist_ze_souboru = tk.Button(self.words, width=20, text="Načíst ze souboru", fg="green", command=self.nacist)
        self.nacist_ze_souboru.grid(row=17, column=2, sticky=E)

        self.mez = tk.Label(self.words, text="", height=1)
        self.mez.grid(row=18, column=0)

        self.Konec = tk.Button(self.words, width=20, text="Konec", fg="red", command=self.words.destroy)
        self.Konec.grid(row=19, column=0, sticky=W)


def nacti_lekci(self):
        try:
                self.akt_Lekce = str(self.tree_Lekce.item(self.tree_Lekce.focus())["values"][0])
                new_words(self)
        except IndexError:
                tk.messagebox.showwarning("ERROR", "Nejdříve vyber jazyk/učebnici/lekci.")
                return
        except tkinter.TclError:
                tk.messagebox.showwarning("ERROR", "Nejdříve vyber jazyk/učebnici/lekci.")
                return
        except AttributeError:
                tk.messagebox.showwarning("ERROR", "Nejdříve vyber jazyk/učebnici/lekci.")
                return
def ulozit(self):
        if messagebox.askyesno("???", "Uložit slovíčka?") == True:
                print("Budu ukládat - doprogramuj")
        else:
                pass


