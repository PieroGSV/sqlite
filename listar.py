# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:20:43 2022

@author: PIERO
"""
import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()
consulta =""" SELECT *
            FROM LIBRO
            WHERE
                precio>=55
            ORDER BY titulo
          """
cursor= conexion.cursor()
cursor.execute(consulta)
print()