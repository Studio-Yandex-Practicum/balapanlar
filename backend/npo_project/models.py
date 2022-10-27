from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class TeamMember(BaseModel):
    name = models.CharField(
        'Имя участника команды',
        help_text='Введите имя, которое будет отображаться на сайте',
        max_length=100,
        unique=True
    )
    role = models.CharField('Роль в команде', max_length=100,)
    image = models.ImageField('Фотография', upload_to='team_members/')

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.role}'


class Benefit(BaseModel):
    class RoleChoices(models.TextChoices):
        CHILD = 'CHILD', _('ребенку')
        PARENT = 'PARENT', _('родятелям')

    text = models.TextField('Причина')
    beneficial_to = models.CharField(
        'Кому понравится', choices=RoleChoices.choices, max_length=10
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

    def __str__(self):
        role = getattr(self.RoleChoices, self.beneficial_to).label
        return f'{role.capitalize()}: {self.text[:50]}'
