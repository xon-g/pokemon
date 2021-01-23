from django.contrib import admin
from .models import PokemonSpecies, PokemonTypes, Pokemons

# Register your models here.
admin.site.register(PokemonSpecies)
admin.site.register(PokemonTypes)
admin.site.register(Pokemons)