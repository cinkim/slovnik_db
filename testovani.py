import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES, VERTICAL
import tkinter.messagebox

import prace_s_db as db

def tes(self):
    self.akt_Lekce = str(self.tree_Lekce.item(self.tree_Lekce.focus())["values"][1])
    self.top_test = tk.Toplevel()
    self.top_test.title("Testování lekce: "+ self.akt_Lekce)

    self.testovani = tk.Label(self.top_test, text="Student: " + self.akt_student + "\nJazyk : " + self.akt_j + "\nUčebnice :" + self.akt_ucebnice + "\nLekce:" + self.akt_Lekce, font="Ariel 14", bg="red")
    self.testovani.grid(row=1, columnspan=4, sticky=W+E)

    self.M_tes = tk.Label(self.top_test, text="")
    self.M_tes.grid(row=2, column=0)

    self.ceskytext = StringVar()
    self.cesky = tk.Label(self.top_test, textvariable=self.ceskytext, width=25, font="Arial 12")
    self.cesky.grid(row=3, column=0)

    self.pr = StringVar()
    self.preklad = tk.Entry(self.top_test, width=25, font="Arial 12", textvariable=self.pr)
    self.archiv = self.preklad.get()
    self.preklad.bind("<Return>", self.vyhodnot)
    self.preklad.grid(row=3, column=1)
    self.preklad.config(state=NORMAL)

    self.M_tes = tk.Label(self.top_test, text="")
    self.M_tes.grid(row=4, column=0)

    self.M_tes = tk.Label(self.top_test, text="Otázka")
    self.M_tes.grid(row=5, column=0)

    self.M_tes = tk.Label(self.top_test, text="Tvoje odpověď")
    self.M_tes.grid(row=5, column=1)

    self.M_tes = tk.Label(self.top_test, text="Správná odpověď")
    self.M_tes.grid(row=5, column=2)

    self.M_tes = tk.Label(self.top_test, text="Hodnocení")
    self.M_tes.grid(row=5, column=3)

    self.text1 = tk.Text(self.top_test, font="Arial 14", width=20)
    self.text1.grid(row=6, column=0)

    self.text2 = tk.Text(self.top_test, font="Arial 14", width=20)
    self.text2.grid(row=6, column=1)

    self.text3 = tk.Text(self.top_test, font="Arial 14", width=20)
    self.text3.grid(row=6, column=2)

    self.text4 = tk.Text(self.top_test, font="Arial 14", width=20)
    self.text4.grid(row=6, column=3)

    self.mez = tk.Label(self.top_test, text="", height=1)
    self.mez.grid(row=7, column=0)

    self.spustit = tk.Button(self.top_test, text="Spustit Test", command=self.Testuj, fg="blue", font="Ariel 8", width=20)
    self.spustit.grid(row=8, column=0, sticky=W)

    self.Konec = tk.Button(self.top_test, text="Konec", command=self.top_test.destroy, fg="red", font="Arial 8", width=20)
    self.Konec.grid(row=9, column=0, sticky=W)


def spust_test(self):
    self.slovicko = self.slovnik.k_testovani[self.slovnik.aktualni_slovo]
    self.cz = self.slovicko[1]
    self.ceskytext.set(self.cz)
    self.slovnik.aktualni_slovo+=1
    self.preklad.focus_set()
    self.preklad.config(state=NORMAL)
    return

def vyhodnoceni(self):
    spravne = self.slovicko[3]
    spatne = self.slovicko[4]
    vys = []
    vys_do_vypisu = []
    if self.slovicko[2].lower() == self.preklad.get().lower():
        self.ok = True       
        spravne +=1
        vys.append(self.slovicko[0])
        vys.append(self.slovicko[1])
        vys.append(self.slovicko[2])
        vys.append(spravne)
        vys.append(self.slovicko[4])

        vys_do_vypisu.append(self.slovicko[1])
        vys_do_vypisu.append(self.preklad.get())
        vys_do_vypisu.append(self.slovicko[2])
        vys_do_vypisu.append("Dobře")

        self.slovnik.vysledky_db.append(vys)
        self.slovnik.vysledky.append(vys_do_vypisu)
        self.pr.set("")
        ukaz(self)
        spust_test(self)
    else:
        self.ok = False
        spatne +=1
        vys.append(self.slovicko[0])
        vys.append(self.slovicko[1])
        vys.append(self.slovicko[2])
        vys.append(self.slovicko[3])
        vys.append(spatne)

        vys_do_vypisu.append(self.slovicko[1])
        vys_do_vypisu.append(self.preklad.get())
        vys_do_vypisu.append(self.slovicko[2])
        vys_do_vypisu.append("Špatně")

        self.slovnik.vysledky_db.append(vys)
        self.slovnik.vysledky.append(vys_do_vypisu)
        self.pr.set("")
        ukaz(self)
        spust_test(self)
        
