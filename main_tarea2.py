from funciones_tarea2 import *
from funciones_utilidades import *

def menu():
    while True:
        funcionlimpiar()
        print("***** POKEPEDIA *******")
        creacionMenu(
            [
                "Listar pokemons por generación",
                "Listar pokemons por forma",
                "Listar pokemons por habilidad",
                "Listar pokemons por habitat",
                "Listar pokemons por tipo",
                "Salir"
            ]
        )
        opcion = validarRangoInt(1, 6, "Ingrese la opción: ")
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            funcionlimpiar()
            listadoPorHabilidad()
            regresarmenu()
        elif opcion == 4:
            pass
        elif opcion == 5:
            
            pass
        elif opcion == 6:
            break


def main():
    funcionlimpiar()
    menu()


if __name__ == "__main__":
    main()

