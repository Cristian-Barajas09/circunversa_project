from Form import Form
import tkinter as tk

if __name__ == '__main__':
    ventana = tk.Tk()

    ventana.wm_title("Ingresar")

    app = Form(ventana)

    app.mainloop()