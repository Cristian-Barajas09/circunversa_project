import tkinter as tk
from tkinter import ttk
class Vista(tk.Tk):
    def __init__(self,master):
        super().__init__(master)

        self.root = master


        self.notebook =  ttk.Notebook(self.root,width=100,height=100)

        self.trabajadores()
        self.notebook.pack()
        self.pack()

    def trabajadores(self):
        self.frame1 = tk.Frame(self.notebook,bg="#333")
        self.frame1.pack()
        self.notebook.add(self.frame1,text="Trabajadores")


