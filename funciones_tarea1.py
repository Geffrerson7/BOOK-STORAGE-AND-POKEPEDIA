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
def crearId(longitudLibros:list[Libro])->int:
    return longitudLibros

def agregarLibro(lastId: int, titulo: str, genero: str, isbn: str, editorial: str, autores: list[str]) -> Libro:
    libroCreado = Libro(lastId, titulo, genero, isbn, editorial, autores)
    return libroCreado

def ordenarLibrosPorTitulo(libros:list[Libro])->list[str]:
    titulosOrdenados=[]
    for libro in libros:
        titulosOrdenados.append(libro.get_titulo())
    return sorted(titulosOrdenados)

def actualizarLibro():
    pass