# Generated by Django 3.1.5 on 2021-01-23 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_auto_20210123_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonspecies',
            name='pokemon_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='pokedex.pokemontypes', verbose_name='Type(s)'),
        ),
    ]