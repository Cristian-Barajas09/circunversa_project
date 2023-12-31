import mysql.connector

class Modelo:
    def __init__(
            self,
            usuario,
            host,
            database,
            password=""
            ):
        self.__user = usuario
        self.__host = host
        self.__password = password
        self.__database = database

    def __conexion(self):
        database = mysql.connector.connect(
            user = self.__user,
            host = self.__host,
            password = self.__password,
            database = self.__database
        )

        return database


    def obtener_usuarios(self):
        con = self.__conexion()
        cur = con.cursor()

        cur.execute("SELECT * FROM empleados")
        result = cur.fetchall()
        con.close()
        return result

    def obtener_usuario(self,cedula):
        con = self.__conexion()
        cur = con.cursor()

        cur.execute(f"SELECT * FROM empleados WHERE cedula = {cedula}")
        result = cur.fetchone()
        con.close()
        return result


    """
        cedula INT NOT NULL PRIMARY KEY,
        nombre VARCHAR(30) NOT NULL,
        apellido VARCHAR(30) NOT NULL,
        cargo_empleado INT NOT NULL DEFAULT 1,
        contrasenna VARCHAR(250) NOT NULL,
        CONSTRAINT fk_cargo FOREIGN KEY (cargo_empleado) REFERENCES cargos(id_tipo)
    """

    def crear_usuario(
            self,
            cedula,
            nombre,
            apellido,
            contrasenna,
            cargo=1
            ):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"INSERT INTO empleados (cedula,nombre,apellido,contrasenna,cargo_empleado) VALUES ({cedula},'{nombre}','{apellido}','{contrasenna}',{cargo})")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def actualizar_usuario(
            self,
            cedula,
            nombre,
            apellido,
            contrasenna,
            cargo=1
            ):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"UPDATE empleados SET cedula={cedula},nombre='{nombre}',apellido='{apellido}',cargo_empleado={cargo},contrasenna='{contrasenna}'")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def eliminar_usuario(self,cedula):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"DELETE FROM empleados WHERE cedula = {cedula}")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def obtener_salario(self,cedula):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM nominas WHERE cedula = {cedula}")
        result = cur.fetchall()
        con.close()
        return result

    def guardar_salario(self,cedula,salario):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"INSERT INTO nominas (cedula,salario) VALUES ({cedula},{salario})")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def actualizar_salario(self,cedula,salario):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"UPDATE nominas SET cedula={cedula},salario={salario} WHERE cedula = {cedula}")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def eliminar_salario(self,cedula):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"DELETE FROM nominas WHERE cedula={cedula}")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def get_cargos(self):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute("SELECT * FROM cargos")
        result = cur.fetchall()
        con.close()
        return result

    def set_porcentaje(self,porcentaje,id_cargo):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"INSERT INTO porcentajes (porcentaje,id_cargo) VALUES ({porcentaje},{id_cargo})")
        con.commit()
        result = cur.rowcount
        con.close()
        return result


    def get_porcentajes(self):
        con = self.__conexion()
        cur = con.cursor()

        cur.execute("SELECT * FROM porcentajes")
        result = cur.fetchall()
        con.close()
        return result


    def busqueda(self,search,param):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM empleados WHERE {param} LIKE '{search}%'")
        result = cur.fetchall()
        con.close()
        return result


    def get_cargo(self,id):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM cargos WHERE id_tipo = {id}")
        result = cur.fetchone()
        con.close()
        return result
    
    def set_sesion(self,cedula):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"INSERT INTO session (cedula,status) VALUES ({cedula},TRUE)")
        con.commit()
        con.close()

    def get_sesion(self):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM session")
        result = cur.fetchone()
        con.close()
        return result
    
    def remove_sesion(self,cedula):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"DELETE FROM session WHERE cedula = {cedula}")
        con.commit()
        con.close()

    def get_bucetas(self):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM bucetas")
        result = cur.fetchone()
        con.close()
        return result
    
    def get_horario(self,numero):
        con = self.__conexion()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM control_bucetas WHERE numero = {numero}")
        result = cur.fetchone()
        con.close()
        return result