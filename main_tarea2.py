from funciones_utilidades import *
import requests
from Pokemon import *
from tabulate import tabulate
from urllib.parse import parse_qsl

# OPCION 3: LISTAR POR HABLIDAD - RAISA
# 		A. INGRESE LA HABILIDAD
#        B. VER OPCIONES DE HABILIDADES - > FUNCION PANEL: DEL 1 - 327
# 											   FUNCION GENERADORA PARA MOSTRAR OPCIONES DE 10 EN 10
URLHABILIDADES = "https://pokeapi.co/api/v2/ability/"


def listarHabilidad():
    print("********** LISTADO POR HABILIDADES ********")
    creacionMenu(["Ingrese la habilidad", "Ver opciones de habilidades", "Cancelar"])
    op = validarRangoInt(1, 3, "Elija una opción: ")
    if op == 1:
        habilidad = validarLeerStrings(" -Ingrese la habildad a buscar: ")
        lista = buscarHabilidad(habilidad)
        if lista:  # si no esta vacia
            listar(lista)
    elif op == 2:
        url = URLHABILIDADES + "?offset=0&limit=10"
        mostrarHabildades(url, 1)


def mostrarHabildades(url, start):
    try:
        print("********HABILIDADES EXISTENTES********")
        req = requests.get(url)
        paramentrosIniciales = paramURL(req.url)
        comienzoPagina = int(paramentrosIniciales["offset"]) + 1
        respuestaHabilidades = req.json()
        next = respuestaHabilidades["next"]  # URL DE SGT PAGINA
        count = respuestaHabilidades["count"]
        parametrosSiguientes = paramURL(next)
        ultimoElemento = int(parametrosSiguientes["offset"]) + 1
        antesUltimo = ultimoElemento
        print("[Existen",count,"habilidades. Actualmente mostrando de",comienzoPagina,"a",ultimoElemento - 1,"]")
        prev = respuestaHabilidades["previous"]  # URL DE PAGINA ANTERIOR
        creacionMenu(listarHablidades(respuestaHabilidades["results"]), start)
        if prev is not None:
            param = paramURL(prev)
            print(str(antesUltimo) + ") VER ANTERIORES")
            ultimoElemento += 1
        if next is not None:
            print(str(ultimoElemento) + ") VER MÁS")
        op = validarLeerInt(" -Ingrese una opción: ")
        if op == ultimoElemento:
            mostrarHabildades(next, ultimoElemento)
        elif op == antesUltimo:
            mostrarHabildades(prev, int(param["offset"]) + 1)
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")


def paramURL(url):
    if "?" in url:
        _, params = url.split("?", maxsplit=1)
        query = dict(parse_qsl(params))
        return query


def listarHablidades(listaH):
    lista = []
    for item in listaH:
        lista.append(item["name"])
    return lista


def urlPokemon(diccionario: dict):
    for pokemon in diccionario:
        yield pokemon["pokemon"]["url"]


def buscarHabilidad(habilidad):
    listado_Pokemones = []
    try:
        request = requests.get(URLHABILIDADES + habilidad)
        if request.ok:
            rpta = request.json()
            generadorUrlPokemon = urlPokemon(rpta["pokemon"])
            for url in generadorUrlPokemon:
                pokemonCreado = crearPokemon(url)
                if pokemonCreado is not None:
                    listado_Pokemones.append(pokemonCreado)
                else:
                    print("[ERROR EN LA CREACIÓN DEL POKEMON]")
                    break
        else:
            print("[La habilidad que ha ingresado no existe]")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")
    return listado_Pokemones


def crearPokemon(url):
    habilidadesList = []
    try:
        r_pok = requests.get(url)
        if r_pok.ok:
            respuestaPokemon = r_pok.json()
            habilidades = respuestaPokemon["abilities"]
            for habilidad in habilidades:
                habilidadesList.append(habilidad["ability"]["name"])
            pokemonCreado = Pokemon(
                respuestaPokemon["name"],
                habilidadesList,
                respuestaPokemon["sprites"]["front_default"],
            )
            return pokemonCreado
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")
        return None


def listar(lista_pokemones):
    # create header
    head = ["Nombre Pokemon", "Url Image", "Habilidades"]
    data = []
    for poke in lista_pokemones:
        # autores="\n".join(libro.habilidades)
        data.append([poke.name, poke.urlImg, str(poke.habilidades)])
    # # display table
    print(tabulate(data, headers=head, tablefmt="grid"))


listarHabilidad()
# FUNCIONES DE UTILIDAD - RAISA
#    FUNCION LISTAR POKEMON: COLUMNA: NOMBRE - CREAR FUNCION 1
#                            COLUMNA: LISTAR HABILIDADES(2) -
# 							  COLUMNA: URL DE LA IMAGEN DEL POKE - CREAR FUNCION
#                            URL DE LA IMAGEN("front_default":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/NUMERO_DE_POKEMON.png")
