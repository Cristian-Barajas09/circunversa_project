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

        
