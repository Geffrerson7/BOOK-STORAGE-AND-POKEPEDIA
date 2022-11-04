"""BIENVENIDO A LA POKEPEDIA"""

import requests

def get_data_endpoint(url: str, key: str):
    resp = requests.get(url)
    data = resp.json()
    results = data[key]
    return results

def leer_opciones_habits():
    url_pokemon_habit = 'https://pokeapi.co/api/v2/pokemon-habitat/'
    results = get_data_endpoint(url_pokemon_habit,'results')
    habits =[]
    for result in results:
        habits.append(result['name'])
    return habits

print(leer_opciones_habits())

def listar_pokemones_por_habits():
     results = leer_opciones_habits()
