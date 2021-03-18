# hlani program

import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox

import new_student as ns


class slovnik:

    def __init__(self):
        self.seznam_studentu = self.nacti_studenty()


    def nacti_studenty(self):
        studenti = []
        with open("studenti.txt", mode="r", encoding="utf-8") as seznam_st:
            for student in seznam_st:
                student = student.strip()
                studenti.append(student)
            return studenti



class slovnikGUI(tk.Frame):

    def __init__(self, parent, slovnik):
        super().__init__(parent)
        self.parent = parent
        self.slovnik = slovnik
        self.parent.title("Slovnik")
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()


    def create_widgets(self):
        self.kdo = tk.LabelFrame(root, text="Kdo jsi", font="Arial 8")
        self.kdo.grid(row=1, column=0, sticky=W)
        if len(self.slovnik.seznam_studentu) == 0:
            pass
        else:
            self.aktualni_osoba = StringVar()
            self.aktualni_osoba.set(self.slovnik.seznam_studentu[0])

            for self.uziv in self.slovnik.seznam_studentu:
                self.RB = tk.Radiobutton(self.kdo, text=self.uziv, variable=self.aktualni_osoba, value=self.uziv, width=20, anchor=W, command=self.nacti_ucivo)
                self.RB.grid()

        self.button_Konec = tk.Button(root, text="Nový student", command=self.novy_student, fg="blue", font="Arial 8", width=20)
        self.button_Konec.grid(row=9, column=0, sticky=W)

        self.button_Konec = tk.Button(root, text="Konec", command=self.on_close, fg="red", font="Arial 8", width=20)
        self.button_Konec.grid(row=10, column=0, sticky=W)
        




    def novy_student(self):
        ns.zaloz_studenta(self)

    def novy(self):
        ns.ulozit_noveho_studenta(self)
        self.slovnik.__init__()
        self.__init__(parent, slovnik)
        root.update()



    def nacti_ucivo(self):
        a=self.aktualni_osoba.get()
        print(a)


    # zavřít
    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    slovnik = slovnik()
    app = slovnikGUI(root, slovnik)
    app.mainloop()

