import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES, VERTICAL
import tkinter.messagebox
import random
import prace_s_db
import prace_s_db as db


def tes(self):
    self.akt_Lekce = str(self.tree_Lekce.item(self.tree_Lekce.focus())["values"][1])
    self.top_test = tk.Toplevel()
    self.top_test.title("Testování lekce: "+ self.akt_Lekce)
    self.top_test.grid_columnconfigure(0, weight=4)
    self.top_test.grid_columnconfigure(1, weight=4)
    self.top_test.grid_columnconfigure(2, weight=4)
    self.top_test.grid_columnconfigure(3, weight=4)

    self.top_test.grid_rowconfigure(1, weight=0)
    self.top_test.grid_rowconfigure(2, weight=1)
    self.top_test.grid_rowconfigure(3, weight=0)
    self.top_test.grid_rowconfigure(4, weight=1)
    self.top_test.grid_rowconfigure(5, weight=0)
    self.top_test.grid_rowconfigure(6, weight=1)
    self.top_test.grid_rowconfigure(7, weight=1)
    self.top_test.grid_rowconfigure(8, weight=0)
    self.top_test.grid_rowconfigure(9, weight=0)

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

    self.uspech = StringVar()
    self.akt_uspech = tk.Label(self.top_test, textvariable=self.uspech, width=25, font="Arial 12")
    self.akt_uspech.grid(row=3, column=2)

    self.M_tes = tk.Label(self.top_test, text="")
    self.M_tes.grid(row=4, column=0)

    self.M_tes = tk.Label(self.top_test, text="Otázka")
    self.M_tes.grid(row=5, column=0)

    self.M_tes = tk.Label(self.top_test, text="Tvoje odpověď")
    self.M_tes.grid(row=5, column=1, )

    self.M_tes = tk.Label(self.top_test, text="Správná odpověď")
    self.M_tes.grid(row=5, column=2)

    self.M_tes = tk.Label(self.top_test, text="Hodnocení")
    self.M_tes.grid(row=5, column=3)

    self.text1 = tk.Text(self.top_test, font="Arial 10", width=33, height=2)
    self.text1.grid(row=6, column=0)

    self.text2 = tk.Text(self.top_test, font="Arial 10", width=33, height=2)
    self.text2.grid(row=6, column=1)

    self.text3 = tk.Text(self.top_test, font="Arial 10", width=33, height=2)
    self.text3.grid(row=6, column=2)

    self.text4 = tk.Text(self.top_test, font="Arial 10", width=33, height=2)
    self.text4.grid(row=6, column=3)

    self.mez = tk.Label(self.top_test, text="")
    self.mez.grid(row=7, column=0)

    self.spustit = tk.Button(self.top_test, text="Spustit Test", command=self.Testuj, fg="blue", font="Ariel 8", width=20)
    self.spustit.grid(row=8, column=0, sticky=W)

    self.Konec = tk.Button(self.top_test, text="Konec", command=self.ukonci_top_test, fg="red", font="Arial 8", width=20)
    self.Konec.grid(row=9, column=0, sticky=W)

def nacti(self):
    try:
        self.akt_Lekce = str(self.tree_Lekce.item(self.tree_Lekce.focus())["values"][1])
        
    except IndexError:
        tk.messagebox.showwarning("ERROR", "Nejdříve vyber lekci.")
        return

    if self.slovnik.typ_prekladu == 1:
        v1(self)
    elif self.slovnik.typ_prekladu == 2:
        v2(self)
    elif self.slovnik.typ_prekladu == 3:
        v1(self)
    else:
        tk.messagebox.showwarning("ERROR", "Chyba v nastavení.")
        return

    
def v1(self): # cz/cizí
    self.slovnik.k_testovani = prace_s_db.slovicka_lekce(self.akt_Lekce, self.akt_student)
    random.shuffle(self.slovnik.k_testovani)
    random.shuffle(self.slovnik.k_testovani)
    prvek = 0
    for poradi in self.slovnik.k_testovani:
        if (prvek < self.slovnik.pocet_k_testu) and (poradi[3] < self.slovnik.pocet_spravnych):
            self.slovnik.testuj.append(poradi)
            prvek +=1
        else:
            self.slovnik.netestuj.append(poradi)
    self.slovnik.k_testovani = self.slovnik.netestuj
    self.slovnik.netestuj = []
    self.slovnik.testuj = self.slovnik.testuj
    self.slovnik.testuj = self.slovnik.testuj * self.slovnik.pocet_kol_testu
    random.shuffle(self.slovnik.testuj)

def v2(self): # cizí/cz
    self.slovnik.k_testovani = prace_s_db.slovicka_lekce(self.akt_Lekce, self.akt_student)
    random.shuffle(self.slovnik.k_testovani)
    random.shuffle(self.slovnik.k_testovani)

def v3(self): # mix
    self.slovnik.k_testovani = prace_s_db.slovicka_lekce(self.akt_Lekce, self.akt_student)
    random.shuffle(self.slovnik.k_testovani)
    random.shuffle(self.slovnik.k_testovani)
    


def spust_test(self): 
          
    self.slovicko = self.slovnik.testuj[self.slovnik.aktualni_slovo]
    self.cz = self.slovicko[1]
    self.ceskytext.set(self.cz)
    
    self.preklad.focus_set()
    self.preklad.config(state=NORMAL)
    return



