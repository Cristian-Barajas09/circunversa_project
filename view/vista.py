import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from controller.controlador import Controlador
from styles.styles import btn,label
class Vista:
    def __init__(self,usuario):

        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Circunversa")
        self.root.configure(bg="#222")
        self.session = usuario

        self.ctrl = Controlador()

        s = ttk.Style(self.root)
        s.configure('TNotebook',background='#222')


        self.notebook =  ttk.Notebook(self.root)

        self.trabajadores()
        self.vehiculos()
        self.salarios()
        self.notebook.place(x=0,y=0,relwidth=1,relheight=1)

        self.root.mainloop()

    def trabajadores(self):
        self.frame1 = tk.Frame(self.notebook,bg="#222")
        self.frame1.pack()
        self.notebook.add(self.frame1,text="Trabajadores")

        s = ttk.Style(self.frame1)
        s.configure('TFrame',background="#222")



        frame_search = ttk.Frame(self.frame1)
        frame_search.place(relx=0,rely=0,relwidth=1,relheight=0.3)

        self.search = ttk.Entry(frame_search,justify="right")
        self.search.place(relx=0.26,rely=0.2,width=180,height=25)

        self.select = ttk.Combobox(frame_search,values=("cedula","nombre","apellido"),state="readonly")
        self.select.current(0)
        self.select.place(relx=0.26,rely=0.21,width=50)

        btn_search = ttk.Button(frame_search,text="buscar",command=lambda: self.buscar(self.search.get(),self.select.get()))
        btn_search.place(relx=0.57,rely=0.2,width=50,height=25)


        columns = ("cedula","nombre","apellido")
        self.tree = ttk.Treeview(self.frame1,columns=columns,show="headings")

        self.tree.heading('cedula',text="Cedula")
        self.tree.heading('nombre',text="Nombre")
        self.tree.heading('apellido',text="Apellido")

        for item in self.get_users():
            self.tree.insert('',tk.END,values=(item[0],item[1],item[2]))

        self.tree.place(relx=0,rely=0.3,relwidth=1,relheight=0.65)
        btn = ttk.Button(self.frame1,text="Agregar empleado",command=self.crear_usuario)


        if self.session[3] == 1:
            btn.place(relx=0.4,rely=0.95)



    def salarios(self):
        self.fsalarios = tk.Frame(self.notebook,bg="#222")
        self.fsalarios.pack()
        self.notebook.add(self.fsalarios,text="salarios")

        texto1= ttk.Entry(self.fsalarios)
        texto1.insert(0,'cargo')
        texto1.pack()

        labelCargo = ttk.Label(self.w1,text="Cargo a ejercer")
        labelCargo.pack()

        result = self.get_cargos()
        values = []
        id_cargo = []
        for item in result:
            id_cargo.append(item[0])
            values.append(f"{item[0]}-{item[1]}")
        cargo = ttk.Combobox(self.w1,values=values,state="readonly")
        cargo.pack()

        texto2= ttk.Entry(self.fsalarios)
        texto2.insert(0,'Pago')
        texto2.pack()

        labelCargo = ttk.Label(self.w1,text="Cargo a ejercer")
        labelCargo.pack()

        result = self.get_cargos()
        values = []
        id_cargo = []
        for item in result:
            id_cargo.append(item[0])
            values.append(f"{item[0]}-{item[1]}")
        cargo = ttk.Combobox(self.w1,values=values,state="readonly")
        cargo.pack()

        boton1= ttk.Entry(self.fsalarios)
        boton1.insert(0,'PAGAR')
        boton1.pack()

    def vehiculos(self):
        self.frame2 = tk.Frame(self.notebook,bg="#222")
        self.frame2.pack()
        self.notebook.add(self.frame2,text="Busceta")


    def get_users(self):
        return self.ctrl.obtener_usuarios()


    def buscar(self,search,param):
        self.carga = tk.Toplevel()
        self.carga.wm_geometry("200x30")
        carga = ttk.Progressbar(self.carga)

        carga.pack()
        carga.start(30)
        print(search)
        result = self.ctrl.busqueda(search,param)

        if not(isinstance(result,list)):
            messagebox.showerror("Error",result)
        else:
            if len(result) > 0:
                self.carga.destroy()
                self.tree.delete(*self.tree.get_children())
                for item in result:
                    self.tree.insert('',tk.END,values=(item[0],item[1],item[2]))
                self.frame1.update()

    def crear_usuario(self):
        self.w1 = tk.Toplevel()
        self.w1.wm_title("Registro")
        self.w1.wm_geometry("400x400")
        self.w1.configure(bg="#222")
        self.ctrl = Controlador()


        style = ttk.Style(self.w1)
        style.map("C.TButton",**btn)

        style.configure('TLabel',**label)

        etiqueta = ttk.Label(self.w1, text = "Registro",font=(15))
        etiqueta.pack(pady=10)

        nombre1 = ttk.Label(self.w1, text = "Nombre")
        nombre1.pack()
        nombreTexto = ttk.Entry(self.w1)
        nombreTexto.pack(pady=5)

        apellido1 = ttk.Label(self.w1, text = "Apellido")
        apellido1.pack()
        apellidoTexto = ttk.Entry(self.w1)
        apellidoTexto.pack(pady=5)

        cedula1 = ttk.Label(self.w1, text = "Cedula")
        cedula1.pack()
        cedulaTexto = ttk.Entry(self.w1)
        cedulaTexto.pack(pady=5)

        labelContrasena = ttk.Label(self.w1, text = "Contraseña")
        labelContrasena.pack()
        self.contrasena1 = ttk.Entry(self.w1,show="*")
        self.contrasena1.pack(pady=5)


        labelConfirm = ttk.Label(self.w1,text="Confirmar contraseña")
        labelConfirm.pack()
        self.confcontrasena1 = ttk.Entry(self.w1,show="*")
        self.confcontrasena1.pack(pady=5)

        labelCargo = ttk.Label(self.w1,text="Cargo a ejercer")
        labelCargo.pack()

        result = self.get_cargos()
        values = []
        id_cargo = []
        for item in result:
            id_cargo.append(item[0])
            values.append(f"{item[0]}-{item[1]}")
        cargo = ttk.Combobox(self.w1,values=values,state="readonly")
        cargo.pack()

        boton1 = ttk.Button(self.w1, text = "Registrar",style="C.TButton",command=lambda: self.registrar(cedulaTexto.get(),nombreTexto.get(),apellidoTexto.get(),self.contrasena1.get(),self.confcontrasena1.get(),cargo.get(),id_cargo))

        boton1.pack(pady=10)

    def show_password(self):
        if self.contrasena1.cget("show") == "*":
            self.contrasena1.configure(show="")
        else:
            self.contrasena1.configure(show="*")


    def registrar(self,cedula,nombre,apellido,contrasenna,confirm,cargo,id_cargo):
        result = self.ctrl.crear_usuario(cedula,nombre,apellido,contrasenna,confirm,cargo,id_cargo)
        if not(isinstance(result,int)):
            messagebox.showerror("error",result)
        else:
            if result > 0:
                messagebox.showinfo("status","guardado exitosamente")
                self.trabajadores()
                self.w1.destroy()
            else: messagebox.showerror("Error",f"no se pudo guardar a {nombre}")

    def get_cargos(self):
        return self.ctrl.get_cargos()