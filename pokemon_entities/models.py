from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_entities/',
                                      blank=True,
                                      null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Тип покемона',
        related_name='entities',
    )
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')


    appeared_at = models.DateTimeField('Появится')
    disappeared_at = models.DateTimeField('Исчезнит')


    level = models.FloatField(null=True, blank=True)
    health = models.FloatField(null=True, blank=True)
    strength = models.FloatField(null=True, blank=True)
    defence = models.FloatField(null=True, blank=True)
    stamina = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon}: {self.latitude}, {self.longitude}, {self.appeared_at}, {self.disappeared_at}"