def vyhodnoceni(self):
    if self.slovnik.typ_prekladu == 1:
        vyhodnoceni_v1(self)
    elif self.slovnik.typ_prekladu == 2:
        vyhodnoceni_v2(self)
    elif self.slovnik.typ_prekladu == 3:
        vyhodnoceni_v3(self)
    


def ukaz(self):
    smaz(self)

    mezivypocet = self.slovnik.pocet_sl_pro_procenta/100
    proc = self.slovnik.pocet_spravnych_pro_procenta/mezivypocet
    self.proc = str(round(proc, 2))

    self.text1.config(state=NORMAL)
    self.text2.config(state=NORMAL)
    self.text3.config(state=NORMAL)
    self.text4.config(state=NORMAL)
    mezi = self.slovnik.vysledky.reverse()
    if mezi == None:
        mezi = self.slovnik.vysledky

    for vysledek in mezi:
        if vysledek[3] == "Dobře":
            self.uspech.set("Aktuální úspěšnost: " + self.proc + " %")

            self.text1.tag_config("cerna", foreground="black", justify=CENTER)
            self.text1.insert(tk.END,vysledek[0], "cerna")
            self.text1.insert(tk.END, "\n")

            self.text2.tag_config("cerna", foreground="black", justify=CENTER)
            self.text2.insert(tk.END,vysledek[1], "cerna")
            self.text2.insert(tk.END, "\n")

            self.text3.tag_config("cerna", foreground="black", justify=CENTER)
            self.text3.insert(tk.END,vysledek[2], "cerna")
            self.text3.insert(tk.END, "\n")

            self.text4.tag_config("modre", foreground="blue", justify=CENTER)
            self.text4.insert(tk.END,vysledek[3], "modre")
            self.text4.insert(tk.END, "\n")
            mezi = []


        else:
            self.uspech.set("Aktuální úspěšnost: " + self.proc + " %")

            self.text1.tag_config("cerna", foreground="black",justify=CENTER)
            self.text1.insert(tk.END,vysledek[0], "cerna")
            self.text1.insert(tk.END, "\n")

            self.text2.tag_config("cerna", foreground="black",justify=CENTER)
            self.text2.insert(tk.END,vysledek[1], "cerna")
            self.text2.insert(tk.END, "\n")

            self.text3.tag_config("cerna", foreground="black",justify=CENTER)
            self.text3.insert(tk.END,vysledek[2], "cerna")
            self.text3.insert(tk.END, "\n")

            self.text4.tag_config("cervena", foreground="red", justify=CENTER)
            self.text4.insert(tk.END,vysledek[3], "cervena")
            self.text4.insert(tk.END, "\n")
            mezi = []
    self.slovnik.vysledky.reverse()
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
    return


def uloz_do_db(self):
    self.slovnik.vysledky_pro_ulozeni_do_db.append(self.akt_student)
    self.slovnik.vysledky_pro_ulozeni_do_db.append(self.akt_Lekce)
    self.slovnik.vysledky_pro_ulozeni_do_db.append(self.proc)
    sl = []
    for qq in self.slovnik.vysledky_db:
        sl.append(qq[0])
        sl.append(qq[3])
        sl.append(qq[4])
        self.slovnik.vysledky_pro_ulozeni_do_db.append(sl)
        sl = []
    print(self.slovnik.vysledky_pro_ulozeni_do_db)
    db.uloz_test_studenta(self.slovnik.vysledky_pro_ulozeni_do_db)
    self.slovnik.vysledky_pro_ulozeni_do_db = []

def vyhodnoceni_v1(self):
    try:
        self.slovnik.pocet_sl_pro_procenta +=1
        spravne = self.slovicko[3]
        spatne = self.slovicko[4]
        vys = []
        vys_do_vypisu = []
        if self.slovicko[2].lower() == self.preklad.get().lower():
            self.ok = True       
            spravne +=1
            self.slovnik.pocet_spravnych_pro_procenta+=1
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
            self.slovnik.aktualni_slovo+=1
            if self.slovnik.aktualni_slovo == len(self.slovnik.testuj):
                self.ceskytext.set("")
                uloz_do_db(self)
                return
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
            self.slovnik.aktualni_slovo+=1
            if self.slovnik.aktualni_slovo == len(self.slovnik.testuj):
                self.ceskytext.set("")
                uloz_do_db(self)
                return
            spust_test(self)
    except TypeError:
        self.slovnik.pocet_sl_pro_procenta +=1
        spravne = self.slovicko[3]
        spatne = self.slovicko[4]
        vys = []
        vys_do_vypisu = []
        if self.slovicko[2].lower() == self.preklad.get().lower():
            self.ok = True       
            spravne +=1
            self.slovnik.pocet_spravnych_pro_procenta+=1
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
            self.slovnik.aktualni_slovo+=1
            if self.slovnik.aktualni_slovo == len(self.slovnik.testuj):
                self.ceskytext.set("")
                uloz_do_db(self)
                return
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
            self.slovnik.aktualni_slovo+=1
            if self.slovnik.aktualni_slovo == len(self.slovnik.testuj):
                self.ceskytext.set("")
                uloz_do_db(self)
                return
            
            spust_test(self)


def vyhodnoceni_v2(self):
    print("Dodělat")

def vyhodnoceni_v3(self):
    print("Dodělat")




