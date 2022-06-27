from unittest import result
import requests
import json

from django.core.management.base import BaseCommand, CommandError
from pokedex.models import Pokemon

# 1. Create management command to store pokemons
# 2. Create view(db access)
class Command(BaseCommand):
    help = "Update Db with https://pokeapi.co/api/v2/pokemon/"


    def handle(self, *args, **kwargs):
        payload = {"limit": 151}
        get_api = requests.get("https://pokeapi.co/api/v2/pokemon/", params=payload)
        response = get_api.json()
        # pages = get_api.pages
        list_pokemons = []

        # for page in pages:
        #     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/?page={page+1}")

        for pokemon in response.pokemon_list:
            new_pokemon = Pokemon(name=pokemon["name"])

            new_pokemon.save()
        self.stdout.write(self.style.SUCCESS(response.get("results")))

    # def view_index():
    #     pass

    # def view(request):
    #     # pokemon_list = Pokemon.objects.all()

    #     response = requests.get("")

    #     for pokemon in response.pokemon_list:
    #         pass
