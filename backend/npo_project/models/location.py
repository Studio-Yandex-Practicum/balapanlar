from django.db import models
from yandex_geocoder import Client


class Location(models.Model):
    """Адрес организации"""

    adress = models.TextField(
        verbose_name='Адрес',
        max_length=100,
        help_text='Впишите текущий адрес'
    )
    image = models.ImageField(
        blank=False,
        upload_to='location_img/',
        verbose_name='Карта',
        help_text='Тут можно вставить карту (скриншот например)'
    )
    latitude = models.FloatField(
        'Широта точки', null=True
    )
    longitude = models.FloatField(
        'Долгота точки', null=True
    )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.adress

    def save(self, *args, **kwargs):
        client = Client('8d85ce6f-3c2a-430c-b9f4-4702060528e9')
        self.longitude, self.latitude = client.coordinates(self.adress)
        super(Location, self).save(*args, **kwargs)
