from django.contrib import admin
from .models import Pokemon
from .models import PokemonEntity
from django.conf import settings
from django.db import models


class PokemonEntityInline(admin.TabularInline):
    model = PokemonEntity



class PokemonAdmin(admin.ModelAdmin):
    inlines = [PokemonEntityInline]
    list_display = ['title', 'image', 'name_en', 'name_ja']


admin.site.register(Pokemon, PokemonAdmin)



admin.site.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ['pokemon', 'latitude', 'longitude', 'appeared_at', 'disappeared_at',
                    'level', 'health', 'strength', 'defence', 'stamina']
