# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:00:42 2022

@author: PIERO
"""
import sqlite3 as sql



conexion=sql.connect("bdbiblioteca.db")
cursor=conexion.cursor()


lista_autores=[('flor cerdan','14/2/78'),('daniel levano','14/5/79'),('Omar peña','15/5/80'),('Cesar zapata','4/9/78')]


lista_paises = [('Perú','A'),
              ('Argentina','A'),
              ('Colombia','A'),
              ('Venezuela','A'),
              ('Uruguay','A'),
              ('Paraguay','A'),
              ('USA','A')]

lista_editoriales = [('EIU','A'),
                    ('Macro','A'),
                    ('Bosch','A'),
                    ('Lima Sur','A'),
                    ('Pirámide','A'),
                    ('Colombus','A'),
                    ('Centro','A')]

lista_libros = [('Oracle 11g',10,2019,50,'A',1,1,1),
                ('Sistemas Operativos',14,2016,59,'A',1,4,3),
                ('Estructura de Datos',6,2018,20,'A',2,2,3),
                ('Algoritmos Python',8,2017,70,'A',2,2,1),
                ('BI',6,1998,50,'A',1,4,2),
                ('Ing. de Software',9,2000,56,'A',3,2,4),
                ('Organización de PC',9,2016,60,'A',7,2,1),
                ('Ensamblaje',9,2018,50,'A',4,4,3)]

consulta_pais = """ INSERT INTO
                PAIS(NOMBRE,ESTADO)
                VALUES(?,?)
                """
                
                
consulta_editorial = """ INSERT INTO
                    EDITORIAL(NOMBRE, ESTADO)
                    VALUES(?,?)
                    """
consulta_autor =""" INSERT INTO
                    AUTOR(NOMBRE, F_NACIMIENTO)
                    VALUES(?,?)
                """

consulta_libro = """ INSERT INTO
                      LIBRO(TITULO, CANTIDAD, ANIO,PRECIO, ESTADO,IDAUTOR,IDEDITORIAL, IDPAIS)
                      VALUES(?,?,?,?,?,?,?,?)
                """

cursor.executemany(consulta_pais,lista_paises)
cursor.executemany(consulta_editorial,lista_editoriales)
cursor.executemany(consulta_autor,lista_autores)
cursor.executemany(consulta_libro, lista_libros)

conexion.commit()

conexion.close()