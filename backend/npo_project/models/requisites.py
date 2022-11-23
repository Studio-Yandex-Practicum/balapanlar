from django.db import models


class Requisite(models.Model):
    """Model Requisite, site section 'Requisites'."""
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
        return f'Реквизиты: {self.text[:30]}...'
