from django.db import models
from django.utils.translation import gettext_lazy as _


class TeamMember(models.Model):
    """Model TeamMember, site section 'Team'."""
    class NameReprChoices(models.TextChoices):
        IOF = 'IOF', _('Сначала имя')
        FIO = 'FIO', _('Сначала фамилия')

    name = models.CharField(
        'имя', help_text='Введите имя участника команды', max_length=100,
    )
    second_name = models.CharField(
        'отчество',
        help_text='Необязательное поле. '
                  'Введите отчество, если его нужно отобразить на странице',
        max_length=100,
        blank=True
    )
    last_name = models.CharField(
        'фамилия',
        help_text='Необязательное поле. '
                  'Введите фамилию, если ее нужно отобразить на странице',
        max_length=100,
        blank=True
    )
    full_name = models.CharField(
        'полное имя',
        help_text='Автогенерируется на основе введенных данных',
        max_length=300,
        blank=True
    )
    name_representation = models.CharField(
        'отображение имени',
        help_text='Поменяйте, если хотите, чтобы фамилия (при наличии) '
                  'отображалась сначала. Или наоборот',
        choices=NameReprChoices.choices,
        default=NameReprChoices.IOF,
        max_length=3
    )
    role = models.CharField(
        'роль в команде',
        max_length=100,
        help_text='Например, "администратор" или "куратор"'
    )
    image = models.ImageField(
        'фотография',
        upload_to='team_members/',
        help_text='Добавьте фотография участника команды'
    )

    class Meta:
        verbose_name = 'участник команды'
        verbose_name_plural = 'участники команды'
        db_table = 'team_member'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        full_name = self.name
        if self.second_name:
            full_name += ' ' + self.second_name
        if self.last_name:
            if self.name_representation == 'IOF':
                full_name += ' ' + self.last_name
            else:
                full_name = self.last_name + ' ' + full_name
        self.full_name = full_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}, {self.role}'
