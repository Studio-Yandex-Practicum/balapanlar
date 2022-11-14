from django.db import models


class Principles(models.Model):
    """Наши принципы"""

    text = models.TextField(
        'описание принципа',
        blank=False,
        unique=True,
        help_text='Укажите принцип, который будет '
                  'отражен на сайте')

    image = models.ImageField(
        'картинка к принципу',
        blank=False,
        upload_to='principles_img/',
        help_text='Загрузите картинку, которая будет '
                  'над Вашим принципом на сайте')

    class Meta:
        verbose_name = 'принцип'
        verbose_name_plural = 'наши принципы'
        db_table = 'principles'

    def __str__(self):
        return self.text
