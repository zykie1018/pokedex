import requests


def pokemon_names_list():
    payload = {"limit": 151}
    list_pokemons = []
    response = requests.get("https://pokeapi.co/api/v2/pokemon/", params=payload)
    pokemons = response.json()
    for line in pokemons["results"]:
        list_pokemons.append(line["name"])
    return list_pokemons
