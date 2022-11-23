from django.db import models


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

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.adress
