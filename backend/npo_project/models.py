from django.db import models
import json


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
    skills = models.CharField('Какие умения даст курс',max_length=200)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        db_table = 'course'

    def __str__(self):
        return str(self.name)
