from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FAQ(models.Model):
    question = models.TextField(
                            verbose_name='Вопрос',
                            max_length=50)
    answer = models.TextField(
                            verbose_name='Ответ',
                            max_length=50)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self):
        return (f'{self.question}, '
                f'{self.answer}')


class Location(models.Model):
    adress = models.TextField(
                            verbose_name='Адрес',
                            max_length=50)
    image = models.ImageField(
                        blank=False,
                        upload_to='location_img/',
                        verbose_name='Карта')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.adress
