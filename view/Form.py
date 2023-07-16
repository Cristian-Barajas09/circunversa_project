import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from controller.controlador import Controlador
class Form(tk.Frame):
    permisos = True
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana = ventana
        self.ventana.wm_title("Circunversa")
        self.ventana.wm_geometry("500x400")
        self.ventana.configure(bg="#333")
        self.ctrl = Controlador()


        style= Style(self.ventana)

        s_entry = {
            'fieldbackground':"#9C0B0B",
            'foreground':'#fff',
        }

        style.theme_use("clam")
        style.configure('TEntry',**s_entry)


        label1 = ttk.Label(self.ventana,text="Cedula")
        label1.pack()

        self.cedula = ttk.Entry(self.ventana,)
        self.cedula.pack()

        label2 = ttk.Label(self.ventana,text="contraseña")
        label2.pack()

        self.password = ttk.Entry(self.ventana,show="*")
        self.password.pack()
