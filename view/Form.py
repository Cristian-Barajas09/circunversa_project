import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from controller.controlador import Controlador
from styles.styles import btn,label

from util.generic import leer_image_tkinter
class Form:
    def __init__(self,):
        self.w = tk.Tk()
        self.w.title("Ingresar")
        self.w.geometry("925x500+300+200")
        self.w.resizable(0,0)

        image = leer_image_tkinter("./img/bus.png",(200,400))

        self.frame1 = tk.Frame(self.w)
        self.frame1.pack(side="left")

        labelI = tk.Label(self.frame1,image=image)
        labelI.pack(side="left")

        self.frame2 = tk.Frame(self.w)
        self.frame2.place(relx=0.5,relwidth=0.5,relheight=1)

        self.cedula = tk.Entry(self.frame2,width=25,border=0,)
        self.cedula.place(relx=0.15,rely=0.3)
        tk.Frame(self.frame2,background="#333",width=120).place(relx=0.2,rely=0.34)

        self.w.mainloop()




