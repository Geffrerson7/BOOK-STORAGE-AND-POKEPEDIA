import csv
import os

from tabulate import tabulate

os.system("cls")
from libro import *
from funciones_utilidades import *


def CargarArchivo(objetos_libros) -> list:
    """Carga un archivo .csv o .txt del disco duro"""
    try:
        direccion = validarLeerStrings("Escriba la dirección del archivo .txt o .csv: ")
        with open(direccion, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                autores = row["AUTORES"].split(",")
                id = crearId(len(objetos_libros))
                libro = Libro(
                    id,
                    row["TITULO"],
                    row["GENERO"],
                    row["ISBN"],
                    row["EDITORIAL"],
                    autores,
                )
                objetos_libros.append(libro)
        print("Archivo cargado")

    except:
        print("No existe el archivo")


def crearId(longitudLibros: int) -> int:
    return longitudLibros


def crearLibro(lista_libros: list[Libro]) -> Libro:
    lastId = crearId(len(lista_libros))
    print("Ingrese datos del libro:")
    titulo = validarLeerStrings(" -Título:")
    genero = validarLeerStrings(" -Género: ")
    isbn = ingresarISBN(" -ISBN: ")
    editorial = validarLeerStrings(" -Editorial: ")
    nroAutores = validarNroAutores()
    autores = leerArrayStrings("  ->Autor ", nroAutores)
    libroCreado = Libro(lastId, titulo, genero, isbn, editorial, autores)
    return libroCreado


def validarNroAutores() -> int:
    while True:
        nroAutores = validarLeerInt(" -Número de autores:")
        if nroAutores > 0:
            return nroAutores
        print("[Se debe ingresar al menos 1 autor para el libro]")


def ingresarISBN(mensaje: str) -> str:
    while True:
        isbn = validarLeerStrings(mensaje)
        if ValidarISBN(isbn) is not None:
            return isbn
        print(
            "[El ISBN debe estar entre 10 o 13 digitos numéricos (Ejemplo: 789-46-4268-197-5)]"
        )


def ordenarLibrosPorTitulo(libros: list[Libro]) -> list[str]:
    titulosOrdenados = [libro.get_titulo() for libro in libros]
    head = ["Orden", "Título"]
    data = []
    for i, titulo in enumerate(sorted(titulosOrdenados), start=1):
        data.append([i, titulo])
    # # display table
    print(tabulate(data, headers=head, tablefmt="grid"))


def actualizarLibro(libro: Libro) -> Libro:
    variablesActualizar = [
        "titulo",
        "título",
        "género",
        "genero",
        "isbn",
        "editorial",
        "autores",
    ]
    atributo = validarLeerStrings(
        "¿Qué desea modificar [título,género,ISBN,editorial o autores]?: "
    ).lower()
    mensaje = "[*** Libro actualizado ****]"
    while True:
        if atributo in variablesActualizar:
            if atributo == variablesActualizar[0] or atributo == variablesActualizar[1]:
                titulo = validarLeerStrings(" -Nuevo Título:")
                libro.set_titulo(titulo)
            elif (
                atributo == variablesActualizar[2] or atributo == variablesActualizar[3]
            ):
                genero = validarLeerStrings(" -Nuevo Género: ")
                libro.set_genero(genero)
            elif atributo == variablesActualizar[4]:
                isbn = ingresarISBN(" -Nuevo ISBN: ")
                libro.set_ISBN(isbn)
            elif atributo == variablesActualizar[5]:
                editorial = validarLeerStrings(" -Nueva Editorial: ")
                libro.set_editorial(editorial)
            elif atributo == variablesActualizar[6]:
                autores, mensaje = modificarAutor(libro)
                libro.set_autores(autores)
            print(mensaje)
            return libro
        print("[El valor ingresado no es una opción disponible]")
        atributo = validarLeerStrings(
            "¿Qué desea modificar [título,género,ISBN,editorial o autores]?: "
        ).lower()


def modificarAutor(libro: Libro) -> list[str]:
    print("**** Autores ****")
    autores = [lib.lower() for lib in libro.get_autores()]
    creacionMenu(["Agregar autor", "Eliminar autor", "Modificar autor existente"])
    op = validarRangoInt(1, 3, "Ingrese una opción: ")
    mensaje = "[*** Libro actualizado ****]"
    if op == 1:
        autor = validarLeerStrings(" ->Nuevo autor:").lower()
        autores.append(autor)
    elif op == 2:
        if len(libro.get_autores()) == 1:
            mensaje = "[ERROR: El libro debe tener al menos 1 autor]"
        else:
            autor = validarLeerStrings(" ->Nombre de autor a eliminar:").lower()
            if autor in autores:
                index = autores.index(autor)
                autores.pop(index)
            else:
                mensaje = "[ERROR: El autor ingresado no existe]"
    elif op == 3:
        autor = validarLeerStrings(" ->Nombre del autor que desea modificar:").lower()
        if autor in autores:
            new_autor = validarLeerStrings(" ->Nuevo nombre:")
            index = autores.index(autor)
            autores[index] = new_autor
        else:
            mensaje = "[ERROR: El autor ingresado no existe]"
    return autores, mensaje


def buscarLibro(isbn: str, lista_libros: list[Libro]) -> list[Libro]:
    for libro in lista_libros:
        if libro.get_ISBN() == isbn:
            return libro, lista_libros.index(libro)
    return None, -1


def buscarISBN(isbn: str, lista_libros: list[Libro]) -> list[Libro]:
    result = []
    for libro in lista_libros:
        if libro.get_ISBN() == isbn:
            result.append(libro)
    if len(result) == 0:
        return 0
    else:
        return result


def Buscar_titulo(titulo: str, lista_libros: list[Libro]) -> list[Libro]:
    result = []
    for libro in lista_libros:
        if libro.get_titulo() == titulo:
            result.append(libro)
    if len(result) == 0:
        return 0
    else:
        return result


def Buscar_libro_por_ISBN_o_título(data):
    creacionMenu(["ISBN", "Titulo"])
    op = validarRangoInt(1, 2, "Ingrese la opción de búsqueda: ")

    if op == 1:
        ISBN = input("Ingrese el ISBN: ")
        if ValidarISBN(ISBN) == None:
            print("ISBN inválido")
        else:
            result_search = buscarISBN(ISBN, data)
            if result_search == 0:
                print("No se encontro ningun libro con ese ISBN")
            else:
                listar(result_search)

    elif op == 2:
        titulo = input("Ingrese el titulo: ")
        result_search = Buscar_titulo(titulo, data)
        if result_search == 0:
            print("No se encontro ningun libro con ese titulo")
        else:
            listar(result_search)
    else:
        print("Opción inválida")


def listar(libros_data):
    # create header
    head = ["Título", "Género", "ISBN", "Editorial", "Autores"]
    data = []
    for libro in libros_data:
        autores = "\n".join(libro.get_autores())
        data.append(
            [
                libro.get_titulo(),
                libro.get_genero(),
                libro.get_ISBN(),
                libro.get_editorial(),
                autores,
            ]
        )

    # # display table
    print(tabulate(data, headers=head, tablefmt="grid"))


def eliminarLibro(isbn: str, lista_libros: list[Libro]) -> None:
    """Funcion que elimina un libro almacenado en una lista cuyo parametro es el codigo isbn del libro"""
    DEL = 0
    for libro in lista_libros:
        if libro.get_ISBN() == isbn:
            lista_libros.pop(lista_libros.index(libro))
            DEL += 1
    if DEL == 1:
        print("El libro ha sido eliminado")
    else:
        print("ERROR: El código isbn no está en la lista")


def Buscar_libro_por_autor_editorial_o_título(lista_libros):
    """Funcion que lista los libros del autor, editorial o título a buscar"""
    creacionMenu(["Autor", "Editorial", "Genero", "Salir al Menú"])
    op = validarRangoInt(1, 4, "Ingrese la opción de búsqueda: ")

    if op == 1:
        variable_a_buscar = "autor"
        autor_a_buscar = validarLeerStrings("Ingrese el nombre del autor: ").lower()
        libros_encontrados = Buscar_en_libros_2(
            variable_a_buscar, lista_libros, autor_a_buscar
        )
        listar(libros_encontrados)
    elif op == 2:
        variable_a_buscar = "editorial"
        editorial_a_buscar = validarLeerStrings(
            "Ingrese el nombre de la editorial: "
        ).lower()
        libros_encontrados = Buscar_en_libros_2(
            variable_a_buscar, lista_libros, editorial_a_buscar
        )
        listar(libros_encontrados)
    elif op == 3:
        variable_a_buscar = "genero"
        genero_a_buscar = validarLeerStrings("Ingrese el nombre del genero: ").lower()
        libros_encontrados = Buscar_en_libros_2(
            variable_a_buscar, lista_libros, genero_a_buscar
        )
        listar(libros_encontrados)
    else:
        print("Adiós")


def guardarlibros(Lista: list) -> None:
    """Función que guarda los libros de una lista en un archivo .csv o .txt"""
    creacionMenu([".txt", ".csv", "Salir al Menú"])
    op = validarRangoInt(1, 3, "Ingrese la opción de búsqueda: ")
    if op == 1:
        txt_file = open(".\lista_de_libros.txt", "w", encoding="utf-8")
        txt_file.write("TITULO,GENERO,ISBN,EDITORIAL,AUTORES\n")

        for libro in Lista:
            autores = ",".join(libro.get_autores())
            data = ",".join(
                [
                    '"' + libro.get_titulo() + '"',
                    libro.get_genero(),
                    libro.get_ISBN(),
                    libro.get_editorial(),
                    '"' + autores + '"',
                ]
            )
            txt_file.write(data + "\n")
        txt_file.close()
        print("La lista de archivos se guardó en lista_de_libros.txt")

    elif op == 2:
        csv_file = open(".\lista_de_libros.csv", "w", encoding="utf-8")
        csv_file.write("TITULO,GÉNERO,ISBN,EDITORIAL,AUTORES\n")

        for libro in Lista:
            autores = ",".join(libro.get_autores())
            data = ",".join(
                [
                    '"' + libro.get_titulo() + '"',
                    libro.get_genero(),
                    libro.get_ISBN(),
                    libro.get_editorial(),
                    '"' + autores + '"',
                ]
            )
            csv_file.write(data + "\n")
        csv_file.close()
        print("La lista de archivos se guardó en lista_de_libros.csv")
    else:
        print("Adios")


def Buscar_en_libros_2(atributoBuscar: str, libros: list[Libro], palabraBuscar: str):
    """Funcion que retorna un lista de libros segun el autor, editorial o genero ingresado"""
    resultados = []
    for libro in libros:
        srch_result = -1
        if atributoBuscar == "autor":
            autores = [lib.lower() for lib in libro.get_autores()]
            for autor in autores:
                if not autor.find(palabraBuscar):
                    srch_result = 0
                    break
        if atributoBuscar == "editorial":
            editorial = libro.get_editorial().lower()
            srch_result = editorial.find(palabraBuscar)

        if atributoBuscar == "genero":
            genero = libro.get_genero().lower()
            srch_result = genero.find(palabraBuscar)

        if srch_result != -1:
            resultados.append(libro)
    return resultados


def Buscar_por_numero_autores(libros: list[Libro]):
    num_autores_user = int(input("Ingrese el número de autores: "))
    result_search = []
    for libro in libros:
        num_autores_libro = len(libro.get_autores())
        if num_autores_libro == num_autores_user:
            result_search.append(libro)
    listar(result_search)


def editar_libro(lista_libros):
    isbn = validarLeerStrings(" -Ingrese ISBN del libro a editar: ")
    libroActualizar, index = buscarLibro(isbn, lista_libros)
    if libroActualizar is not None:
        print("***** OPCIONES DE EDICIÓN ***** ")
        creacionMenu(
            [
                "Editar todos los datos del libro",
                "Actualizar un dato en especifico",
                "Cancelar",
            ]
        )
        op = validarRangoInt(1, 3, "Ingrese una opción: ")
        if op == 1:
            lista_libros[index] = crearLibro(lista_libros)
            print("[*** Libro editado ****]")
        if op == 2:
            libro = actualizarLibro(libroActualizar)
            lista_libros[index] = libro
    else:
        print("[El ISBN ingresado no está registrado en el sistema]")
    return lista_libros
