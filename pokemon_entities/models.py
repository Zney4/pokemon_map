from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название покемона рус.')
    image = models.ImageField(upload_to='pokemon_entities/',
                                      blank=True,
                                      null=True)
    title_en = models.CharField(blank=True, max_length=200, verbose_name='название покемона англ.')
    title_jp = models.CharField(blank=True, max_length=200, verbose_name='название покемона япон.')
    description = models.TextField(blank=True, verbose_name='Описание покемона')

    previous_evolution = models.ForeignKey('self', null=True, blank=True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions',
                                           verbose_name='Эволюция покемона'
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
    latitude = models.FloatField('Широта', null=True, blank=True)
    longitude = models.FloatField('Долгота', null=True, blank=True)

    appeared_at = models.DateTimeField('Появится', null=True, blank=True)
    disappeared_at = models.DateTimeField('Исчезнит', null=True, blank=True)

    level = models.FloatField(null=True, blank=True, verbose_name='Уровень покемона')
    health = models.FloatField(null=True, blank=True, verbose_name='Здоровье покемона')
    strength = models.FloatField(null=True, blank=True, verbose_name='Сила покемона')
    defence = models.FloatField(null=True, blank=True, verbose_name='Защита покемона')
    stamina = models.FloatField(null=True, blank=True, verbose_name='Выносливость покемона')

    def __str__(self):
        return f"{self.pokemon}: {self.latitude}, {self.longitude}, {self.appeared_at}, {self.disappeared_at}"
