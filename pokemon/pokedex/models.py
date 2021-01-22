from django.db import models

# Create your models here.
class PokemonSpecies(models.Model):
    name = models.CharField(max_length=200)
    evolution_level = models.DateTimeField('date published')
    next_evolution =
    pokemon_types =

class PokemonTypes(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Pokemons(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)