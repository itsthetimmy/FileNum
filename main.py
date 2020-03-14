import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os, sys
from pathlib import Path

class Public(): pass

class App():
    def __init__(self, master):
        super().__init__()
        self.CreateUI(master)
    
    def CreateUI(self, master):
        self.selectB = ttk.Button(master, text="...", command=lambda: commingsoon())
        self.selectB.config(width=3)
        self.selectB.pack(padx=50,pady=50)
        self.downloadB = ttk.Button(master, text="Ausführen", command=lambda: self.num(master))
        self.downloadB.config(width=20)
        self.downloadB.pack(padx=50,pady=50)

    def num(self,master):
        

    def GetSaveDir(self):
        self.osname = sys.platform
        self.location = filedialog.askdirectory()
        self.location=(str(Path(self.location)))
        self.getLocE.delete(0, "end")
        self.getLocE.insert(0, self.location)

def Start():
    root = tk.Tk()
    root.title("Datei Nummerierer")
    root.resizable(0,0)
    App(root)
    root.mainloop()

def commingsoon():
    tk.messagebox.showinfo("","Wurde noch nicht implementiert!")


if __name__ == "__main__":
    Start()