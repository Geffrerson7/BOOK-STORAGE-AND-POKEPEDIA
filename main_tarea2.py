"""BIENVENIDO A LA POKEPEDIA"""

import requests

def get_data_endpoint(url: str, key: str):
    resp = requests.get(url)
    data = resp.json()
    results = data[key]
    return results
url_pokemon_habit = 'https://pokeapi.co/api/v2/pokemon-habitat/'
def get_opciones_habits():
    results = get_data_endpoint(url_pokemon_habit,'results')
    habits =[]
    for result in results:
        habits.append(result['name'])
    return habits
def get_pokemones_por_habita():
    opcion = input("Ingrese una opción en números: ")
    endpoint = url_pokemon_habit+opcion
    result = get_data_endpoint(endpoint,"pokemon_species")
    return result
        

print(get_pokemones_por_habita())

