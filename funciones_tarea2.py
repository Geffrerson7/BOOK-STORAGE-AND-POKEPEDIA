from funciones_utilidades import *
import requests
from Pokemon import *
from tabulate import tabulate
from urllib.parse import parse_qsl


URLHABILIDADES = "https://pokeapi.co/api/v2/ability/"

def listadoPorHabilidad():
    print("********** LISTADO POR HABILIDADES ********")
    creacionMenu(["Ingrese la habilidad", "Ver opciones de habilidades", "Cancelar"])
    op = validarRangoInt(1, 3, "Elija una opción: ")
    if op == 1:
        habilidad = validarLeerStrings(" -Ingrese la habilidad a buscar [id o nombre]: ")
        funcionlimpiar()
        lista = buscarHabilidad(habilidad)
        if lista:  # si no esta vacia
            listar(lista)
        else:
            print("[NO HAY POKEMONES CON ESTA HABILIDAD :c]")
    elif op == 2:
        url = URLHABILIDADES + "?offset=0&limit=10"
        mostrarHabildades(url, 1)


def mostrarHabildades(url, start):
    try:
        funcionlimpiar()
        print("********HABILIDADES EXISTENTES********")
        req = requests.get(url)
        paramentrosIniciales = paramURL(req.url)
        comienzoPagina = int(paramentrosIniciales["offset"]) + 1
        respuestaHabilidades = req.json()
        next = respuestaHabilidades["next"]  # URL DE SGT PAGINA
        count = respuestaHabilidades["count"]
        prev = respuestaHabilidades["previous"]  # URL DE PAGINA ANTERIOR
        pPag=parametrosPag(prev,next,count)
        print("[Existen",count,"habilidades. Actualmente mostrando de",comienzoPagina,"a",pPag["ultimoElemento"] - 1,"]")
        creacionMenu(listarHablidades(respuestaHabilidades["results"]), start)
        if pPag["verAnterior"] is not None:
            print("A) VER ANTERIORES")
        if pPag["verMas"] is not None:
            print("B) VER MÁS")
        
        op = validarRangoConString(1,327,pPag["opciones"]," -Ingrese una opción: ")
        if op == "b":
            mostrarHabildades(next, pPag["ultimoElemento"])
        elif op == "a":
            mostrarHabildades(prev, pPag["elementoAnterior"])
        else:
            if(op>267):
                op=9734+op-1
            lista = buscarHabilidad(str(op))
            if lista:  # si no esta vacia
                listar(lista)
            else:
                print("[NO HAY POKEMONES CON ESA HABILIDAD]")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")

def parametrosPag(prev,next,count):
    parametrosNecesarios={"ultimoElemento":count+1,"verMas":None,"verAnterior":None,"elementoAnterior":1,"opciones":[]}
    if next is not None:
        parametrosSiguientes = paramURL(next)
        ultimoElemento = int(parametrosSiguientes["offset"]) + 1
        parametrosNecesarios["ultimoElemento"]=ultimoElemento
        parametrosNecesarios["verMas"]=True
        parametrosNecesarios["opciones"].append("b")
    if prev is not None:
        parametroAnteriores = paramURL(prev)
        primerElemento=int(parametroAnteriores["offset"]) + 1
        parametrosNecesarios["elementoAnterior"]=primerElemento
        parametrosNecesarios["verAnterior"]=True
        parametrosNecesarios["opciones"].append("a")
    return parametrosNecesarios

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
            print("HABILIDAD:",rpta["name"].upper())
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
    

