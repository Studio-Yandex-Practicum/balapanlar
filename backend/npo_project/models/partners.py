from django.db import models


class Partners(models.Model):
    """Наши партнеры"""

    name = models.CharField(
        'название партнера',
        max_length=350,
        unique=True,
        blank=False,
        help_text='Укажите наименование партнера')

    description = models.TextField(
        'краткая информация о партнере',
        blank=False,
        unique=True,
        help_text='Опишите информацию о партнере, '
                  'которая будет отражаться на сайте')

    image = models.ImageField(
        'логотип партнера',
        blank=False,
        upload_to='partners_img/',
        help_text='Загрузите логотип партнера')

    url = models.URLField(
        'ссылка на сайт партнера',
        unique=True,
        blank=False,
        help_text='Укажите полную ссылку на сайт партнера, '
                  'в формате - https://lewibo.org/')

    class Meta:
        verbose_name = 'партнера'
        verbose_name_plural = 'наши партнеры'
        db_table = 'partners'
        constraints = [
            models.UniqueConstraint(fields=['name', 'url'],
                                    name='unique_partners')
        ]

    def __str__(self):
        return self.name
