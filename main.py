import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
import os, sys
from pathlib import Path

class Public(): pass

class App():
    def __init__(self, master):
        super().__init__()
        self.CreateUI(master)
    
    def CreateUI(self, master):
        self.downloadB = ttk.Button(master, text="Nummerieren", command=lambda: self.num(master))
        self.downloadB.config(width=20)
        self.downloadB.pack(pady=2)

    def num(self,master):
        print("test")


def Start():
    root = tk.Tk()
    root.title("Datei Nummerierer")
    root.resizable(0,0)
    App(root)
    root.mainloop()

if __name__ == "__main__":
    Start()