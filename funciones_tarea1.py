import csv
import os
os.system("cls")
from libro import *
from funciones_utilidades import *

def CargarArchivo() -> list:
        direccion = input("Escriba la dirección del archivo .txt o .csv: ")
        with open(direccion, "r", encoding = 'utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            objetos_libros=[]
            for row in csv_reader:
                autores = row['AUTORES'].split(',')
                libro = Libro(1, row['TITULO'], row['GENERO'], row['ISBN'], row['EDITORIAL'], autores)
                objetos_libros.append(libro)
            return objetos_libros
                # libro_2 = Libro(2, row[1]['TITULO'], row[1]['GENERO'], row[1]['ISBN'], row[1]['EDITORIAL'], row[1]['AUTORES'] )
                # libro_3 = Libro(3, row[2]['TITULO'], row[2]['GENERO'], row[2]['ISBN'], row[2]['EDITORIAL'], row[2]['AUTORES'] )

def crearId(longitudLibros:list[Libro])->int:
    return longitudLibros

def crearLibro(lista_libros:list[Libro]) -> Libro:
    lastId = crearId(len(lista_libros))
    print("Ingrese datos del libro:")
    titulo = validarLeerStrings(" -Título:")
    genero = validarLeerStrings(" -Género: ")
    isbn = validarLeerStrings(" -ISBN: ")
    editorial = validarLeerStrings(" -Editorial: ")
    nroAutores = validarLeerInt(" -Nro de autores:")
    autores = leerArrayStrings("  ->Autor ", nroAutores)
    libroCreado = Libro(lastId, titulo, genero, isbn, editorial, autores)
    return libroCreado

def ordenarLibrosPorTitulo(libros:list[Libro])->list[str]:
    titulosOrdenados=[libro.get_titulo() for libro in libros]
    return sorted(titulosOrdenados)

def actualizarLibro(libro:Libro)->Libro:
    variablesActualizar=["titulo","título","género", "genero", "isbn", "editorial", "autores"]
    atributo=validarLeerStrings("¿Qué desea modificar [título,género,ISBN,editorial o autores]?: ").lower()
    while True:
        if(atributo in variablesActualizar):
            if(atributo==variablesActualizar[0] or atributo==variablesActualizar[1]):
                titulo = validarLeerStrings(" -Nuevo Título:")
                libro.set_titulo(titulo)
            elif(atributo==variablesActualizar[2] or atributo==variablesActualizar[3]):
                genero = validarLeerStrings(" -Nuevo Género: ")
                libro.set_genero(genero)
            elif(atributo==variablesActualizar[4]):
                isbn = validarLeerStrings(" -Nuevo ISBN: ")
                libro.set_ISBN(isbn)
            elif(atributo==variablesActualizar[5]):
                editorial = validarLeerStrings(" -Nueva Editorial: ")
                libro.set_editorial(editorial)
            elif(atributo==variablesActualizar[6]):
                autores=modificarAutor(libro)
                libro.set_autores(autores)
            return libro
        atributo=validarLeerStrings("¿Qué desea modificar [título,género,ISBN,editorial o autores]?: ").lower()
        print("[El valor ingresado no es una opción disponible]")

def modificarAutor(libro:Libro)->list[str]:
    print("**** Autores ****")
    autores=libro.get_autores()
    creacionMenu(["Agregar autor","Eliminar autor","Modificar autor existente"])
    op=validarRangoInt(1,3,"Ingrese una opción: ")
    if(op==1):
        autor=validarLeerStrings(" ->Nuevo autor:")
        autores.append(autor)
    elif(op==2):
        if(len(libro.get_autores())==1):
            print("[ERROR: El libro debe tener al menos 1 autor]")
        else:
            autor=validarLeerStrings(" ->Nombre de autor a eliminar:")
            if(autor in autores):
                index=autores.index(autor)
                autores.pop(index)
            else:
                print("[ERROR: El autor ingresado no existe]")
    elif(op==3):
        autor=validarLeerStrings(" ->Nombre de autor a modificar:")
        if(autor in autores):
            index=autores.index(autor)
            autores[index]=autor
        else:
            print("[ERROR: El autor ingresado no existe]")
    return autores

def buscarISBN(isbn:str,lista_libros:list[Libro])->Libro:
    for libro in lista_libros:
        if(libro.get_ISBN()==isbn):
            return libro,lista_libros.index(libro)
    return None,-1
