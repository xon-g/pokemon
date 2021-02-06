from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_DEFAULT, SET_NULL
from django.db.models.fields.related import ForeignKey, ForeignObject


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
    poke_type = models.ManyToManyField(PokemonTypes, verbose_name="Pokemon Type(s)")

    def __str__(self):
        return self.name
    
    def pokemon_type(self):
        type1_id = self.poke_type.first()
        type2_id = self.poke_type.last()
        # return type_
        if type1_id == type2_id:
            return type1_id
        else:
            return f'{type1_id} {type2_id}'

    class Meta:
        verbose_name_plural = "Pokemon Species"

class Pokemons(models.Model):
    nickname = models.CharField(max_length=20)
    species = models.ForeignKey(PokemonSpecies, verbose_name="Pokemon Species", null=True, on_delete=models.SET_NULL)
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
    trainer = models.CharField(max_length=20, null=True)

    # def pokemon_type(self):
    #     poke_name = self.species
    #     poke_id = poke_name.id
    #     poke_type = PokemonTypes.objects.all()
    #     return poke_type

    def pokemon_type(self):
        return PokemonSpecies.objects.get(name=self.species).pokemon_type()
    class Meta:
        verbose_name_plural = "Pokemons"

    def __str__(self):
        return self.nickname