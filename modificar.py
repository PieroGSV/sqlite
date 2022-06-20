# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 11:03:55 2022

@author: PIERO
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta= """ UPDATE EDITORIAL SET 
            NOMBRE= 'Editorial imprenta union'
            WHERE
            IDEDITORIAL = 1
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()