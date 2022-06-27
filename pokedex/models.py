from django.db import models


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    names = models.CharField(max_length=100, unique=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"

    def __str__(self):
        return self.names


class PokemonStats(models.Model):
    name = models.CharField(max_length=100)
    effort = models.IntegerField()
    base_stat = models.IntegerField()
    pokemon = models.ForeignKey(
        "pokedex.Pokemon", related_name="stats", on_delete=models.CASCADE
    )


class PokemonTypes(models.Model):
    name = models.CharField(max_length=50)
    pokemon = models.ForeignKey(
        "pokedex.Pokemon", related_name="type", on_delete=models.CASCADE
    )
