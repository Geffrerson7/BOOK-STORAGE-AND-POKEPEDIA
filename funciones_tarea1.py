import csv
import os
import re
from tabulate import tabulate

os.system("cls")
from libro import *
from funciones_utilidades import *

def CargarArchivo(objetos_libros) -> list:
    try:
        print("***** CARGAR EL ARCHIVO DE LIBROS *******")
        direccion = input("Escriba la dirección del archivo .txt o .csv: ")
        with open(direccion, "r", encoding = 'utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)


            for row in csv_reader:
                autores = row['AUTORES'].split(',')
                id = crearId(len(objetos_libros))
                libro = Libro(id, row['TITULO'], row['GENERO'], row['ISBN'], row['EDITORIAL'], autores)
                objetos_libros.append(libro)
            print("Archivo cargado")
            
    except:
        print("No existe el archivo") 

def crearId(longitudLibros:int)->int:
    return longitudLibros

def crearLibro(lista_libros:list[Libro]) -> Libro:
    lastId = crearId(len(lista_libros))
    print("Ingrese datos del libro:")
    titulo = validarLeerStrings(" -Título:")
    genero = validarLeerStrings(" -Género: ")
    isbn = validarISBN()
    editorial = validarLeerStrings(" -Editorial: ")
    nroAutores = validarNroAutores()
    autores = leerArrayStrings("  ->Autor ", nroAutores)
    libroCreado = Libro(lastId, titulo, genero, isbn, editorial, autores)
    return libroCreado

def validarNroAutores()->int:
    while True:
        nroAutores = validarLeerInt(" -Nro de autores:")
        if(nroAutores>0):
            return nroAutores
        print("[Se debe ingresar al menos 1 autor para el libro]")

def validarISBN()->str:
    while True:
        isbn = validarLeerStrings(" -ISBN: ")
        aux=isbn.replace("-","")
        if(len(aux)>=10 and len(aux)<=13):
            return isbn
        print("[El ISBN debe estar entre 10 o 13 digitos numéricos (Ejemplo: 789-46-4268-197-5 o 7894642681975)]")

def ordenarLibrosPorTitulo(libros:list[Libro])->list[str]:
    titulosOrdenados=[libro.get_titulo() for libro in libros]
    head = ["Orden","Título"]
    data = []
    for i,titulo in enumerate(sorted(titulosOrdenados),start=1):
      data.append([i,titulo])
    # # display table
    print(tabulate(data, headers=head, tablefmt="grid")) 

def actualizarLibro(libro:Libro)->Libro:
    variablesActualizar=["titulo","título","género", "genero", "isbn", "editorial", "autores"]
    atributo=validarLeerStrings("¿Qué desea modificar [título,género,ISBN,editorial o autores]?: ").lower()
    mensaje="[*** Libro actualizado ****]"
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
                autores,mensaje=modificarAutor(libro)
                libro.set_autores(autores)
            print(mensaje)
            return libro
        print("[El valor ingresado no es una opción disponible]")
        atributo=validarLeerStrings("¿Qué desea modificar [título,género,ISBN,editorial o autores]?: ").lower()
        

def modificarAutor(libro:Libro)->list[str]:
    print("**** Autores ****")
    autores=libro.get_autores()
    creacionMenu(["Agregar autor","Eliminar autor","Modificar autor existente"])
    op=validarRangoInt(1,3,"Ingrese una opción: ")
    mensaje="[*** Libro actualizado ****]"
    if(op==1):
        autor=validarLeerStrings(" ->Nuevo autor:")
        autores.append(autor)
    elif(op==2):
        if(len(libro.get_autores())==1):
            mensaje="[ERROR: El libro debe tener al menos 1 autor]"
        else:
            autor=validarLeerStrings(" ->Nombre de autor a eliminar:")
            if(autor in autores):
                index=autores.index(autor)
                autores.pop(index)
            else:
                mensaje="[ERROR: El autor ingresado no existe]"
    elif(op==3):
        autor=validarLeerStrings(" ->Nombre de autor a modificar:")
        if(autor in autores):
            index=autores.index(autor)
            autores[index]=autor
        else:
            mensaje="[ERROR: El autor ingresado no existe]"
    return autores,mensaje

def buscarISBN(isbn:str,lista_libros:list[Libro])->Libro:
    for libro in lista_libros:
        if(libro.get_ISBN()==isbn):
            return libro,lista_libros.index(libro)
    return None,-1

def Buscar_en_libros(cadena: str, libros: list, tipo_separador: str, tipo_key: str):
    cadena_list = cadena.split(tipo_separador)
    indice_libros = []
    
    for palabra in cadena_list:
      srch_result = 0
      for indice,libro in enumerate(libros):
        if tipo_key == 'titulo':
            srch_result = libro.get_titulo().lower().find(palabra)
        else:
            srch_result = libro.get_ISBN().lower().find(palabra)
        if srch_result != -1:
            indice_libros.append(indice)
    indices_libros = set(indice_libros)   
    
    result = []
    for indice in indices_libros:
      result.append(libros[indice])
    return result


def Buscar_libro_por_ISBN_o_título(data):
    variable_a_buscar = input("¿Desea buscar por título o por ISBN?")
    #ISBN = re.search("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$", input_user)

    if variable_a_buscar == 'ISBN':
       print(Buscar_en_libros(variable_a_buscar, data, '-','ISBN'))
    else:
      print(Buscar_en_libros(variable_a_buscar, data, ' ','titulo'))


def listar(libros_data):
    # create header
    head = ["Título", "Género", "ISBN", "Editorial", "Autores"]
    data = []
    for libro in libros_data:
        autores="\n".join(libro.get_autores())
        data.append([libro.get_titulo(), libro.get_genero(), libro.get_ISBN(), libro.get_editorial(), autores])

    # # display table
    print(tabulate(data, headers=head, tablefmt="grid"))

def eliminarLibro(isbn:str, lista_libros:list[Libro]) -> None:
    for libro in lista_libros:
        if libro.get_ISBN() == isbn:
            lista_libros.pop(lista_libros.index(libro))
    print("El libro ha sido eliminado")

def Buscar_libro_por_autor_editorial_o_título(lista_libros):
    creacionMenu(["Autor", "Editorial", "Genero", "Salir al Menú"])
    op=validarRangoInt(1,4,"Ingrese la opción ed búsqueda: ")
   
    if op == 1:
        variable_a_buscar = "autor"
        autor_a_buscar = validarLeerStrings("Ingrese el nombre del autor: ")
        libros_encontrados = Buscar_en_libros_2(variable_a_buscar, lista_libros, autor_a_buscar)
        listar(libros_encontrados)
    elif op == 2:
        variable_a_buscar = "editorial"
        editorial_a_buscar = validarLeerStrings("Ingrese el nombre de la editorial: ")
        libros_encontrados = Buscar_en_libros_2(variable_a_buscar, lista_libros, editorial_a_buscar)
        listar(libros_encontrados)
    elif op == 3:
        variable_a_buscar = "genero"
        genero_a_buscar = validarLeerStrings("Ingrese el nombre del genero: ")
        libros_encontrados = Buscar_en_libros_2(variable_a_buscar, lista_libros, genero_a_buscar)
        listar(libros_encontrados)
    else:
        print("Adiós")
    
def guardarlibros(Lista : list) -> None:
    formato = validarLeerStrings("¿Desea guardar la lista de libros en un .txt o .csv? ")
    if formato == '.txt':
        with open(".\lista_de_libros.txt", "w", newline="") as txt_file:
            txt_writer=csv.writer(txt_file, delimiter=",")
            for linea in Lista:
                txt_writer.writerow(linea)
        print("La lista de archivos se guardó en lista_libros.txt")

    elif formato == '.csv':
        with open("lista_de_libros.csv", "w", newline="") as csv_file:
            csv_writer=csv.writer(csv_file, delimiter=",")
            for linea in Lista:
                csv_writer.writerow(linea)
        print("La lista de archivos se guardó en lista_libros.csv")
    else:
        print("El tipo de archivo ingresado no es el correcto")

def Buscar_en_libros_2(atributoBuscar: str, libros: list[Libro], palabraBuscar: str):
    resultados = []
    for libro in libros:
        srch_result = -1
        if atributoBuscar == 'autor':
            autores = libro.get_autores()
            if palabraBuscar in autores:
                srch_result = 0
            
        if atributoBuscar == 'editorial':
            editorial = libro.get_editorial()
            srch_result = editorial.find(palabraBuscar)
            
        if atributoBuscar == 'genero':
            genero = libro.get_genero()
            srch_result = genero.find(palabraBuscar)
           
        if srch_result != -1:
            resultados.append(libro)
    return resultados