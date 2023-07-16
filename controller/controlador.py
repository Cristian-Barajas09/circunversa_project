from model.modelo import Modelo
class Controlador:
    def __init__(self):
        self.modelo = Modelo("root","localhost","circunversa","cb300804")

    def crear_usuario(self,cedula,nombre,apellido,contrasenna,cargo):
        if (
            cedula == "" or
            nombre == "" or
            apellido == "" or
            contrasenna == "" or
            cargo == ""
            ):
            return 0
        else:
            return self.modelo.crear_usuario(cedula,nombre,apellido,contrasenna,cargo)

    def obtener_usuario(self,cedula):
        return self.modelo.obtener_usuario(cedula)


    def obtener_usuarios(self):
        return self.modelo.obtener_usuarios()


    def actualizar_usuario(self,cedula,nombre,apellido,contrasenna,cargo):
        return self.modelo.actualizar_usuario(cedula,nombre,apellido,contrasenna,cargo)


    def eliminar_usuario(self,cedula):
        return self.modelo.eliminar_usuario(cedula)


    def obtener_salario(self,cedula):
        return self.modelo.obtener_salario(cedula)


    def guardar_salario(self,cedula,salario):
        return self.modelo.guardar_salario(cedula,salario)


    def actualizar_salario(self,cedula,salario):
        return self.modelo.actualizar_salario(cedula,salario)


    def eliminar_salario(self,cedula):
        return self.modelo.eliminar_salario(cedula)