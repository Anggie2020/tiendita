import sqlite3
import os
os.system("cls")

miConexion= sqlite3.connect("tiendita.db")
print("Conectado satisfactoriamete")
miCursor= miConexion.cursor()

miConexion.close()