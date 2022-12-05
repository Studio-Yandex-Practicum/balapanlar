from django.db import models

from balapanlar.settings import TEXT_CUT_VALUE
from .utils import get_coordinates


class Location(models.Model):
    """Model Location, site section 'How to find us?'."""
    center_name = models.CharField(
        'название центра',
        max_length=50,
        blank=False,
        help_text='Пример заполнения данного поля: Адрес «УЯ»'
    )
    address = models.CharField(
        'адрес',
        blank=False,
        max_length=100,
        help_text='Укажите текущий адрес для отображения на сайте. '
                  'Например: аул Икон-Халк, ул. Ленина 175'
    )
    additional_info = models.TextField(
        'дополнительная информация',
        blank=True,
        help_text='Укажите дополнительную информацию, о том как найти центр. '
                  'Пример заполнения: ТЦ «Каскад», 2 этаж'
    )
    full_address = models.CharField(
        'полный адрес',
        blank=True,
        max_length=256,
        help_text='Полный адрес для отображения на сайте. '
                  'Автогенерируется на основе введенных ранее данных.'
    )
    latitude = models.FloatField(
        'Широта точки', null=True
    )
    longitude = models.FloatField(
        'Долгота точки', null=True
    )
    image = models.ImageField(
        'Схема проезда',
        blank=True,
        null=True,
        upload_to='locations/',
        help_text='Можете добавить картинку со схемой, чтобы показать, как '
                  'добраться до указанного адреса',
    )
    schema_description = models.CharField(
        'Описание для схемы проезда',
        max_length=250,
        help_text='Можете добавить краткое описание, как добраться. '
                  'Например: вход через серые ворота справа от аптеки',
        blank=True,
    )

    class Meta:
        db_table = 'location'
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return f'{self.full_address[:TEXT_CUT_VALUE]}...'

    def save(self, *args, **kwargs):
        full_address = self.center_name + ': ' + self.address
        if self.additional_info:
            full_address += ', ' + self.additional_info
        self.full_address = full_address
        self.longitude, self.latitude = get_coordinates(self.address)
        super().save(*args, **kwargs)
