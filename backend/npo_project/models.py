from django.db import models


class Partners(models.Model):
    """Наши партнеры"""

    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name='Название партнера')

    description = models.TextField(
        blank=False,
        unique=True,
        verbose_name='Краткая информация о партнере')

    image = models.ImageField(
        blank=False,
        upload_to='partners_img/',
        verbose_name='Логотип партнера')

    url = models.URLField(
        blank=False,
        verbose_name='Ссылка на сайт партнера')

    class Meta:
        verbose_name = 'Партнера'
        verbose_name_plural = 'Наши партнеры'
        constraints = [
            models.UniqueConstraint(fields=['name', 'url'],
                                    name='unique_partners')
        ]

    def __str__(self):
        return self.name


class Principles(models.Model):
    """Наши принципы"""

    text = models.TextField(
        blank=False,
        unique=True,
        verbose_name='Описание принципа')

    image = models.ImageField(
        blank=True,
        upload_to='principles_img/',
        verbose_name='Картинка к принципу')

    class Meta:
        verbose_name = 'Принцип'
        verbose_name_plural = 'Наши принципы'

    def __str__(self):
        return self.text


class Requisites(models.Model):
    """Реквизиты организации"""

    text = models.TextField(
        blank=False,
        unique=True,
        verbose_name='Реквизиты организации')

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты организации'

    def __str__(self):
        return self.text
