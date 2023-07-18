-- Active: 1687916797927@@127.0.0.1@3306@circunversa
CREATE DATABASE circunversa;

USE circunversa;

CREATE TABLE cargos(
	id_tipo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
);

INSERT INTO cargos (nombre) VALUES ("admin"),("administracion"),("empleado");

CREATE TABLE empleados(
	cedula INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    cargo_empleado INT NOT NULL DEFAULT 1,
    contrasenna VARCHAR(250) NOT NULL,

    CONSTRAINT fk_cargo FOREIGN KEY (cargo_empleado) REFERENCES cargos(id_tipo)
);

CREATE TABLE session(
    cedula INT NOT NULL,
    status BOOLEAN NOT NULL,
    CONSTRAINT fk_empleado_sesion FOREIGN KEY (cedula) REFERENCES empleados(cedula)
);


CREATE TABLE nominas (
	cedula INT NOT NULL,
    salario INT NOT NULL,
    CONSTRAINT fk_empleado FOREIGN KEY (cedula) REFERENCES empleados(cedula)
);

CREATE TABLE porcentajes(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    porcentaje INT NOT NULL DEFAULT 40,
    id_cargo INT NOT NULL,
    CONSTRAINT fk_cargo_salario FOREIGN KEY (id_cargo) REFERENCES cargos(id_tipo)
);

CREATE TABLE bucetas(
    numero INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    conductor INT NOT NULL,
    CONSTRAINT fk_conductor FOREIGN KEY (conductor) REFERENCES empleados(cedula)
);

CREATE TABLE control_bucetas(
    numero INT NOT NULL,
    salida DATETIME DEFAULT CURRENT_TIMESTAMP,
    llegada DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_buceta FOREIGN KEY (numero) REFERENCES bucetas(numero)
);







