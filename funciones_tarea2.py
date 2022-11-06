from funciones_utilidades import *
import requests, json
from Pokemon import *
from tabulate import tabulate
from urllib.parse import parse_qsl


URLHABILIDADES = "https://pokeapi.co/api/v2/ability/"
URLGENERACIONES = "https://pokeapi.co/api/v2/generation/"
URLFORMAS = "https://pokeapi.co/api/v2/pokemon-shape/"
URLPOKEMON = "https://pokeapi.co/api/v2/pokemon/"

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
        creacionMenu(listarOpciones(respuestaHabilidades["results"]), start)
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


def listarOpciones(listaH):
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

def listar_de_a_diez(data):  # listar_10_pokes
    '''Imprime los pokemons y sus datos de diez en diez'''
    head = [
        "Nombre",
        "Habilidades",
        "Url Image",
    ]

    
    i = 0
    while i <= len(data) - 10:

        print(tabulate(data[i : i + 10], headers=head, tablefmt="grid"))
        r = validarLeerStrings(
            "¿Desea continuar buscando?Presione la tecla s si su respuesta es si, de lo contrario presione otra tecla: "
        ).lower()
        if i == (len(data) - 10) - len(data) % 10:

            print(
                tabulate(
                    data[len(data) - (len(data)) % 10 :], headers=head, tablefmt="grid"
                )
            )
        if r == "s":
            i += 10
            continue
        else:
            break

def buscarGeneracion(generacion:int) -> None:
    """Imprime los datos de los pokemons de la generacion a buscar"""
    listado_Pokemones = []
    try:
        url_gen = URLGENERACIONES + str(generacion) + "/"
        peticion1 = requests.get(url_gen)
        if peticion1.ok:

            respuesta1 = json.loads(peticion1.content)
            for gen in respuesta1["pokemon_species"]:

                nombre_pokemon = gen["name"]
                url_poke = URLPOKEMON + nombre_pokemon + "/"

                res_pok = requests.get(url_poke)
                if res_pok.ok:
                    respuestaPokemon = json.loads(res_pok.content)
                    habilidadesList = []

                    for pokemon in respuestaPokemon["abilities"]:
                        habilidadesList.append(pokemon["ability"]["name"])
                    habilidades = "\n".join(habilidadesList)
                    listado_Pokemones.append(
                        [
                            respuestaPokemon["name"],
                            habilidades,
                            respuestaPokemon["sprites"]["front_default"],
                        ]
                    )
                else:
                    print("[ERROR EN LA CREACIÓN DEL POKEMON]")

        else:
            print("[La generacion que ha ingresado no existe]")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")
    listar_de_a_diez(listado_Pokemones)

def listarGeneracion() -> None:
    """Imprime los datos de los pokemons de una genracion"""
    while True:

        print("***** LISTAR POR GENERACION *******")
        creacionMenu(
            [
                "Listar la Generación 1",
                "Listar la Generación 2",
                "Listar la Generación 3",
                "Listar la Generación 4",
                "Listar la Generación 5",
                "Listar la Generación 6",
                "Listar la Generación 7",
                "Listar la Generación 8",
                "Salir al Menú",
            ]
        )
        gen = validarRangoInt(1, 9, "Ingrese el numero de generacion a listar: ")
        if gen == 1:
            buscarGeneracion(1)
        elif gen == 2:
            buscarGeneracion(2)
        elif gen == 3:
            buscarGeneracion(3)
        elif gen == 4:
            buscarGeneracion(4)
        elif gen == 5:
            buscarGeneracion(5)
        elif gen == 6:
            buscarGeneracion(6)
        elif gen == 7:
            buscarGeneracion(7)
        elif gen == 8:
            buscarGeneracion(8)
        else:
            break
    
def buscarForma(url_forma:str) -> list[str]:
    """Retorna la lista de pokemons según la lista ingresada"""
    listado_Pokemones = []
    try:
        
        peticion1 = requests.get(url_forma)
        if peticion1.ok:

            respuesta1 = json.loads(peticion1.content)

            for forma_poke in respuesta1["pokemon_species"]:

                nombre_pokemon = forma_poke["name"]
                url_poke = URLPOKEMON + nombre_pokemon + "/"
                try: 
                    res_pok = requests.get(url_poke)
                    if res_pok.ok:
                        respuestaPokemon = json.loads(res_pok.content)
                        habilidadesList = []

                        for pokemon in respuestaPokemon["abilities"]:
                            habilidadesList.append(pokemon["ability"]["name"])
                        habilidades = "\n".join(habilidadesList)
                        listado_Pokemones.append(
                            [
                                respuestaPokemon["name"],
                                habilidades,
                                respuestaPokemon["sprites"]["front_default"],
                            ]
                        )
                    else:
                        print("[ERROR EN LA BÚSQUEDA DEL POKEMON]")
                except:
                    print("[ERROR DE CONEXIÓN CON EL API]")
        else:
            print("[ERROR EN LA BUSQUEDA DE LA FORMA")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")
    return listado_Pokemones


def validarForma(forma:str) -> str:
    """Valida si la forma ingresada por el pokemon"""
    try:
        
        peticion1 = requests.get(URLFORMAS)
        if peticion1.ok:

            respuesta1 = json.loads(peticion1.content)
            for form in respuesta1["results"]:
                
                if form["name"] == forma:
                    url_form = form["url"]
                    return url_form

                else:
                    print("[La forma ingresada no existe]")
                    return None

        else:
            print("[ERROR EN LA BUSQUEDA DE LA FORMA")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")


def mostrarForma(url_formas:str) -> None:
    """Imprime las 14 formas de pokemons que existen"""
    try:

        peticion1 = requests.get(url_formas)
        if peticion1.ok:

            respuesta1 = json.loads(peticion1.content)
            creacionMenu(listarOpciones(respuesta1["results"]), 1)
            
        else:
            print("[La forma que ha ingresado no existe]")
    except:
        print("[ERROR DE CONEXIÓN CON EL API]")


def listarForma():
    """Imprime la los datos de los pokemons según su forma"""
    print("********** LISTADO POR FORMAS ********")
    creacionMenu(["Ingrese la forma", "Ver opciones de formas", "Cancelar"])
    op = validarRangoInt(1, 3, "Elija una opción: ")
    if op == 1:
        forma = validarLeerStrings(" -Ingrese la forma a buscar: ")
        funcionlimpiar()
        url_forma = validarForma(forma)
        if url_forma is not None:  
            listar_de_a_diez(buscarForma(url_forma))
        else:
            print("[NO HAY POKEMONES CON ESTA FORMA :c]")
    elif op == 2:
        mostrarForma(URLFORMAS)
