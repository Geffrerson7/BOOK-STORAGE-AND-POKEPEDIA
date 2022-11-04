from funciones_utilidades import *
import requests
from Pokemon import *
from tabulate import tabulate
# OPCION 3: LISTAR POR HABLIDAD - RAISA
# 		A. INGRESE LA HABILIDAD
#        B. VER OPCIONES DE HABILIDADES - > FUNCION PANEL: DEL 1 - 327
# 											   FUNCION GENERADORA PARA MOSTRAR OPCIONES DE 10 EN 10
URLHABILIDADES="https://pokeapi.co/api/v2/ability/"

def listarHabilidad():
    print("********** LISTADO POR HABILIDADES ********")
    creacionMenu(["Ingrese la habilidad","Ver opciones de habilidades","Cancelar"])
    op=validarRangoInt(1,3,"Elija una opción: ")
    if(op==1):
        habilidad=validarLeerStrings(" -Ingrese la habildad a buscar: ")
        lista=buscarHabilidad(habilidad)
        if(lista):
            listar(lista)
    elif(op==2):
        pass

def mostrarHabildades():
    try:
        print("Existen","habilidades solo se muestran","si desea ver más ingrese la opción 0")
        pass
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")

def listadoGneral(diccionario:dict):
    for pokemon in diccionario:
        yield pokemon["pokemon"]["url"]


def buscarHabilidad(habilidad):
    listado_Pokemones=[]
    try:
        request=requests.get(URLHABILIDADES+habilidad);
        if(request.ok):
            r_dict=request.json()
            generadorPokemon=listadoGneral(r_dict["pokemon"])
            for pokemon in generadorPokemon:
                pokemon1=pokemn(pokemon)
                listado_Pokemones.append(pokemon1)
        else:
            print("[La habilidad que ha ingresado no existe]")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")
    return listado_Pokemones

def pokemn(pokemon1):
    habilidadesList=[]
    r_pok=requests.get(pokemon1);
    if(r_pok.ok):
        r_pok_dict=r_pok.json()
        habilidades=r_pok_dict["abilities"]
        for habilidad in habilidades:
            habilidadesList.append(habilidad["ability"]["name"])
            
        pokemonsCon=Pokemon(r_pok_dict["name"],habilidadesList,r_pok_dict["sprites"]["front_default"])
        #habilidadesList.append(pokemonsCon)
        return pokemonsCon

def listar(libros_data):
    # create header
    head = ["Nombre Pokemon", "Url Image", "Habilidades"]
    data = []
    for libro in libros_data:
        #autores="\n".join(libro.habilidades)
        data.append([libro.name,libro.urlImg,str(libro.habilidades)])

    # # display table
    print(tabulate(data, headers=head, tablefmt="grid"))
listarHabilidad()





# FUNCIONES DE UTILIDAD - RAISA
#    FUNCION LISTAR POKEMON: COLUMNA: NOMBRE - CREAR FUNCION 1
#                            COLUMNA: LISTAR HABILIDADES(2) -  
# 							  COLUMNA: URL DE LA IMAGEN DEL POKE - CREAR FUNCION
#                            URL DE LA IMAGEN("front_default":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/NUMERO_DE_POKEMON.png")