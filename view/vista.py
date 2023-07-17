import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from controller.controlador import Controlador

class Vista:
    def __init__(self,usuario):

        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Circunversa")
        self.root.configure(bg="#222")
        self.session = usuario

        self.control = Controlador()

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
        s.configure('Treeview',background='#F52020')
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

        result = self.control.obtener_usuarios()

        columns = ("cedula","nombre","apellido")
        self.tree = ttk.Treeview(self.frame1,columns=columns,show="headings")
        for item in range(len(columns)):
            self.tree.column("#"+str(item),width=100,stretch=False)
        self.tree.heading('cedula',text="Cedula")
        self.tree.heading('nombre',text="Nombre")
        self.tree.heading('apellido',text="Apellido")

        for item in self.get_users():
            self.tree.insert('',tk.END,item[0])

        self.tree.place(relx=0,rely=0.3,relwidth=1,relheight=0.65)
        btn = ttk.Button(self.frame1,text="Agregar empleado",command=self.crear_usuario)
        if self.session[3] == 1:
            btn.place(relx=0.4,rely=0.95)



    def salarios(self):
        self.fsalarios = tk.Frame(self.notebook,bg="#222")
        self.fsalarios.pack()
        self.notebook.add(self.fsalarios,text="salarios")


    def vehiculos(self):
        self.frame2 = tk.Frame(self.notebook,bg="#222")
        self.frame2.pack()
        self.notebook.add(self.frame2,text="Busceta")


    def get_users(self):
        return self.control.obtener_usuarios()


    def buscar(self,search,param):
        self.carga = tk.Toplevel()
        self.carga.wm_geometry("200x30")
        carga = ttk.Progressbar(self.carga)

        carga.pack()
        carga.start(30)
        result = self.control.busqueda(search,param)

        if not(isinstance(result,list)):
            messagebox.showerror("Error",result)
        else:
            if len(result) > 0:
                carga.destroy()
                self.trabajadores()

        print(search,param)

    def crear_usuario(self):
        self.w1 = tk.Toplevel()
        self.w1.wm_title("Agregar usuario")
        self.w1.configure(bg="#222")
        self.w1.wm_geometry("200x400")

        self.lcedula = ttk.Label(self.w1)
        self.cedula = ttk.Entry(self.w1)

        self.lnombre =ttk.Label(self.w1)
        self.nombre = ttk.Entry(self.w1)

        self.lapellido = ttk.Label(self.w1)
        self.apellido = ttk.Entry(self.w1)

        self.lcargo = ttk.Label(self.w1)
        self.cargo = ttk.Combobox(self.w1)

        self.lpassword = ttk.Label(self.w1)
        self.password = ttk.Entry(self.w1,show='*')

        btn = ttk.Button(self.w1,text="Guardar")