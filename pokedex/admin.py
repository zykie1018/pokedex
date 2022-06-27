from django.contrib import admin
from pokedex.models import Pokemon, PokemonStats


class PokemonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "names",
        "weight",
        "height",
    ]
    search_fields = ["names"]


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonStats)
