from django.db import models
from django.utils.translation import gettext_lazy as _


class Benefit(models.Model):
    """
    Описания разделов 'Почему вашему ребёнку понравится у нас?' и
    'Почему это удобно родителям?'
    """
    class RoleChoices(models.TextChoices):
        CHILD = 'CHILD', _('ребенку')
        PARENT = 'PARENT', _('родителям')

    text = models.TextField('Причина')
    beneficial_to = models.CharField(
        'Кому понравится',
        choices=RoleChoices.choices,
        max_length=10,
        help_text='Выберите раздел: "Почему вашему ребёнку понравится у нас?"'
                  ' или "Почему это удобно родителям?"'
    )
    image = models.ImageField(
        'Фотография',
        upload_to='benefits/',
        help_text='Можете добавить фотографию',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Причина выбора курсов родителями / детьми'
        verbose_name_plural = 'Причины выбора курсов родителями / детьми'
        db_table = 'benefit'

    def __str__(self):
        role = getattr(self.RoleChoices, self.beneficial_to).label
        return f'{role.capitalize()}: {self.text[:50]}'
