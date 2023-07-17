import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from controller.controlador import Controlador
from styles.styles import btn,label
from .vista import Vista
class Form:
    def __init__(self,):
        self.ventana = tk.Tk()
        self.ventana.title("Registro")
        self.ventana.geometry("400x400")
        self.ventana.configure(bg="#222")
        self.ctrl = Controlador()


        style = Style(self.ventana)
        style.map("C.TButton",**btn)

        style.configure('TLabel',**label)

        etiqueta = ttk.Label(self.ventana, text = "Registro",font=(15))
        etiqueta.pack(pady=10)

        nombre1 = ttk.Label(self.ventana, text = "Nombre")
        nombre1.pack()
        nombreTexto = ttk.Entry(self.ventana)
        nombreTexto.pack(pady=5)

        apellido1 = ttk.Label(self.ventana, text = "Apellido")
        apellido1.pack()
        apellidoTexto = ttk.Entry(self.ventana)
        apellidoTexto.pack(pady=5)

        cedula1 = ttk.Label(self.ventana, text = "Cedula")
        cedula1.pack()
        cedulaTexto = ttk.Entry(self.ventana)
        cedulaTexto.pack(pady=5)

        labelContrasena = ttk.Label(self.ventana, text = "Contraseña")
        labelContrasena.pack()
        self.contrasena1 = ttk.Entry(self.ventana,show="*")
        self.contrasena1.pack(pady=5)


        labelConfirm = ttk.Label(self.ventana,text="Confirmar contraseña")
        labelConfirm.pack()
        self.confcontrasena1 = ttk.Entry(self.ventana,show="*")
        self.confcontrasena1.pack(pady=5)

        labelCargo = ttk.Label(self.ventana,text="Cargo a ejercer")
        labelCargo.pack()

        result = self.get_cargos()
        values = []
        id_cargo = []
        for item in result:
            id_cargo.append(item[0])
            values.append(item[1])
        cargo = ttk.Combobox(self.ventana,values=values)
        cargo.pack()

        boton1 = ttk.Button(self.ventana, text = "Registrar",style="C.TButton",command=lambda: self.registrar(nombreTexto.get(),apellidoTexto.get(),cedulaTexto.get(),self.contrasena1.get(),self.confcontrasena1.get(),cargo.get(),id_cargo))

        boton1.pack(pady=10)

        self.ventana.mainloop()


    def show_password(self):
        if self.contrasena1.cget("show") == "*":
            self.contrasena1.configure(show="")
        else:
            self.contrasena1.configure(show="*")


    def registrar(self,cedula,nombre,apellido,contrasenna,confirm,cargo,id_cargo):
        result = self.ctrl.crear_usuario(cedula,nombre,apellido,contrasenna,confirm,cargo,id_cargo)

        self.ventana.destroy()
        Vista()

    def get_cargos(self):
        return self.ctrl.get_cargos()
