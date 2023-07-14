from modelo import Modelo
class Controlador:
    def __init__(self):
        self.modelo = Modelo("root","localhost","circunversa","cb300804")

    def crear_usuario(self,cedula,nombre,apellido,contrasenna,cargo):
        return self.modelo.crear_usuario(cedula,nombre,apellido,contrasenna,cargo)


    def obtener_usuario(self,cedula):
        return self.modelo.obtener_usuario(cedula)


    def obtener_usuarios(self):
        return self.modelo.obtener_usuarios()


    def actualizar_usuario(self,cedula,nombre,apellido,contrasenna,cargo):
        return self.modelo.actualizar_usuario(cedula,nombre,apellido,contrasenna,cargo)

    def eliminar_usuario(self,cedula):
        return self.modelo.eliminar_usuario(cedula)