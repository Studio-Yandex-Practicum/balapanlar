from django.db import models

from balapanlar.settings import TEXT_CUT_VALUE


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
        help_text='Укажите дополнительную информацию о том как найти центр. '
                  'Пример заполнения: ТЦ «Каскад», 2 этаж'
    )
    full_address = models.CharField(
        'полный адрес',
        blank=True,
        max_length=256,
        help_text='Полный адрес для отоброжения на сайте. '
                  'Автогенерируется на основе введенных ранее данных.'
    )

    class Meta:
        db_table = 'location'
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return f'{self.full_address[:TEXT_CUT_VALUE]}...'

    def save(self, *args, **kwargs):
        full_address = self.address_for_center + ': ' + self.address
        if self.additional_info:
            full_address += ', ' + self.additional_info
        self.full_address = full_address
        super().save(*args, **kwargs)
