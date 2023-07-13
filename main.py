from vista import Vista
import tkinter as tk

if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.wm_title("Circunversa")



    app = Vista(ventana)
    app.mainloop()