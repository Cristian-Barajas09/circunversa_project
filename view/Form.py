import tkinter as tk
from tkinter import ttk
class Form(tk.Frame):
    permisos = True
    def __init__(self,ventana):
        super().__init__(ventana)
        self.ventana = ventana


        self.frame1 = ttk.Frame(self.ventana)
        self.frame2 = ttk.Frame(self.ventana)