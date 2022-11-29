from django.db import models

from balapanlar.settings import TEXT_CUT_VALUE


class CoursePrice(models.Model):
    """Model CoursePrice, site section 'Our Courses'."""
    price = models.CharField(
        'стоимость курсов', max_length=100,
        help_text='Напишите в формате "Стоимость курсов 3500 руб./мес."'
    )
    included_in_price = models.ManyToManyField(
        'IncludedInCoursePrice', related_name='course_price',
        verbose_name='включено в стоимость',
        help_text='Выберите уже имеющиеся варианты или добавьте новый '
                  'с помощью зелёного плюсика.'
    )
    not_included_in_price = models.ManyToManyField(
        'NotIncludedInCoursePrice', related_name='course_price',
        verbose_name='не включено в стоимость',
        help_text='Выберите уже имеющиеся варианты или добавьте новый '
                  'с помощью зелёного плюсика.'
    )
    payment_url = models.URLField('ссылка для кнопки "Оплатить курсы"')

    class Meta:
        verbose_name = 'стоимость курсов'
        verbose_name_plural = 'стоимости курсов'
        db_table = 'course_price'

    def __str__(self):
        return f'{self.price[:TEXT_CUT_VALUE]}...'


class IncludedInCoursePrice(models.Model):
    """Model IncludedInCoursePrice, site section 'Our Courses'."""
    text = models.CharField(
        'что включено в стоимость', max_length=100,
        help_text='например, "Снэки, вода, чай на нашей кухне"'
    )

    class Meta:
        verbose_name = 'что входит в стоимость курсов'
        verbose_name_plural = 'что входит в стоимость курсов'
        db_table = 'included_in_course_price'

    def __str__(self):
        return f'{self.text[:TEXT_CUT_VALUE]}...'


class NotIncludedInCoursePrice(models.Model):
    """Model NotIncludedInCoursePrice, site section 'Our Courses'."""
    text = models.CharField(
        'что не включено в стоимость', max_length=100,
        help_text='например, "Трансфер из вашего аула к центру"'
    )

    class Meta:
        verbose_name = 'что не входит в стоимость курсов'
        verbose_name_plural = 'что не входит в стоимость курсов'
        db_table = 'not_included_in_course_price'

    def __str__(self):
        return f'{self.text[:TEXT_CUT_VALUE]}...'
