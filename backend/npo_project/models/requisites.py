from django.db import models


class Requisites(models.Model):
    """Реквизиты организации"""

    text = models.TextField(
        'реквизиты организации',
        blank=False,
        unique=True,
        help_text='Укажите/отредактируйте реквизиты организации')

    class Meta:
        verbose_name = 'реквизиты'
        verbose_name_plural = 'реквизиты организации'
        db_table = 'requisites'

    def __str__(self):
        return self.text
