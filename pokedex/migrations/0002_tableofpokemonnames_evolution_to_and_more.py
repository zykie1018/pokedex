# Generated by Django 4.0.5 on 2022-06-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableofpokemonnames',
            name='evolution_to',
            field=models.ManyToManyField(blank=True, to='pokedex.tableofpokemonnames'),
        ),
        migrations.AddField(
            model_name='tableofpokemonnames',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tableofpokemonnames',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