def ukaz(self):
    smaz(self)
    try:
        for vysledek in self.slovnik.vysledky.reverse():
            if vysledek[3] == "Dobře":
                self.text1.config(state=NORMAL)
                self.text2.config(state=NORMAL)
                self.text3.config(state=NORMAL)
                self.text4.config(state=NORMAL)

                self.text1.insert(tk.END,vysledek[0])
                self.text1.insert(tk.END, "\n")
                self.text2.insert(tk.END,vysledek[1])
                self.text2.insert(tk.END, "\n")

                self.text3.insert(tk.END,vysledek[2])
                self.text3.insert(tk.END, "\n")

                self.text4.tag_config("modre", foreground="blue")
                self.text4.insert(tk.END,vysledek[3], "modre")
                self.text4.insert(tk.END, "\n")

                self.text1.config(state=DISABLED)
                self.text2.config(state=DISABLED)
                self.text3.config(state=DISABLED)
                self.text4.config(state=DISABLED)

            else:
                self.text1.config(state=NORMAL)
                self.text2.config(state=NORMAL)
                self.text3.config(state=NORMAL)
                self.text4.config(state=NORMAL)

                self.text1.insert(tk.END,vysledek[0])
                self.text1.insert(tk.END, "\n")

                self.text2.insert(tk.END,vysledek[1])
                self.text2.insert(tk.END, "\n")

                self.text3.insert(tk.END,vysledek[2])
                self.text3.insert(tk.END, "\n")

                self.text4.tag_config("cervena", foreground="red")
                self.text4.insert(tk.END,vysledek[3], "cervena")
                self.text4.insert(tk.END, "\n")

                self.text1.config(state=DISABLED)
                self.text2.config(state=DISABLED)
                self.text3.config(state=DISABLED)
                self.text4.config(state=DISABLED)
    except TypeError:
        for vysledek in self.slovnik.vysledky:
            if vysledek[3] == "Dobře":
                self.text1.config(state=NORMAL)
                self.text2.config(state=NORMAL)
                self.text3.config(state=NORMAL)
                self.text4.config(state=NORMAL)

                self.text1.insert(tk.END,vysledek[0])
                self.text1.insert(tk.END, "\n")
                self.text2.insert(tk.END,vysledek[1])
                self.text2.insert(tk.END, "\n")

                self.text3.insert(tk.END,vysledek[2])
                self.text3.insert(tk.END, "\n")

                self.text4.tag_config("modre", foreground="blue")
                self.text4.insert(tk.END,vysledek[3], "modre")
                self.text4.insert(tk.END, "\n")

                self.text1.config(state=DISABLED)
                self.text2.config(state=DISABLED)
                self.text3.config(state=DISABLED)
                self.text4.config(state=DISABLED)

            else:
                self.text1.config(state=NORMAL)
                self.text2.config(state=NORMAL)
                self.text3.config(state=NORMAL)
                self.text4.config(state=NORMAL)

                self.text1.insert(tk.END,vysledek[0])
                self.text1.insert(tk.END, "\n")

                self.text2.insert(tk.END,vysledek[1])
                self.text2.insert(tk.END, "\n")

                self.text3.insert(tk.END,vysledek[2])
                self.text3.insert(tk.END, "\n")

                self.text4.tag_config("cervena", foreground="red")
                self.text4.insert(tk.END,vysledek[3], "cervena")
                self.text4.insert(tk.END, "\n")

                self.text1.config(state=DISABLED)
                self.text2.config(state=DISABLED)
                self.text3.config(state=DISABLED)
                self.text4.config(state=DISABLED)



def smaz(self):
    self.text1.config(state=NORMAL)
    self.text2.config(state=NORMAL)
    self.text3.config(state=NORMAL)
    self.text4.config(state=NORMAL)

    self.text1.delete(1.0, tk.END)
    self.text2.delete(1.0, tk.END)
    self.text3.delete(1.0, tk.END)
    self.text4.delete(1.0, tk.END)

    self.text1.config(state=DISABLED)
    self.text2.config(state=DISABLED)
    self.text3.config(state=DISABLED)
    self.text4.config(state=DISABLED)


