# Generated by Django 2.2.28 on 2022-10-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название партнера')),
                ('text', models.TextField(unique=True, verbose_name='Описание про партнера')),
                ('url', models.URLField(verbose_name='Ссылка на сайт партнера')),
            ],
            options={
                'verbose_name': 'Наши партнеры',
                'verbose_name_plural': 'Наши партнеры',
            },
        ),
        migrations.CreateModel(
            name='Principles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, unique=True, verbose_name='Описание принципа')),
                ('comment', models.TextField(unique=True, verbose_name='Комментарий к принципу')),
            ],
            options={
                'verbose_name': 'Наши принципы',
                'verbose_name_plural': 'Наши принципы',
            },
        ),
        migrations.AddConstraint(
            model_name='partners',
            constraint=models.UniqueConstraint(fields=('name', 'url'), name='unique_partners'),
        ),
    ]
