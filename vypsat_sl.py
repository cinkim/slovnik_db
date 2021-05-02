import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO
import tkinter.messagebox
from tkinter import messagebox

def vypis_slovicka(self,seznam_slovicek):
        self.slovicka = tk.Toplevel()
        self.slovicka.title("Slovíčka lekce: " + self.akt_Lekce)

        self.nadpis = tk.Label(self.slovicka, text="Jazyk: " + self.akt_j + "\nUčebnice:" + self.akt_ucebnice + "\nLekce:" + self.akt_Lekce, font="Ariel 14", bg="red")
        self.nadpis.grid(row=0, columnspan=3, sticky=W+E)
         
        self.tree_slovicka = ttk.Treeview(self.slovicka, column=("česky", "nečesky"), height=20, selectmode='browse')
        self.tree_slovicka['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_slovicka.grid(row=13, columnspan=3)
        
        self.tree_slovicka.heading("#0", text="#\n ")
        self.tree_slovicka.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_slovicka.heading("česky", text="CZ\n ")
        self.tree_slovicka.column("česky", minwidth=0, width=270, stretch=NO, anchor='center')

        #self.tree_slovicka.heading("nečesky", text="nečesky\n ")
        self.tree_slovicka.heading("nečesky", text=self.akt_j.upper() + "\n")
        self.tree_slovicka.column("nečesky", minwidth=0, width=270, stretch=NO, anchor='center')

        self.mez = tk.Label(self.slovicka, text="", height=1)
        self.mez.grid(row=17, column=0)

        self.Konec = tk.Button(self.slovicka, width=20, text="Konec", fg="red", command=self.slovicka.destroy)
        self.Konec.grid(row=19, column=0, sticky=W)
        """
        for ii in self.tree_slovicka.get_children():
            self.tree_slovicka.delete(ii)
        """
        pozice = 0
        for zaznam in seznam_slovicek:
            self.tree_slovicka.insert("", "end", text=pozice, values=(zaznam[1], zaznam[2]))
            pozice += 1

"""
def nacti_lekci(self):
        try:
                self.akt_Lekce = str(self.tree_Lekce.item(self.tree_Lekce.focus())["values"][1])
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
"""
