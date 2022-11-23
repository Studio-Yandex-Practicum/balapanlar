from django.db import models


class Location(models.Model):
    """Model Location, site section 'How to find us?'."""
    address = models.TextField(
        'адрес',
        max_length=100,
        help_text='Укажите текущий адрес для отображения на сайте'
    )
    image = models.ImageField(
        'карта',
        blank=False,
        upload_to='location_img/',
        help_text='Тут можно вставить карту (скриншот например)'
    )

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return f'Адрес: {self.address[:30]}...'
