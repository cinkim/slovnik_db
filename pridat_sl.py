import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO
import tkinter.messagebox

def new_words(self):
        self.words = tk.Toplevel()
        self.words.title("Nová slovíčka")

        self.cesky = tk.Label(self.words, text="Česky", font="Ariel 10")
        self.cesky.grid(row=0, column=0)
        self.mez = tk.Label(self.words, text="X", width=5)
        self.mez.grid(row=1, column=1)
        self.jinak = tk.Label(self.words, text="Nečesky", font="Ariel 10")
        self.jinak.grid(row=0, column=2)

        self.w1 = StringVar()
        self.wc = tk.Entry(self.words, width=30, justify="center", textvariable=self.w1)
        self.wc.grid(row=1, column=0, sticky=W)
        self.wc.config(state=NORMAL)

        self.w2 = StringVar()
        self.wnc = tk.Entry(self.words, width=30, justify="center", textvariable=self.w2)
        self.wnc.bind("<Return>", self.dalsi_slovo)
        self.wnc.grid(row=1, column=2, sticky=W)
        self.wnc.config(state=NORMAL)

        self.tree_zaznamy = ttk.Treeview(self.words, column=("česky", "nečesky"), height=20, selectmode='browse')
        self.tree_zaznamy['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_zaznamy.grid(row=2, columnspan=3)
        
        self.tree_zaznamy.heading("#0", text="#\n ")
        self.tree_zaznamy.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_zaznamy.heading("česky", text="Česky\n ")
        self.tree_zaznamy.column("česky", minwidth=0, width=204, stretch=NO, anchor='center')

        self.tree_zaznamy.heading("nečesky", text="Nečesky\n ")
        self.tree_zaznamy.column("nečesky", minwidth=0, width=204, stretch=NO, anchor='center')

        self.mez = tk.Label(self.words, text="", height=1)
        self.mez.grid(row=7, column=0)

        self.Ulozit = tk.Button(self.words, width=20, text="Uložit", fg="green", command=self.pridat_Ulozit)
        self.Ulozit.grid(row=7, column=0, sticky=W)

        self.mez = tk.Label(self.words, text="", height=1)
        self.mez.grid(row=8, column=0)

        self.Konec = tk.Button(self.words, width=20, text="Konec", fg="red", command=self.pridat_Konec)
        self.Konec.grid(row=9, column=0, sticky=W)


