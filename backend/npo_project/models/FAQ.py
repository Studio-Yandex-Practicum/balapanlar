from django.db import models


class FAQ(models.Model):
    question = models.TextField(
                            verbose_name='Вопрос',
                            max_length=100)
    answer = models.TextField(
                            verbose_name='Ответ',
                            max_length=1500)

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self):
        return (f'{self.question}, '
                f'{self.answer}')
