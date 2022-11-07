from django.db import models


class Location(models.Model):
    adress = models.TextField(
                            verbose_name='Адрес',
                            max_length=100)
    image = models.ImageField(
                        blank=False,
                        upload_to='location_img/',
                        verbose_name='Карта')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.adress
