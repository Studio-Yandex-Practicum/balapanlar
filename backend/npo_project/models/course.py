'''
This file contents the Course model and all models related to it:
CourseCategory, CourseTag.
'''

from django.db import models


class CourseCategory(models.Model):
    """Model CourseCategory, site section 'Our Courses'."""
    name = models.CharField(
        'название категории', max_length=100, unique=True,
        help_text='Например, "Программирование" или "Иностранные языки"'
    )
    description = models.TextField(
        'описание категории', blank=True,
        help_text='Например, "Наши курсы программирования созданы '
                  'в международной школе «Алгоритмика»..."'
    )

    class Meta:
        verbose_name = 'категория курса'
        verbose_name_plural = 'категории курсов'
        db_table = 'course_category'

    def __str__(self):
        return f'Категория курса: {self.name[:30]}...'


class CourseTag(models.Model):
    """Model CourseTag, site section 'Our Courses'."""
    name = models.CharField(
        'текст тэга', max_length=100, unique=True,
        help_text='Например, "язык Python" или "изучение культуры"'
    )

    class Meta:
        verbose_name = 'тэг курса'
        verbose_name_plural = 'тэги курсов'
        db_table = 'course_tag'

    def __str__(self):
        return f'Тэг курса: {self.name[:30]}...'


class Course(models.Model):
    """Model Course, site section 'Our Courses'."""
    name = models.CharField(
        'название', max_length=100, unique=True,
        help_text='Например, "Python Start"'
    )
    category = models.ForeignKey(
        CourseCategory, related_name='courses',
        verbose_name='категория курса',
        max_length=50, blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text='(необязательное поле) Выберите категорию из списка (либо '
                  'оставьте прочерк) или добавьте новую с помощью зелёного '
                  'плюсика.'
    )
    age_groups = models.CharField(
        'возрастной диапазон', max_length=50,
        help_text='Например, "группы 8+ лет"'
    )
    duration = models.CharField(
        'временной формат курса', max_length=100,
        help_text='Например, "блоки по 3 месяца" или "1 год, блоками по '
                  '3 месяца"'
    )
    description = models.TextField(
        'описание',
        help_text='Например, "Студенты к концу курса будут сами '
                  'создавать приложения."'
    )
    tags = models.ManyToManyField(
        CourseTag, related_name='course',
        verbose_name='тэги курса',
        help_text='Выберите уже имеющиеся варианты или добавьте новый '
                  'с помощью зелёного плюсика.'
    )
    skills = models.TextField(
        'какие умения даст курс', blank=True,
        help_text='(необязательное поле) По желанию напишите список умений, '
                  'которые учащиеся приобретут по окончании курса.',
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        db_table = 'course'

    def __str__(self):
        return f'Курс: {self.name[:30]}...'
