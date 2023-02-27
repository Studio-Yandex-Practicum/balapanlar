from django.db import models

from balapanlar.settings import TEXT_CUT_VALUE


class FAQ(models.Model):
    """Model FAQ, site section 'FAQ'."""
    question = models.TextField(
        'вопрос',
        max_length=100,
        help_text='Впишите часто задаваемый вопрос'
    )
    answer = models.TextField(
        'ответ',
        max_length=1500,
        help_text='Дайте развернутый ответ'
    )

    class Meta:
        verbose_name = 'часто задаваемый вопрос'
        verbose_name_plural = 'часто задаваемые вопросы'

    def __str__(self):
        return f'Вопрос: {self.question[:TEXT_CUT_VALUE]}...'
