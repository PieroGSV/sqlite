# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:35:04 2022

@author: PIERO
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

cursor=conexion.cursor()
consulta=""" DELETE FROM EDITORIAL
         WHERE
          IDEDITORIAL = 5
         """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()