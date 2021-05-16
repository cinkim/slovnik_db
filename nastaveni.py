import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES
import tkinter.messagebox
from typing_extensions import IntVar
import prace_s_db

def nastaveni_studenta(self):
    # načte z db nastavení daného studenta
    self.nacti_nastaveni_studenta()
    
    self.top_student = tk.Tk()
    self.top_student.title("Nastavení studenta")  
    
    self.nastaveni = tk.LabelFrame(self.top_student, text="Nastavení studenta: "  + self.akt_student, font="Arial 14")
    self.nastaveni.grid(row=0, column=0, rowspan=5, sticky=N)
    
    self.mezera0 = tk.Label(self.nastaveni, text="")
    self.mezera0.grid(row=1, column=0, columnspan=3, sticky=W)
   
    self.pocet_slovicek_popis = tk.Label(self.nastaveni, text="Počet slovíček v jednom testu:")
    self.pocet_slovicek_popis.grid(row=2, column=0, columnspan=2,sticky=W)
    self.pocet_slovicek_Entry = tk.Entry(self.nastaveni, width=10, justify="center")
    self.pocet_slovicek_Entry.grid(row=2, column=2, sticky=W)
    self.pocet_slovicek_Entry.insert(0,self.pocet_k_testu)

    self.pocet_opakovani_popis = tk.Label(self.nastaveni, text="Počet opakování stejného testu: ")
    self.pocet_opakovani_popis.grid(row=3, column=0, columnspan=2,sticky=W)
    self.pocet_opakovani_Entry = tk.Entry(self.nastaveni, width=10, justify="center")
    self.pocet_opakovani_Entry.grid(row=3, column=2, sticky=W)
    self.pocet_opakovani_Entry.insert(0,self.pocet_kol_testu)

    self.pocet_spravne_popis = tk.Label(self.nastaveni, text="Počet správných odpovědí pro vyřazení slovíčka z testu: ")
    self.pocet_spravne_popis.grid(row=4, column=0, columnspan=3, sticky=W)
    self.pocet_spravne_Entry = tk.Entry(self.nastaveni, width=10, justify="center")
    self.pocet_spravne_Entry.grid(row=4, column=3, sticky=W)
    self.pocet_spravne_Entry.insert(0,self.pocet_spravnych)

    self.mezera = tk.Label(self.nastaveni, text="")
    self.mezera.grid(row=5, column=0, columnspan=3, sticky=W)


    """________________________ výběr typu překladu ___________________"""
    
    self.nastaveni_preklad = tk.LabelFrame(self.nastaveni, text="Typ překladu: ", font="Arial 8")
    self.nastaveni_preklad.grid(row=6, column=0, rowspan=5, sticky=N)
    
    pozice = 1 # pozice řádky v rámci skupiny RadioButtonu
    typy = [("cz -> cizí jazyk","1"),
            ("cizí jazyk -> cz","2"),
            ("míchat: cz <-> cizí jazyk","3")
            ]
    
    var_preklad = StringVar()
    
    
    for text, hodnota in typy:      # indicatoron=0, 
        preklad_Radio = tk.Radiobutton(self.nastaveni_preklad, text=text, variable=var_preklad, value=hodnota, 
            command = lambda: print(var_preklad.get()))

        
        if hodnota == str(self.typ_prekladu):
            preklad_Radio.select()
        
        preklad_Radio.grid(row=pozice, sticky=W) 
        pozice = pozice + 1
     

    
    
    """________________________ výběr testu se slovíčky s více špatnými odpověďmi___________________"""
    
    self.nastaveni_test_spatna = tk.LabelFrame(self.nastaveni, text="Test pouze ze slovíček\n s více jak 3 špatnými odpověďmi: ", font="Arial 8")
    self.nastaveni_test_spatna.grid(row=6, column=2, columnspan=2,rowspan=5, sticky=W)
    
    pozice = 1 # pozice řádky v rámci skupiny RadioButtonu
    a_n = [("Ano","1"),
            ("Ne","2"),
            ]
    var_spatne = StringVar()
    for text, hodnota in a_n:      # indicatoron=0, 
        self.test_spatna_Radio = tk.Radiobutton(self.nastaveni_test_spatna, text=text, variable=var_spatne, value=hodnota,
                 command=lambda: print("NEVRACÍ MI TO: ", var_spatne.get())) 
        
        if hodnota == str(self.testovat_jen_spatne): # označí jako nastavenou hodnotu z db
            self.test_spatna_Radio.select()
        
        self.test_spatna_Radio.grid(row=pozice, sticky=W) 
        pozice = pozice + 1
    


    
    self.ulozit_nastaveni = tk.Button(self.top_student, text="Uložit nastavení", command=self.uloz_nastaveni_stud, fg="blue", font="Arial 8", width=20)
    self.ulozit_nastaveni.grid(row=0, column=5, sticky=W)

    self.ulozit_Konec = tk.Button(self.top_student, text="Konec", command=self.top_student.destroy, fg="red", font="Arial 8", width=20)
    self.ulozit_Konec.grid(row=1, column=5, sticky=W+E)





def uloz_nastaveni_studenta(self):
    print([
    self.akt_student, 
    self.pocet_slovicek_Entry.get(),
    self.pocet_spravne_Entry.get(),
    self.pocet_opakovani_Entry.get(),
    3,#self.var_preklad.get(),  # zatím natvrdo, nelze měnit, nejde mi načíst proměnná var_preklad.get()
    2    # zatím natvrdo, nelze měnit, nejde mi načíst proměnná var_spatne.get()
    ])

    
    prace_s_db.uloz_nastaveni_studenta([
    self.akt_student, 
    self.pocet_slovicek_Entry.get(),
    self.pocet_spravne_Entry.get(),
    self.pocet_opakovani_Entry.get(),
    3,#self.var_preklad.get(),  # zatím natvrdo, nelze měnit, nejde mi načíst proměnná var_preklad.get()
    2    # zatím natvrdo, nelze měnit, nejde mi načíst proměnná var_spatne.get()
    ])
    
 