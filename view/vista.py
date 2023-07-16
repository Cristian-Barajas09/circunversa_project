import tkinter as tk
from tkinter import ttk
from controller.controlador import Controlador

class Vista:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Circunversa")
        self.root.configure(bg="#222")

        s = ttk.Style(self.root)
        s.configure('TNotebook',background='#222')
        s.configure('Treeview',background='#222')

        self.notebook =  ttk.Notebook(self.root)

        self.trabajadores()
        self.vehiculos()
        self.notebook.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.mainloop()

    def trabajadores(self):
        self.frame1 = tk.Frame(self.notebook,bg="#222")
        self.frame1.pack()
        self.notebook.add(self.frame1,text="Trabajadores")

        frame1 = ttk.Frame(self.frame1)
        frame1.pack(side="left")

        frame2 = ttk.Frame(self.frame1)
        frame2.pack(side="right")

        frame3 = ttk.Frame(frame2)
        frame3.pack(side="top")

        frame4 = ttk.Frame(frame2)
        frame4.pack(side="bottom")
        
        columns = ("cedula")
        self.tree = ttk.Treeview(frame4,columns=columns,show="headings")
        self.tree.heading('cedula',text="Cedula")

        # for item in self.get_users():
        #     self.tree.insert()

        self.tree.pack()

        


    def vehiculos(self):
        self.frame2 = tk.Frame(self.notebook,bg="#222")
        self.frame2.pack()
        self.notebook.add(self.frame2,text="Busceta")


    def get_users(self):
        return 