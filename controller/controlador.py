from model.modelo import Modelo

from util.passwords import encryptPassword


class Controlador:
    def __init__(self):
        self.modelo = Modelo("root","localhost","circunversa","cb300804")

    def crear_usuario(self,cedula,nombre,apellido,contrasenna,confirm,cargo,id_cargo):
        if (
            cedula == "" or
            nombre == "" or
            apellido == "" or
            contrasenna == "" or
            cargo == "" or
            confirm == ""
            ):
            return "rellene todos los campos"
        else:
            if contrasenna != confirm:
                return "las contraseñas no son iguales"

            contrasenna = encryptPassword(contrasenna)

            for item in id_cargo:
                if cargo.startswith(str(item)):
                    cargo = item
                    break

            return self.modelo.crear_usuario(cedula,nombre,apellido,contrasenna,cargo)

    def obtener_usuario(self,cedula):
        if cedula == "":
            return "falta la cedula para poder buscar"
        else:
            return self.modelo.obtener_usuario(cedula)


    def obtener_usuarios(self):

        return self.modelo.obtener_usuarios()


    def actualizar_usuario(self,cedula,nombre,apellido,contrasenna,cargo):

        return self.modelo.actualizar_usuario(cedula,nombre,apellido,contrasenna,cargo)


    def eliminar_usuario(self,cedula):
        if cedula == "":
            return "falta la cedula para poder buscar"
        else:
            return self.modelo.eliminar_usuario(cedula)


    def obtener_salario(self,cedula):
        if cedula == "":
            return "falta la cedula para poder buscar"
        else:
            return self.modelo.obtener_salario(cedula)


    def guardar_salario(self,cedula,salario):

        porcentaje = self.get_porcentajes()

        salario_final = salario * porcentaje / 100

        return self.modelo.guardar_salario(cedula,salario_final)


    def actualizar_salario(self,cedula,salario):
        return self.modelo.actualizar_salario(cedula,salario)


    def eliminar_salario(self,cedula):
        return self.modelo.eliminar_salario(cedula)


    def get_cargos(self):
        return self.modelo.get_cargos()

    def get_cargo(self,id):
        return self.modelo.get_cargo(id)


    def set_porcentajes(self,value,id_cargo):
        return self.modelo.set_porcentajes(value,id_cargo)

    def get_porcentajes(self):
        return self.modelo.get_porcentajes()

    def busqueda(self,search,param):
        if param == "cedula":
            search = int(search)
        return self.modelo.busqueda(search,param)
    
    def set_sesion(self,cedula):
        self.modelo.set_sesion(cedula)

    def get_sesion(self):
        result = self.modelo.get_sesion()
        if result is None:
            return []
        return result
    
    def remove_sesion(self,cedula):
        self.modelo.remove_sesion(cedula)

    def get_bucetas(self):
        return self.modelo.get_bucetas()
