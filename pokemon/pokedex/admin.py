from django.contrib import admin
from .models import PokemonSpecies, PokemonTypes, Pokemons

# Register your models here.
admin.site.site_header = "Pokemon Django Admin"

class PokemonSpeciesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'pokemon_type', 
        'evolution_level', 'next_evolution', 
    )



class PokemonsAdmin(admin.ModelAdmin):
    list_display = (
        'nickname', 'species', 'pokemon_type',
        'level', 'trainer'
    )

admin.site.register(PokemonSpecies, PokemonSpeciesAdmin)
admin.site.register(PokemonTypes)
admin.site.register(Pokemons, PokemonsAdmin)