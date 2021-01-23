from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_DEFAULT, SET_NULL


# Create your models here.
class PokemonTypes(models.Model):
    pokemon_type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.pokemon_type
    class Meta:
        verbose_name_plural = "Pokemon Types"

class PokemonSpecies(models.Model):
    name = models.CharField(max_length=20)
    evolution_level = models.PositiveIntegerField(
        null=True, blank=True,
        validators=[
            MinValueValidator(
                0,
                message="Please enter up to 100. Leave blank if not applicable."
            ),
            MaxValueValidator(
                100,
                message="Please enter up to 100. Leave blank if not applicable."
            )
        ]
    ) 
    next_evolution = models.ForeignKey('self', blank=True, null=True, on_delete=SET_NULL)
    pokemon_type = models.ForeignKey(PokemonTypes, verbose_name="Type(s)", default=1, on_delete=SET_DEFAULT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pokemon Species"


class Pokemons(models.Model):
    nickname = models.CharField(max_length=20)
    species = models.ForeignKey(PokemonSpecies, verbose_name="Pokemon Species", null=True, on_delete=SET_NULL)
    class Meta:
        verbose_name_plural = "Pokemons"
    level = models.PositiveIntegerField(
        default=5,
        validators=[
            MinValueValidator(
                0,
                message="Please enter up to 100. Leave blank if not applicable."
            ),
            MaxValueValidator(
                100,
                message="Please enter up to 100. Leave blank if not applicable."
            )
        ]
    )
        
    pokemon_type = 'hello'
    trainer = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nickname