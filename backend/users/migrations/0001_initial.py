# Generated by Django 3.2.16 on 2022-10-28 10:47

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Уникальный идентификатор пользователя.', primary_key=True, serialize=False, verbose_name='UUID Пользователя')),
                ('email', models.EmailField(help_text='Электронная почта пользователя.', max_length=255, unique=True, verbose_name='Электронная почта')),
                ('password', models.CharField(help_text='Пароль пользователя длиной не менее 8 символов и не более 128.', max_length=128, verbose_name='Пароль')),
                ('first_name', models.CharField(help_text='Имя пользователя длиной не более 128 символов. Может содержать заглавные и строчные буквы русского и английского алфавитов и символ "-".', max_length=128, validators=[django.core.validators.RegexValidator(code='Неверное значение', message='В поле Имя можно вводить только русские или английские буквы и "-".', regex='^[а-яА-ЯёЁa-zA-Z][а-яА-ЯёЁa-zA-Z -]*[а-яА-ЯёЁa-zA-Z]$')], verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Фамилия пользователя длиной не более 128 символов. Может содержать заглавные и строчные буквы русского и английского алфавитов и символ "-".', max_length=128, validators=[django.core.validators.RegexValidator(code='Неверное значение', message='В поле Фамилия можно вводить только русские или английские буквы и "-".', regex='^[а-яА-ЯёЁa-zA-Z][а-яА-ЯёЁa-zA-Z -]*[а-яА-ЯёЁa-zA-Z]$')], verbose_name='Фамилия')),
                ('is_team', models.BooleanField(default=False, help_text='Данное поле указывает на принадлежность пользователя к команде Балапанлар.', verbose_name='Команда Балапанлар')),
                ('is_active', models.BooleanField(default=True, help_text='Данное поле указывает, что аккаунт пользователя "Действующий".', verbose_name='Аккаунт активен')),
                ('is_superuser', models.BooleanField(default=False, help_text='Означает, что этот пользователь имеет полностью все права, без явного назначения этих прав.', verbose_name='Статус суперпользователь')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего посещения')),
                ('groups', models.ManyToManyField(blank=True, help_text='Группы к которым принадлежит пользователь. Юзер получит права для каждой из этих групп.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='Группы')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Специфические права для данного пользователя.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='Права пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'custom_user',
                'ordering': ('email',),
            },
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(fields=('email', 'first_name', 'last_name'), name='unique_email_first_name_and_last_name'),
        ),
    ]
