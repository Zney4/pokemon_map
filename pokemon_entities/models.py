from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_entities/',
                                      blank=True,
                                      null=True)
    title_en = models.CharField(blank=True, max_length=200)
    title_jp = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)

    previous_evolution = models.ForeignKey('self', null=True, blank=True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions'
                                           )

    def __str__(self):
        return self.title_ru

    def get_next_evolutions(self):
        return self.next_evolutions.all()


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
