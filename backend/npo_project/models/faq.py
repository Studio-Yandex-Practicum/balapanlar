from django.db import models


class FAQ(models.Model):
    """ Часто задаваемые вопросы-FAQ"""

    question = models.TextField(
        verbose_name='Вопрос',
        max_length=100,
        help_text='Впишите часто задаваемый вопрос'
    )
    answer = models.TextField(
        verbose_name='Ответ',
        max_length=1500,
        help_text='Дайте развернутый ответ'
    )

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self):
        return (f'{self.question}, '
                f'{self.answer}')
