import os
import re


def regresarmenu():
    input("Presione una tecla para regresar ...")


def funcionlimpiar():
    """Limpia la pantalla de la consola"""
    # os.name (define el sistema operativo), var es la palabra para limpiar pantalla
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    os.system(var)


def validarLeerStrings(mensaje: str) -> str:
    """Recibe un mensaje para el input y valida que el dato ingresado no sea un str vacio"""
    while True:
        variableLeer = input(mensaje)
        if variableLeer != "":
            return variableLeer.strip()
        print("[El valor a ingresar no debe ser vacio]")


def validarLeerInt(mensaje: str) -> int:
    """Recibe un mensaje para el input y valida que el dato ingresado no sea una variable de tipo str"""
    while True:
        variableLeer = input(mensaje)
        if variableLeer.isnumeric():
            variableLeer = int(variableLeer)
            return variableLeer
        print("[El valor a ingresar debe ser un NÚMERO]")


def validarRangoInt(inicio: int, final: int, mensaje: str) -> int:
    """Valida que una opcion ingresada este en el rango indicado y valida que sea un entero"""
    while True:
        variable = validarLeerInt(mensaje)
        if variable >= inicio and variable <= final:
            return variable
        print("[El número ingresado no está en el rango indicado]")


def validarRangoConString(
    inicio: int, final: int, stringAceptados: list[str], mensaje: str
) -> int:
    """Valida que una opcion ingresada este en el rango indicado, ademas acepta string de una lista"""
    while True:
        variable = input(mensaje)
        if variable.isnumeric():
            variable = int(variable)
            if variable >= inicio and variable <= final:
                return variable
            print("[El número ingresado no está en el rango indicado]")
        elif variable.lower() in stringAceptados:
            return variable.lower()
        print("[La variable ingresada no es válida]")


def leerArrayStrings(mensaje: str, longitud: int) -> list[str]:
    """Recibe un mensaje para el input y la longitud del array a recorrer, solo es para valores de tipo str"""
    lista = []
    for i in range(1, longitud + 1):
        variable = validarLeerStrings(mensaje + str(i) + ":")
        lista.append(variable)
    return lista


def creacionMenu(opciones: list[str], start=1) -> None:
    """Crea un menú de opciones a partir de una lista"""
    for i, opcion in enumerate(opciones, start=start):
        print(str(i) + ") " + opcion)


def ValidarISBN(ISBN: str):
    """Valida el código ISBN"""
    result = re.search("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$", ISBN)
    try:
        return result
    except:
        return
