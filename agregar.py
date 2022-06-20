# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 09:54:03 2022

@author: PIERO
"""

import sqlite3

#con el comando connect buscará la base de datos
#que tenga ese nombre y si no lo tiene lo creara'''
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()

tabla_autor = """   CREATE TABLE IF NOT EXISTS autor(
                    idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    f_nacimiento TEXT
                    )
                    """



tabla_pais = """ CREATE TABLE IF NOT EXISTS pais(
                idpais INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE,
                estado TEXT
                )
                """
tabla_editorial=""" CREATE TABLE IF NOT EXISTS editorial(
                    ideditorail INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    estado TEXT
                    )
                    """

tabla_libro = """   CREATE TABLE IF NOT EXISTS libro(
                    idlibro INTEGER PRIMARU KEY AUTOINCREMENTE,
                    titulo TEXT,
                    cantidad ¡NTEGER,
                    anio INTEGER,
                    precio REAL,
                    estado TEXT,
                    idpais INTEGER REFERENCES pais,
                    ideditorial INTEGER REFERENCES editorial,
                    idautor INTEGER REFERENCES autor
                    )
                    """

cursor.execute(tabla_pais)  
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)


conexion.close()