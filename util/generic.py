from PIL import ImageTk,Image

def leer_image_tkinter(path,size):
    return ImageTk.PhotoImage(Image.open(path).resize(size,Image.ANTIALIAS))