from django.db import models

from balapanlar.settings import TEXT_CUT_VALUE


class Location(models.Model):
    """Model Location, site section 'How to find us?'."""
    address = models.TextField(
        'адрес',
        max_length=100,
        help_text='Укажите текущий адрес для отображения на сайте. '
                  'Например: Адрес «УЯ»: аул Икон-Халк, ул. Ленина 175, '
                  'ТЦ «Каскад», 2 этаж'
    )

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return f'Адрес: {self.address[:TEXT_CUT_VALUE]}...'
