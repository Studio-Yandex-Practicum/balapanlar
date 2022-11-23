from django.db import models


class Program(models.Model):
    """Model Program, site section 'About Us'."""
    name = models.CharField(
        'название программы', max_length=100,
        help_text='Например, "Досуговый центр «Уя»"'
    )
    image = models.ImageField(
        'картинка-фон для названия программы', upload_to='programs_img/'
    )
    description = models.TextField(
        'описание',
        help_text='Например, "— это место для общения, '
                  'учёбы, встреч и досуга аульских детей..."'
    )
    location = models.CharField(
        'место проведения', max_length=100,
        help_text='Например, "Аул Икон-Халк, Карачаево-Черкессия"'
    )
    characteristics = models.ManyToManyField(
        'ProgramCharacteristic', related_name='program',
        verbose_name='характеристики занятий на программе',
        help_text='Выберите уже имеющиеся или добавьте новую характеристику '
                  'с помощью зелёного плюсика.'
    )

    class Meta:
        verbose_name = 'программа'
        verbose_name_plural = 'программы'
        db_table = 'program'

    def __str__(self):
        return f'{self.name[:30]}...'


class ProgramCharacteristic(models.Model):
    """Model ProgramCharacteristic, site section 'About Us'."""
    text = models.CharField(
        'текст характеристики', max_length=100,
        help_text='Например, "Занятия весь год" или "Занятия в каникулы"'
    )

    class Meta:
        verbose_name = 'характеристика программы'
        verbose_name_plural = 'характеристики программы'
        db_table = 'program_сharacteristic'

    def __str__(self):
        return f'{self.text[:30]}...'
