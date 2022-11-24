from django.db import models

from balapanlar.settings import TEXT_CUT_VALUE


class Requisite(models.Model):
    """Model Requisite, site section 'Requisites'."""
    text = models.TextField(
        'реквизиты организации',
        blank=False,
        unique=True,
        help_text='Укажите/отредактируйте реквизиты организации')

    class Meta:
        verbose_name = 'реквизит организации'
        verbose_name_plural = 'реквизиты организации'
        db_table = 'requisites'

    def __str__(self):
        return f'Реквизиты: {self.text[:TEXT_CUT_VALUE]}...'
