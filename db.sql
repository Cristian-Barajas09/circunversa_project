-- Active: 1687916797927@@127.0.0.1@3306@circunversa
CREATE DATABASE circunversa;

USE circunversa;

CREATE TABLE empleados(
	cedula INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    cargo_empleado INT NOT NULL DEFAULT 1,
    contrasenna VARCHAR(250) NOT NULL,

    CONSTRAINT fk_cargo FOREIGN KEY (cargo_empleado) REFERENCES cargos(id_tipo)
);

DROP TABLE empleados;
DROP TABLE nominas;



CREATE TABLE nominas (
	cedula INT NOT NULL,
    salario INT NOT NULL,
    CONSTRAINT fk_empleado FOREIGN KEY (cedula) REFERENCES empleados(cedula)
);





CREATE TABLE cargos(
	id_tipo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
);

INSERT INTO cargos (nombre) VALUES ("admin"),("administracion"),("empleado")