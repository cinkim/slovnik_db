# hlavni program

import tkinter as tk
from tkinter import ttk, StringVar,  N, E, W
from tkinter import NO, VERTICAL
import tkinter.messagebox
from tkinter import messagebox

import os

import win32com.client as win32

import webbrowser

import new_student as ns
import prace_s_db
import nastaveni
import testovani as ts
import vysledky as vys
import pridat_sl as sl
import vypsat_sl as v_sl
import pridat_uc as uc
import pridat_lek as lek
import import_slovicek as im

class slovnik:

    def __init__(self):
        self.seznam_studentu = [] # vrácený seznam studentů z db
        self.nacti_studenty() # načte z db seznam studentů
        self.jazyky_studenta = [] # seznam jazyků aktuálního studenta
        self.akt_jazyk = "" # aktuální jazyk k testování zvoleného studenta
        self.seznam_ucebnic = [] # seznam učebnic studenta/jazyku
        self.nova_sl = [] # nová slovíčka k uložení do db

        self.k_testovani = [] # načtená všechna slovíčka z db zvolené lekce
        self.testuj = [] # vybraná slova k testování 
        self.netestuj = []# vyřazená slova z testování
        self.aktualni_slovo = 0 # aktuálně testované slovo

        self.vysledky_pro_ulozeni_do_db = [] # konečný řetězec pro uložení výsledku do db

        self.pocet_k_testu = None # počet slovíček v rámci jednoho testu
        self.pocet_spravnych = None # počet správných odpovědí pro vyřazení slovíčka
        self.pocet_kol_testu = None # počet kol testování se stejnými slovíčky
        self.typ_prekladu = None # "směr" překladu: 1=cz/cizí, 2=cizí/cz, 3=míchat
        self.testovat_jen_spatne = None  # Testovat jen ze slovíček se špatnou odpovědí>3,   1=ano, 2=ne
        self.rychlost_cteni = 0 # Nastavení rychlosti pro čení Aj slovíček, 0=pomalu/1=rychle
        
        
        self.vysledky_db = [] # vysledky spravnych sloviček pro uložení do db
        self.vysledky = [] # průběžné výsledky do výpisu na obrazovku
        
        self.pocet_sl_pro_procenta = 0 # mezivýpočet pro procentuelní vyhodnocení testu
        self.pocet_spravnych_pro_procenta = 0 # mezivýpočet pro procentuelní vyhodnocení testu
        self.zbyva_k_testovani = 0
        self.aj = ""
        self.de = ""
        self.fr = ""
        self.it = ""
        self.es = ""
        self.ru = "" 
        self.nacti_vyslovnost() # načte předvolenou výslovnost 



    """_____________ načtení všech studentů po startu aplikace ______________"""
    def nacti_studenty(self):
        try:
            prace_s_db.overeni_sl()
        except:
            self.seznam_studentu = []
        else:
            self.seznam_studentu = prace_s_db.seznam_studentu()
            for filename in os.listdir('.'):
                if filename.endswith('.mp3'):
                    os.remove(filename)

    def nacti_vyslovnost(self):
        try:
            with open("vyslovnost.txt", mode="r", encoding="UTF-8") as vyslov:
                for radka in vyslov:
                    radka = radka.strip()
                    radka = radka.split(";")
                    if radka[0] == "aj":
                        self.aj = radka[1]
                    elif radka[0] == "de":
                        self.de = radka[1]
                    elif radka[0] == "fr":
                        self.fr = radka[1]
                    elif radka[0] == "it":
                        self.it = radka[1]
                    elif radka[0] == "es":
                        self.es = radka[1]
                    elif radka[0] == "ru":
                        self.ru = radka[1]
            return
        except FileNotFoundError:
            tk.messagebox.showwarning("ERROR", "Soubor s přednastavenou výslovností nenalezen.")



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

        self.studenti = tk.LabelFrame(root, text="Studenti", font="Arial 8")
        self.studenti.grid(row=1, column=0, sticky=N)

        self.scrollbar_studenti = tk.Scrollbar(self.studenti, orient=VERTICAL)
        self.studenti_ListBox = tk.Listbox(self.studenti, width=21, yscrollcommand=self.scrollbar_studenti.set, height=15, font="Arial 8")
        self.studenti_ListBox.bind( "<ButtonRelease-1>", self.nacti_studenta)  # po kliknutí se načtou slovíčka z dané učebnice 
        self.studenti_ListBox.grid(row=2, column=0, sticky=W)

        self.button_new_st = tk.Button(root, text="Nový student", command=self.vytvor_top_okno_novy_student, font="Arial 8", width=20)
        self.button_new_st.grid(row=10, column=0, sticky=W)

        self.button_Konec = tk.Button(root, text="Konec", command=self.on_close, fg="red", font="Arial 8", width=20)
        self.button_Konec.grid(row=11, column=0, sticky=W)

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

        self.button_pridat_ucebnici = tk.Button(self.ucebnice, text="Přidat učebnici", command=self.pridat_ucebnici, font="Arial 8", width=20)
        self.button_pridat_ucebnici.grid(row=8, column=2, sticky=W)



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

        self.button_pridat_lekci = tk.Button(self.Lekce, text="Přidat lekci", command=self.pridat_lekci, font="Arial 8", width=20)
        self.button_pridat_lekci.grid(row=4, column=0, sticky=W)

        self.button_pridat_slovicka = tk.Button(self.Lekce, text="Přidat slovíčka", command=self.pridat_slovicka, font="Arial 8", width=20)
        self.button_pridat_slovicka.grid(row=4, column=1, sticky=W)

        self.button_pridat_slovicka = tk.Button(self.Lekce, text="Vypsat slovíčka", command=self.vypsat_slovicka, font="Arial 8", width=20)
        self.button_pridat_slovicka.grid(row=5, column=0, sticky=W)

        self.button_Test = tk.Button(self.Lekce, text="Testovat", command=self.Test, font="Arial 8", width=20)
        self.button_Test.grid(row=5, column=1, sticky=W)
              
    """_________________ vytvoří pravé pole pro další volby - nastavení/testování/historie ____________________________"""
    def create_ovl_sekce(self):
        self.pole_nastaveni = tk.LabelFrame(root, text="Nastavení", font="Arial 8")
        self.pole_nastaveni.grid(row=1, column=4, sticky=N)
        self.nastav = tk.Label(self.pole_nastaveni, text="", font="Arial 8")

        self.button_Nastaveni = tk.Button(self.pole_nastaveni, text="Nastavení studenta", command=self.nastaveni_stud, font="Arial 8", width=20)
        self.button_Nastaveni.grid(row=2, column=2, sticky=W)

        self.mezera1 = tk.Label(self.pole_nastaveni, text="")
        self.mezera1.grid(row=3, column=2, sticky=W)

        self.button_Nastaveni = tk.Button(self.pole_nastaveni, text="Výsledky studenta", command=self.vysledky_stud, font="Arial 8", width=20)
        self.button_Nastaveni.grid(row=4, column=2, sticky=W)

        self.mezera1 = tk.Label(self.pole_nastaveni, text="")
        self.mezera1.grid(row=5, column=2, sticky=W)

        self.email = tk.Button(self.pole_nastaveni, text="Poslat email vývojářům?", command=self.email_vyvojarum, font="Arial 8", width=20)
        self.email.grid(row=6, column=2, sticky=W)

        self.mezera2 = tk.Label(self.pole_nastaveni, text="")
        self.mezera2.grid(row=7, column=2, sticky=W)

        self.novinky = tk.Button(self.pole_nastaveni, text="Zkontrolovat novinky", command=self.kontrola_novinek, font="Arial 8", width=20)
        self.novinky.grid(row=8, column=2, sticky=W)

        self.mezera3 = tk.Label(self.pole_nastaveni, text="")
        self.mezera3.grid(row=9, column=2, sticky=W)

        self.button_tov_nastaveni = tk.Button(self.pole_nastaveni, text="Obnovit\ntovární nastavení", command=self.tovarni_nastaveni, fg="red", font="Arial 8", width=20)
        self.button_tov_nastaveni.grid(row=10, column=2, sticky=W)

    """_______________________Novinky___________________________"""
    def kontrola_novinek(self):
        webbrowser.open('www.pyladiesplzen.wz.cz', new = 2)
    """__________________________email vývojářům________________"""
    def email_vyvojarum(self):
        try:
            outlook = win32.Dispatch("outlook.application")
            mail = outlook.CreateItem(0)
            mail.subject = "Slovník - nahlásit problém/požadavek" # předmět
            mail.To = "lucie.jimenez@gmail.com; lenka@konstant.cz; cinkim@seznam.cz"
            mail.Display(False)
            return
        except:
            tk.messagebox.showwarning("Error", "Je nutné mít nainstalovanou aplikaci MS Outlook\npokud aplikaci nechcete instalovat, použijte jeden z následujících kontaktů\n\nlucie.jimenez@gmail.com\nlenka@konstant.cz\ncinkim@seznam.cz")
            print("ok")


    """_______________________ Tovární nastavení______________________________"""
    def tovarni_nastaveni(self):
        if messagebox.askyesno("POZOR", "Program se uvede do prvotního spuštění\nBudou smazána tato data!!!\n-registrovaní studenti\n-přidané učebnice\n-přidané lekce\n-přidaná slovíčka\n-výsledky testů") == True:
            os.remove("db_slovnik.sqlite")
            tk.messagebox.showwarning("???", "Nastaveno prvotní zobrazení\nSPUSŤE PROGRAM ZNOVU")
            self.parent.destroy()

        else:
            pass



    """_______________________ nastaveni.py ___________________________________________________________________"""
    # vše k pravému nastavení + testování
    def nastaveni_stud(self):
        nastaveni.nastaveni_studenta(self)
        return

    def uloz_nastaveni_stud(self):
        nastaveni.uloz_nastaveni_studenta(self)
        return

    def pridej_jazyk(self, student, jazyk):
        nastaveni.pridat_jazyk(self, student, jazyk)
        return
    
    """_______________________ vysledky.py ___________________________________________________________________"""
    def vysledky_stud(self):
        # vypíše výsledky studenta v rámci jedné učebnice
        
        try:
            # self.akt_ucebnice = self.seznam_ucebnic[self.ucebnice_ListBox.curselection()[0]]
            data = prace_s_db.nacti_vysledky(self.akt_student, self.akt_ucebnice)
            vys.vypis_vysledky(self, data)
        except AttributeError:
            tk.messagebox.showwarning("ERROR", "Vyber jazyk a učebnici.")
        except IndexError:
            tk.messagebox.showwarning("ERROR", "Vyber učebnici.")
        except TypeError:
            tk.messagebox.showwarning("ERROR", "Vyber učebnici.")
        return
    

    """_______________________Testování______________________________________"""
    # vše k oknu testování
    
    def Test(self): # otevře okno pro testování
        try:
            ts.tes(self)
        except IndexError:
            tk.messagebox.showwarning("ERROR", "Nejdříve vyber lekci.")
        return

   
    def Testuj(self): # spustí se po kliknutí na tlačítko Testuj
        self.nacti_nastaveni_studenta()
        if self.slovnik.aktualni_slovo == 0:
            self.slovnik.vysledky = []
            self.slovnik.aktualni_slovo = 0
            ts.nacti(self)
            ts.spust_test(self)
        elif self.slovnik.aktualni_slovo == len(self.slovnik.testuj):
            if tk.messagebox.askyesno("???", "Testovat znuvu?") == True:
                self.slovnik.k_testovani = []
                self.slovnik.testuj = []
                self.slovnik.netestuj = []
                self.slovnik.aktualni_slovo = 0
                self.slovnik.vysledky_pro_ulozeni_do_db = []
                self.slovnik.vysledky_db = []
                self.slovnik.vysledky = []
                self.slovnik.pocet_sl_pro_procenta = 0
                self.slovnik.pocet_spravnych_pro_procenta = 0
                ts.nacti(self)
                ts.spust_test(self)
            else:
                self.slovnik.k_testovani = []
                self.slovnik.testuj = []
                self.slovnik.netestuj = []
                self.slovnik.aktualni_slovo = 0
                self.slovnik.vysledky_pro_ulozeni_do_db = []
                self.slovnik.vysledky_db = []
                self.slovnik.vysledky = []
                self.slovnik.pocet_sl_pro_procenta = 0
                self.slovnik.pocet_spravnych_pro_procenta = 0
                self.top_test.destroy()
        else:
            pass
            


    def vyhodnot(self, event):    
        if self.slovnik.aktualni_slovo == len(self.slovnik.testuj):
            return
        else:
            ts.vyhodnoceni(self)


    def ukonci_top_test(self):
        self.slovnik.k_testovani = []
        self.slovnik.testuj = []
        self.slovnik.netestuj = []
        self.slovnik.aktualni_slovo = 0
        self.slovnik.vysledky_pro_ulozeni_do_db = []
        self.slovnik.vysledky_db = []
        self.slovnik.vysledky = []
        self.slovnik.pocet_sl_pro_procenta = 0
        self.slovnik.pocet_spravnych_pro_procenta = 0
        self.top_test.destroy()

    """_______________________ pridat_uc.py _________________________________________________________________________"""
    # vše k učebnici
    def pridat_ucebnici(self):
        uc.nova_ucebnice(self) # otevře nové okno
         
    def ulozit_ucebnice(self):
        uc.ulozit_novou_ucebnici(self) # uloží novou učebnici
        self.Lekce.destroy()
            

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
            v_sl.vypis_slovicka(self,prace_s_db.slovicka_lekce(self.akt_Lekce, self.akt_student))
            #print(prace_s_db.nastaveni_studenta(self.akt_student))
        except IndexError:
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
        self.slovnik.seznam_studentu = []
        self.slovnik.nacti_studenty()
        self.studenti.destroy()
        self.create_widgets_uzivatele()
        self.zobraz()
        return


    """___________________________ načtení studenta ____________________________________________________________"""
    # načtení studenta
    def nacti_studenta(self, event=""):
        """
        Nacte jazyky studenta
        """
        try:
            if event !="":  # funkci spouštím z akce ListBoxu - <on click>     
                self.akt_student = self.slovnik.seznam_studentu[self.studenti_ListBox.curselection()[0]]
            self.words.destroy()
            self.ucebnice.destroy()
            # self.Lekce.destroy()
        except IndexError:
            tk.messagebox.showwarning("ERROR", "Vyber studenta.")
            return
        except AttributeError:
            pass
        self.jazyky_studenta = prace_s_db.jazyky_studenta(self.akt_student)
        self.create_widgets_jazyk()
        self.create_ovl_sekce()
        self.uzivatel["text"] = "Aktuální uživatel je "+ str(self.akt_student)
        self.nacti_nastaveni_studenta()
        return
    
    def nacti_nastaveni_studenta(self):
        
        """
        nastavi aktuální hodnoty do promennych:
        self.pocet_k_testu 
        self.pocet_spravnych
        self.pocet_kol_testu
        self.typ_prekladu
        self.testovat_jen_spatne
        self.rychlost_cteni
        """
        
        nastav_studenta = prace_s_db.nastaveni_studenta(self.akt_student)
        self.slovnik.pocet_k_testu = nastav_studenta[0]
        self.slovnik.pocet_spravnych = nastav_studenta[1]
        self.slovnik.pocet_kol_testu = nastav_studenta[2]
        self.slovnik.typ_prekladu = nastav_studenta[3]
        self.slovnik.testovat_jen_spatne = nastav_studenta[4]
        self.slovnik.rychlost_cteni = nastav_studenta[5]
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
        for student in self.slovnik.seznam_studentu:
            self.studenti_ListBox.insert(tkinter.END, student)
        return


    """_______________________ ukončení celé aplikace _____________________________"""
    # zavře celou aplikaci včetně všech oken
    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    slovnik = slovnik()
    app = slovnikGUI(root, slovnik)
    app.mainloop()
