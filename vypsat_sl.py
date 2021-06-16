import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W, NO

import os
import pyttsx3
from pyttsx3.drivers import sapi5
from pyttsx3 import voice

import platform

from gtts import gTTS
from io import BytesIO


def vypis_slovicka(self,seznam_slovicek):
        
        self.slovicka = tk.Toplevel()
        self.slovicka.title("Slovíčka lekce: " + self.akt_Lekce)

        self.nadpis = tk.Label(self.slovicka, text="Jazyk: " + self.akt_j + "\nUčebnice:" + self.akt_ucebnice + "\nLekce:" + self.akt_Lekce, font="Ariel 14", bg="grey")
        self.nadpis.grid(row=0, columnspan=3, sticky=W+E)
         
        self.tree_slovicka = ttk.Treeview(self.slovicka, column=("česky", "nečesky", "správně", "špatně"), height=20, selectmode='browse')
        self.tree_slovicka['show'] = 'headings' # schová první sloupec s identifikátorem
        self.tree_slovicka.grid(row=1, columnspan=3)
        
        self.tree_slovicka.heading("#0", text="#\n ")
        self.tree_slovicka.column("#0", width=0, stretch=NO, anchor='center')

        self.tree_slovicka.heading("česky", text="CZ\n ")
        self.tree_slovicka.column("česky", minwidth=0, width=270, stretch=NO, anchor=W)

        #self.tree_slovicka.heading("nečesky", text="nečesky\n ")
        self.tree_slovicka.heading("nečesky", text=self.akt_j.upper() + "\n")
        self.tree_slovicka.column("nečesky", minwidth=0, width=270, stretch=NO, anchor=W)

        self.tree_slovicka.heading("správně", text="SPRÁVNĚ\n ")
        self.tree_slovicka.column("správně", minwidth=0, width=65, stretch=NO, anchor='center')

        self.tree_slovicka.heading("špatně", text="ŠPATNĚ\n ")
        self.tree_slovicka.column("špatně", minwidth=0, width=65, stretch=NO, anchor='center')
                
        self.tree_slovicka.bind("<ButtonRelease-1>", lambda x:precti(self.tree_slovicka.item(self.tree_slovicka.focus())["values"][1], self.akt_jazyk.get(), self.slovnik.rychlost_cteni ) )
        self.tree_slovicka.bind("<Up>", lambda x:precti(self.tree_slovicka.item(self.tree_slovicka.focus())["values"][1], self.akt_jazyk.get(), self.slovnik.rychlost_cteni ) )
        self.tree_slovicka.bind("<Down>", lambda x:precti(self.tree_slovicka.item(self.tree_slovicka.focus())["values"][1], self.akt_jazyk.get(), self.slovnik.rychlost_cteni ) )

        self.mez = tk.Label(self.slovicka, text="", height=1)
        self.mez.grid(row=2, column=0)

        self.Konec = tk.Button(self.slovicka, width=20, text="Konec", fg="red", command=self.slovicka.destroy)
        self.Konec.grid(row=3, column=0, sticky=W)

        pozice = 0
        for zaznam in seznam_slovicek:
            
            self.tree_slovicka.insert("", "end", text=pozice, values=(zaznam[1], zaznam[2], zaznam[3], zaznam[4]))
            pozice += 1

    
def precti(slovicko, jazyk, rychlost):        
    #https://stackoverflow.com/questions/65977155/change-pyttsx3-language
    #https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3

    win = platform.platform()   # vytahne z pc verzi systému Windows
    # print(win)  # vypíše operační systém, po úpravě podmínek se řádka musí smazat

    newVoiceRate = rychlost     # nastaví rychlost čtení

    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')   # vytahne ze systému jazykové balíčky


    if "Windows-7" in win:
        if jazyk == "Aj":
            engine.setProperty("rate",newVoiceRate)
            engine.say(slovicko)
            engine.runAndWait()
        else:
            tk.messagebox.showwarning("???", """Pro tuto verzi systému není k dispozici jazykový balíček,\n
                pokud chcete využívat všechny funkce slovníku, musíte přejít na Windows-10.""")

    elif "Windows-8" in win:
        if jazyk == "Aj":
            engine.setProperty("rate",newVoiceRate)
            engine.say(slovicko)
            engine.runAndWait()
        else:
            tk.messagebox.showwarning("???", """Pro tuto verzi systému není k dispozici jazykový balíček,\n
                pokud chcete využívat všechny funkce slovníku, musíte přejít na Windows-10.""") 

    elif "Windows-10" in win:
        for voice in voices:     
            rec = voice.name # převede název jazykového balíčku na řetězec 
            # print(rec) # vypíše název jazykového balíčku, po úpravě podmínek se řádka musí smazat

            if ("United States" in rec) and (jazyk == "Aj"):  # upravit podmínku podle názvu jazykového balíčku
                tts = gTTS(slovicko, lang='en', tld="co.uk")
                tts.save(slovicko + '.mp3')
                os.startfile(slovicko + ".mp3")
                break

            elif ("German" in rec) and (jazyk == "Nj"):  # upravit podmínku podle názvu jazykového balíčku
                tts = gTTS(slovicko, lang='de')
                tts.save(slovicko + '.mp3')
                os.startfile(slovicko + ".mp3")
                break

            elif ("Russian" in rec) and (jazyk == "Ru"):    # upravit podmínku podle názvu jazykového balíčku
                tts = gTTS(slovicko, lang='ru')
                tts.save(slovicko + '.mp3')
                os.startfile(slovicko + ".mp3")
                break

            elif ("French" in rec) and (jazyk == "Fr"):  # upravit podmínku podle názvu jazykového balíčku
                tts = gTTS(slovicko, lang='fr', tld="fr")
                tts.save(slovicko + '.mp3')
                os.startfile(slovicko + ".mp3")
                break

            elif ("Spanish" in rec) and (jazyk == "Es"):    # upravit podmínku podle názvu jazykového balíčku
                tts = gTTS(slovicko, lang='es', tld="com.mx")
                tts.save(slovicko + '.mp3')
                os.startfile(slovicko + ".mp3")
                break

            elif ("Italy" in rec) and (jazyk == "It"):   # upravit podmínku podle názvu jazykového balíčku
                tts = gTTS(slovicko, lang='it')
                tts.save(slovicko + '.mp3')
                os.startfile(slovicko + ".mp3")
                break
    else:
        tk.messagebox.showwarning("???", """Pro tuto verzi systému není k dispozici jazykový balíček,\n
                pokud chcete využívat všechny funkce slovníku, musíte přejít na Windows-10.""") 
              