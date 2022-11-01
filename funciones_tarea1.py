import csv
import os
os.system("cls")
from libro import *


def CargarArchivo() -> list:
    try:
        direccion = input("Escriba la dirección del archivo .txt o .csv: ")
        with open(direccion, "r", encoding = 'utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            objetos_libros=[]
            for row in csv_reader:
                autores = row['AUTORES'].split(',')
                libro = Libro(1, row['TITULO'], row['GENERO'], row['ISBN'], row['EDITORIAL'], autores)
                objetos_libros.append(libro)
            return objetos_libros
    except:
        print("No existe el archivo")         
