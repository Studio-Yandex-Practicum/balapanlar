# Generated by Django 3.2.16 on 2022-11-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('npo_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='Причина')),
                ('beneficial_to', models.CharField(choices=[('CHILD', 'ребенку'), ('PARENT', 'родителям')], max_length=10, verbose_name='Кому понравится')),
                ('image', models.ImageField(blank=True, help_text='Можете добавить фотографию', null=True, upload_to='benefits/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Причина выбора курсов родителями / детьми',
                'verbose_name_plural': 'Причины выбора курсов родителями / детьми',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100, verbose_name='Вопрос')),
                ('answer', models.TextField(max_length=1500, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопросы',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='IncludedInCoursePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='например, "Снэки, вода, чай на нашей кухне"', max_length=100, verbose_name='что включено в стоимость')),
            ],
            options={
                'verbose_name': 'что входит в стоимость курсов',
                'verbose_name_plural': 'что входит в стоимость курсов',
                'db_table': 'included_in_course_price',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.TextField(max_length=100, verbose_name='Адрес')),
                ('image', models.ImageField(upload_to='location_img/', verbose_name='Карта')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='NotIncludedInCoursePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='например, "Трансфер из вашего аула к центру"', max_length=100, verbose_name='что не включено в стоимость')),
            ],
            options={
                'verbose_name': 'что не входит в стоимость курсов',
                'verbose_name_plural': 'что не входит в стоимость курсов',
                'db_table': 'not_included_in_course_price',
            },
        ),
        migrations.CreateModel(
            name='ProgramCharacteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Например, "Занятия весь год" или "Занятия в каникулы"', max_length=100, verbose_name='текст характеристики')),
            ],
            options={
                'verbose_name': 'характеристика программы',
                'verbose_name_plural': 'характеристики программы',
                'db_table': 'program_сharacteristic',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Введите имя, которое будет отображаться на сайте', max_length=100, unique=True, verbose_name='Имя участника команды')),
                ('role', models.CharField(max_length=100, verbose_name='Роль в команде')),
                ('image', models.ImageField(upload_to='team_members/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Участник команды',
                'verbose_name_plural': 'Участники команды',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например, "Досуговый центр «Уя»"', max_length=100, verbose_name='название программы')),
                ('image', models.ImageField(upload_to='programs_img/', verbose_name='картинка-фон для названия программы')),
                ('description', models.TextField(help_text='Например, "— это место для общения, учёбы, встреч и досуга аульских детей..."', verbose_name='описание')),
                ('location', models.CharField(help_text='Например, "Аул Икон-Халк, Карачаево-Черкессия"', max_length=100, verbose_name='место проведения')),
                ('characteristics', models.ManyToManyField(help_text='Выберите уже имеющиеся или добавьте новую характеристику с помощью зелёного плюсика.', related_name='program', to='npo_project.ProgramCharacteristic', verbose_name='характеристики занятий на программе')),
            ],
            options={
                'verbose_name': 'программа',
                'verbose_name_plural': 'программы',
                'db_table': 'program',
            },
        ),
        migrations.CreateModel(
            name='CoursePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(help_text='Напишите в формате "Стоимость курсов 3500 руб./мес."', max_length=100, verbose_name='стоимость курсов')),
                ('payment_url', models.URLField(verbose_name='ссылка для кнопки "Оплатить курсы"')),
                ('included_in_price', models.ManyToManyField(help_text='Выберите уже имеющиеся варианты или добавьте новый с помощью зелёного плюсика.', related_name='course_price', to='npo_project.IncludedInCoursePrice', verbose_name='включено в стоимость')),
                ('not_included_in_price', models.ManyToManyField(help_text='Выберите уже имеющиеся варианты или добавьте новый с помощью зелёного плюсика.', related_name='course_price', to='npo_project.NotIncludedInCoursePrice', verbose_name='не включено в стоимость')),
            ],
            options={
                'verbose_name': 'стоимость курсов',
                'verbose_name_plural': 'стоимости курсов',
                'db_table': 'course_price',
            },
        ),
    ]
