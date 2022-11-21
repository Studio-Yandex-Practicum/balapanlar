from django.db import models


class TeamMember(models.Model):
    """Участники команды, раздел 'Команда'"""
    name = models.CharField(
        'Имя участника команды',
        help_text='Введите имя, которое будет отображаться на сайте',
        max_length=100,
        unique=True
    )
    role = models.CharField(
        'Роль в команде',
        max_length=100,
        help_text='Например, "администратор" или "куратор".'
    )
    image = models.ImageField('Фотография', upload_to='team_members/')

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'
        db_table = 'team_member'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.role}'
