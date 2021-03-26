# hlani program

import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL, YES
import tkinter.messagebox

import new_student as ns
import prace_s_db


class slovnik:

    def __init__(self):
        self.seznam_studentu = []
        self.nacti_studenty()


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
        self.create_widgets()
        self.zobraz()


    def create_widgets(self):
        self.kdo = tk.LabelFrame(root, text="Kdo jsi", font="Arial 8")
        self.kdo.grid(row=1, column=0, sticky=W)

        self.tree_zaznamy = ttk.Treeview(self.kdo, column=("student"), height=8)
        self.tree_zaznamy['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_zaznamy.grid(row=2, column=0)

        
        self.tree_zaznamy.heading("#0", text="#")
        self.tree_zaznamy.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_zaznamy.heading("student", text="Student")
        self.tree_zaznamy.column("student", minwidth=0, width=124, stretch=NO, anchor='center')

        self.button_Konec = tk.Button(root, text="Nový student", command=self.novy_student, fg="blue", font="Arial 8", width=20)
        self.button_Konec.grid(row=9, column=0, sticky=W)

        self.button_Konec = tk.Button(root, text="Konec", command=self.on_close, fg="red", font="Arial 8", width=20)
        self.button_Konec.grid(row=10, column=0, sticky=W)
        

    def novy(self):
        self.novy = ns.ulozit_noveho_studenta(self)
        if self.novy == None:
            return
        prace_s_db.pridat_studenta(self.novy)
        self.slovnik.nacti_studenty()
        self.zobraz()
        return


    def novy_student(self):
        """
        Otevře okno pro registraci studenta
        """
        ns.zaloz_studenta(self)


    def zobraz(self):
        for ii in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(ii)

        pozice = 0
        for zaznam in self.slovnik.seznam_studentu:
            self.tree_zaznamy.insert("", "end", text=pozice, values=zaznam)
            pozice += 1

    # zavřít
    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    slovnik = slovnik()
    app = slovnikGUI(root, slovnik)
    app.mainloop()

