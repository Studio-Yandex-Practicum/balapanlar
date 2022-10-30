from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        db_table = 'tags'

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100, unique=True)
    category = models.CharField('Категория', max_length=50)
    age_groups = models.CharField('Возрастной диапозон', max_length=15)
    duration = models.CharField('Длительность курса', max_length=40)
    description = models.TextField('Описание')
    tags = models.ManyToManyField(Tag)
    skills = models.CharField('Какие умения даст курс', max_length=200)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        db_table = 'course'

    def __str__(self):
        return str(self.name)


class Partners(models.Model):
    """Наши партнеры"""

    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name='Название партнера')

    description = models.TextField(
        blank=False,
        unique=True,
        verbose_name='Краткая информация о партнере')

    image = models.ImageField(
        blank=False,
        upload_to='partners_img/',
        verbose_name='Логотип партнера')

    url = models.URLField(
        blank=False,
        verbose_name='Ссылка на сайт партнера')

    class Meta:
        verbose_name = 'Партнера'
        verbose_name_plural = 'Наши партнеры'
        constraints = [
            models.UniqueConstraint(fields=['name', 'url'],
                                    name='unique_partners')
        ]

    def __str__(self):
        return self.name


class Principles(models.Model):
    """Наши принципы"""

    text = models.TextField(
        blank=False,
        unique=True,
        verbose_name='Описание принципа')

    image = models.ImageField(
        blank=True,
        upload_to='principles_img/',
        verbose_name='Картинка к принципу')

    class Meta:
        verbose_name = 'Принцип'
        verbose_name_plural = 'Наши принципы'

    def __str__(self):
        return self.text


class Requisites(models.Model):
    """Реквизиты организации"""

    text = models.TextField(
        blank=False,
        unique=True,
        verbose_name='Реквизиты организации')

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты организации'

    def __str__(self):
        return self.text
>>>>>>> 2c9697604f2753e7fcf9cfbae3504d3c44e1390d
