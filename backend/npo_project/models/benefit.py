from django.db import models
from django.utils.translation import gettext_lazy as _

from balapanlar.settings import TEXT_CUT_VALUE


class Benefit(models.Model):
    """Model Benefit, site section 'Why is it good for parents?'."""
    class RoleChoices(models.TextChoices):
        CHILD = 'CHILD', _('ребенку')
        PARENT = 'PARENT', _('родителям')

    text = models.TextField(
        'причина',
        help_text='Например, "Участие в конкурсах и олимпиадах" или '
                  '"Для вашего ребёнка у нас всегда есть чай, вода и снэки"'
    )
    beneficial_to = models.CharField(
        'кому понравится',
        choices=RoleChoices.choices,
        max_length=10,
        help_text='Выберите раздел: "Почему вашему ребёнку понравится у нас?"'
                  ' или "Почему это удобно родителям?"'
    )
    image = models.ImageField(
        'фотография',
        upload_to='benefits/',
        help_text='Можете добавить фотографию',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'причина выбора курсов родителями / детьми'
        verbose_name_plural = 'причины выбора курсов родителями / детьми'
        db_table = 'benefit'

    def __str__(self):
        role = getattr(self.RoleChoices, self.beneficial_to).label
        return f'{role.capitalize()}: {self.text[:TEXT_CUT_VALUE]}...'
