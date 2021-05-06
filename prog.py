# hlani program

import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES, VERTICAL, ACTIVE
import tkinter.messagebox

import new_student as ns
import prace_s_db
import nastaveni
import testovani
import pridat_sl as sl
import vypsat_sl as v_sl
import pridat_uc as uc
import pridat_lek as lek
import import_slovicek as im


class slovnik:

    def __init__(self):
        self.seznam_studentu = []
        self.nacti_studenty()
        self.jazyky_studenta = []
        self.akt_jazyk = ""
        self.seznam_ucebnic = []
        self.nova_sl = []
        
    """_____________ načtení všech studentů po startu aplikace ______________"""
    def nacti_studenty(self):
        try:
            prace_s_db.overeni_sl()
        except:
            self.seznam_studentu = []
        else:
            self.seznam_studentu = prace_s_db.seznam_studentu()

class slovnikGUI(tk.Frame):

    def __init__(self, parent, slovnik):
        super().__init__(parent)
        self.parent = parent
        self.slovnik = slovnik
        self.parent.title("Slovnik")
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets_uzivatele()
        self.zobraz()
        self.akt_ucebnice = ""
        

    """__________________ vytvoří pole se seznamem studentů _________________________________________"""
    def create_widgets_uzivatele(self):
        self.uzivatel = tk.Label(root, text="", font="Arial 16", fg="red")
        self.uzivatel.grid(row=0, columnspan=4, sticky=W+E)

        self.kdo = tk.LabelFrame(root, text="Kdo jsi", font="Arial 8")
        self.kdo.grid(row=1, column=0, sticky=W)

        self.tree_zaznamy = ttk.Treeview(self.kdo, column=("student"), height=8, selectmode='browse')
        self.tree_zaznamy['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_zaznamy.grid(row=2, column=0)
        
        self.tree_zaznamy.heading("#0", text="#\n ")
        self.tree_zaznamy.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_zaznamy.heading("student", text="Student\n ")
        self.tree_zaznamy.column("student", minwidth=0, width=124, stretch=NO, anchor='center')

        self.button_NacistStudenta = tk.Button(root, text="Načti studenta", command=self.nacti_studenta, fg="blue", font="Arial 8", width=20)
        self.button_NacistStudenta.grid(row=8, column=0, sticky=W)

        self.button_new_st = tk.Button(root, text="Nový student", command=self.vytvor_top_okno_novy_student, fg="blue", font="Arial 8", width=20)
        self.button_new_st.grid(row=9, column=0, sticky=W)

        self.button_Konec = tk.Button(root, text="Konec", command=self.on_close, fg="red", font="Arial 8", width=20)
        self.button_Konec.grid(row=10, column=0, sticky=W)

    """________________________ vytvoří pole jazyků, podle zvoleného studenta ___________________"""
    def create_widgets_jazyk(self):      
        pozice = 1 # pozice řádky v rámci skupiny RadioButtonu
        self.akt_jazyk = StringVar()

        try:
            self.jazyky.destroy()
            self.ucebnice.destroy()
            self.Lekce.destroy()
        except AttributeError:
            pass

        self.jazyky = tk.LabelFrame(root, text="Testovat jazyk", font="Arial 8")
        self.jazyky.grid(row=1, column=1, sticky=N)

        for jazyk in self.jazyky_studenta:
            self.j_studenta = tk.Radiobutton(self.jazyky, indicatoron=0, text=jazyk, variable=self.akt_jazyk, command=self.nacti_ucebnice, value=jazyk, width = 20)
            self.j_studenta.grid(row=pozice, column=0, sticky=W)
            if jazyk == self.akt_jazyk:
                self.j_studenta.select()
                
            else:
                self.j_studenta.deselect()
            pozice = pozice + 1

    """___________________________ vytvoří pole se seznamem učebnic podle zvoleného studenta a jazyka ________________________"""
    def create_widgets_ucebnice(self):       
        try:
            self.ucebnice.destroy()
            self.Lekce.destroy()
        except AttributeError:
            pass
        self.ucebnice = tk.LabelFrame(root, text="Učebnice", font="Arial 8")
        self.ucebnice.grid(row=1, column=2, rowspan=11, sticky=N)
        self.scrollbar_ucebnice = tk.Scrollbar(self.ucebnice, orient=VERTICAL)
        self.ucebnice_ListBox = tk.Listbox(self.ucebnice, width=21, yscrollcommand=self.scrollbar_ucebnice.set, height=15, font="Arial 8")
        self.ucebnice_ListBox.bind( "<ButtonRelease-1>", self.nacti_lekce)  # po kliknutí se načtou slovíčka z dané učebnice
        
        self.ucebnice_ListBox.grid(row=2, column=2, sticky=W)

        self.button_pridat_ucebnici = tk.Button(self.ucebnice, text="Přidat učebnici", command=self.pridat_ucebnici, fg="blue", font="Arial 8", width=20)
        self.button_pridat_ucebnici.grid(row=8, column=2, sticky=W)
        """
        self.button_smazat_ucebnici = tk.Button(self.ucebnice, text="Smazat učebnici", command=self.smazat_ucebnici, fg="blue", font="Arial 8", width=20)
        self.button_smazat_ucebnici.grid(row=9, column=2, sticky=W)
        """


    """____________________vytvoří pole se seznamem lekcí podle zvoleného studenta/jazyka/učebnice ____________________"""
    def create_widgets_Lekce(self):
        try:
            self.Lekce.destroy()
        except AttributeError:
            pass
        self.Lekce = tk.LabelFrame(root, text="Lekce", font="Arial 8")
        self.Lekce.grid(row=1, column=3, rowspan=11, sticky=N)

        self.tree_Lekce = ttk.Treeview(self.Lekce, column=("c_lekce", "nazev"), height=10, selectmode='browse')
        self.tree_Lekce['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_Lekce.grid(row=2, column=0,  columnspan=2)
        
        self.tree_Lekce.heading("#0", text="#\n ")
        self.tree_Lekce.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_Lekce.heading("c_lekce", text="lekce\n ")
        self.tree_Lekce.column("c_lekce", minwidth=0, width=50, stretch=NO, anchor='center')

        self.tree_Lekce.heading("nazev", text="Název lekce\n ")
        self.tree_Lekce.column("nazev", minwidth=0, width=200, stretch=NO, anchor='center')

        self.button_pridat_lekci = tk.Button(self.Lekce, text="Přidat lekci", command=self.pridat_lekci, fg="blue", font="Arial 8", width=20)
        self.button_pridat_lekci.grid(row=4, column=0, sticky=W)
        """
        self.button_smazat_lekci = tk.Button(self.Lekce, text="Smazat lekci", command=self.smazat_lekci, fg="blue", font="Arial 8", width=20)
        self.button_smazat_lekci.grid(row=5, column=0, sticky=W)
        """
        self.button_pridat_slovicka = tk.Button(self.Lekce, text="Přidat slovíčka", command=self.pridat_slovicka, fg="blue", font="Arial 8", width=20)
        self.button_pridat_slovicka.grid(row=4, column=1, sticky=W)

        self.button_pridat_slovicka = tk.Button(self.Lekce, text="Vypsat slovíčka", command=self.vypsat_slovicka, fg="blue", font="Arial 8", width=20)
        self.button_pridat_slovicka.grid(row=5, column=0, sticky=W)
              
    """_________________ vytvoří pravé pole pro další volby - nastavení/testování/historie ____________________________"""
    def create_ovl_sekce(self):
        self.pole_nastaveni = tk.LabelFrame(root, text="Nastavení", font="Arial 8")
        self.pole_nastaveni.grid(row=1, column=4, sticky=N)
        self.nastav = tk.Label(self.pole_nastaveni, text="", font="Arial 8")

        self.button_Nastaveni = tk.Button(self.pole_nastaveni, text="Nastavení studenta", command=self.nastaveni_stud, fg="blue", font="Arial 8", width=20)
        self.button_Nastaveni.grid(row=2, column=2, sticky=W)

        self.mezera1 = tk.Label(self.pole_nastaveni, text="")
        self.mezera1.grid(row=3, column=2, sticky=W)

    """_______________________ nastaveni.py ___________________________________________________________________"""
    # vše k pravému nastavení + testování
    def nastaveni_stud(self):
        nastaveni.nastav_studenta(self)
        return
    

    """_______________________ pridat_uc.py _________________________________________________________________________"""
    # vše k učebnici
    def pridat_ucebnici(self):
        uc.nova_ucebnice(self) # otevře nové okno
         
    def ulozit_ucebnice(self):
        uc.ulozit_novou_ucebnici(self) # uloží novou učebnici
            
    def smazat_ucebnici(self):
        uc.smazat_uc(self) # smaže učebnici

    """____________________________ pridat_lek.py ___________________________________________________________________"""

    # vše k lekci
    def pridat_lekci(self): 
        lek.nova_lekce(self) # otevře nové okno

    
    def ulozit_lekci(self): # uloží novou lekci
        lek.ulozit_Lek(self)

    def smazat_lekci(self):
        lek.smazat_Lek(self) # smaže lekci

    """____________________________ pridat_sl.py _______________________________________________________________"""

    # vše k novému oknu přidat slovíčka(otevření, zavření, ukládání)
    def pridat_slovicka(self):
        """
        Otevře okno pro přidání učebnice, lekce, slovíček
        """
        sl.nacti_lekci(self)

    def dalsi_slovo(self, event):
        """
        Postupné ukládání slovíček
        """
        sl.dalsi(self)
        sl.vypsat_manualni_slovicka(self)


    def ulozit(self):
        """
        Uložení nových slovíček
        """
        sl.ulozit(self)

    def nacist(self):
        im.import_sl(self)

    def edit(self):
        sl.opravit(self)

    """____________________________ vypsat_sl.py _______________________________________________________________"""

    # vše k novému oknu vypsat slovíčka(otevření, zavření, ukládání)
    def vypsat_slovicka(self):
        """
        Vypíše seznam slovíček vybrané lekce
        """
        try:
            self.akt_Lekce = str(self.tree_Lekce.item(self.tree_Lekce.focus())["values"][1])
            v_sl.vypis_slovicka(self,prace_s_db.slovicka_lekce(self.akt_Lekce))
        except:
            tk.messagebox.showwarning("ERROR", "Vyber lekci.")


    """_____________________________ new_student.py ______________________________________________________________"""

    # vše k oknu nový student

    def vytvor_top_okno_novy_student(self):
        """
        Otevře okno pro registraci studenta
        """
        ns.vytvor_top_okno_novy_student(self)


    def novy(self):
        ns.ulozit_noveho_studenta(self)
        self.slovnik.nacti_studenty()
        self.zobraz()
        return


    """___________________________ načtení studenta ____________________________________________________________"""
    # načtení studenta
    def nacti_studenta(self):
        """
        Nacte jazyky studenta
        """
        try:
            self.words.destroy()
            self.ucebnice.destroy()
        except AttributeError:
            pass
        if self.slovnik.seznam_studentu == []:
            tk.messagebox.showwarning("ERROR", "Nejdříve se zaregistruj.")
            return
        # urci vybranou pozici polozky a z toho pak hodnotu dane polozky
        try:
            self.akt_student = self.tree_zaznamy.item(self.tree_zaznamy.focus())["values"][0]
            self.jazyky_studenta = prace_s_db.jazyky_studenta(self.akt_student)
            self.create_widgets_jazyk()
            self.create_ovl_sekce()
            self.uzivatel["text"] = "Aktuální uživatel je "+ str(self.akt_student)
            return
        except IndexError:
            tk.messagebox.showwarning("ERROR", "Nejdříve vyber studenta.")
            return


    """____________________ načtení učebnice _________________________________________________________"""
    # načte učebnice podle zvoleného jazyka
    def nacti_ucebnice(self):
        # print(self.akt_jazyk.get(), end=": ")
        self.akt_j = self.akt_jazyk.get()
        self.seznam_ucebnic = prace_s_db.seznam_ucebnic(self.akt_jazyk.get())
        #print(self.seznam_ucebnic)
        self.create_widgets_ucebnice()
        for ucebnice in self.seznam_ucebnic:
            #print(ucebnice)
            self.ucebnice_ListBox.insert(tkinter.END, ucebnice)
        return
       
    """___________________________ načtení lekce ______________________________________"""
    # načte lekce podle vybrané učebnice
    def nacti_lekce(self, event=""):
        try:
            if event !="":  # funkci spouštím z akce ListBoxu - <on click>     
                self.akt_ucebnice = self.seznam_ucebnic[self.ucebnice_ListBox.curselection()[0]]
        except IndexError:
            tk.messagebox.showwarning("ERROR", "Vyber, nebo založ novou učebnici.")
            self.akt_ucebnice = ""
            return
        self.create_widgets_Lekce()
        # print("Učebnice: ", self.akt_ucebnice, end=": ")
        self.seznam_lekci = prace_s_db.seznam_lekci(self.akt_ucebnice)
        for ii in self.tree_Lekce.get_children():
            self.tree_Lekce.delete(ii)

        pozice = 0
        for cislo in self.seznam_lekci:
            self.tree_Lekce.insert("", "end", text=pozice, values=cislo)
            pozice += 1

    """_______________________ zobrazí registrované studenty __________________________"""
    # zobrazí registrované studenty
    def zobraz(self):
        for ii in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(ii)

        pozice = 0
        for zaznam in self.slovnik.seznam_studentu:
            self.tree_zaznamy.insert("", "end", text=pozice, values=zaznam)
            pozice += 1

    """_______________________ ukončení celé aplikace _____________________________"""
    # zavře celou aplikaci včetně všech oken
    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    slovnik = slovnik()
    app = slovnikGUI(root, slovnik)
    app.mainloop()
