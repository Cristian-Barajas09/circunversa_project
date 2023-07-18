import tkinter as tk
from controller.controlador import Controlador
from .vista import Vista
from tkinter import messagebox
from util.passwords import matchPassword
from util.generic import leer_image_tkinter

class Form:
    def __init__(self,):
        self.w = tk.Tk()
        self.w.title("Ingresar")
        self.w.geometry("925x500")
        self.w.configure(bg="#fff")
        self.w.resizable(0,0)
        self.ctrl = Controlador()

        image = leer_image_tkinter("./img/bus.png",(300,400))

        tk.Label(self.w,image=image,bg="white").place(x=50,y=50)

        frame = tk.Frame(self.w,width=350,height=350,bg="white")
        frame.place(x=480,y=70)

        heading = tk.Label(frame,text="Ingresar",fg="#920",bg="white",font=('Microsoft Yahei UI Light',23,'bold'))
        heading.place(x=100,y=5)
        #########--------------------------------
        self.cedula = tk.Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.cedula.place(x=30,y=80)
        self.cedula.insert(0,'Cedula')
        self.cedula.bind('<FocusIn>',self.on_enter)
        self.cedula.bind('<FocusOut>',self.on_leave)

        tk.Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

        ###########----------------------------------
        self.password = tk.Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.password.place(x=30,y=150)
        self.password.insert(0,'Contraseña')
        self.password.bind('<FocusIn>',self.on_enter_pass)
        self.password.bind('<FocusOut>',self.on_leave_pass)

        tk.Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

        ####################################

        tk.Button(frame,width=39,pady=7,text='Ingresar',bg="#920",fg="white",border=0,command=lambda: self.ingresar(self.cedula.get(),self.password.get())).place(x=35,y=204)


        self.w.mainloop()


    def on_enter(self,e):
        self.cedula.delete(0,'end')

    def on_leave(self,e):
        ci = self.cedula.get()
        if ci == '':
            self.cedula.insert(0,'Cedula')

    def on_enter_pass(self,e):
        self.password.delete(0,'end')

    def on_leave_pass(self,e):
        pw = self.password.get()
        if pw == '':
            self.password.insert(0,'Cedula')

    def ingresar(self,cedula,password):
        result = self.ctrl.obtener_usuario(cedula)
        

        if isinstance(result,str):
            messagebox.showerror("Error",result)
        else:
            if len(result) > 0:
                if  not(matchPassword(password,result[4])):
                    return messagebox.showerror("Error","Contraseña erronea")
                messagebox.showinfo("bienvenido",f"Bienvenido {result[1]}")
                self.ctrl.set_sesion(cedula)
                self.w.destroy()
                Vista(result)
            else:
                messagebox.showerror("Error","Error al iniciar sesion")
    def get_session(self):
        result = self.ctrl.get_sesion()
        if result is None:
            return []
        return result

    



