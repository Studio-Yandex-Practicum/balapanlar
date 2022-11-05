# Балапанлар

## О проекте
НКО "Балапанлар" (Карачаево-Черкессия) - классный образовательный проект, где детям, которые часто ничего, кроме своего аула, не видели, покажут другой мир. Здесь обучат кодингу, 4 иностранным языкам, познакомят с путешественниками, расскажут об устойчивом развитии и вовлекут в неформальное образование.

## Запуск проекта

<details><summary>Локальный запуск Django проекта:</summary>
<p>

1. Клонировать репозиторий:
```bash
git clone https://github.com/Studio-Yandex-Practicum/balapanlar.git
```

2. Создать виртуальное окружение:
```bash
python3 -m venv venv
```

3. Активировать виртуальное окружение:
```bash
Unix-like systems:
. ./venv/bin/activate

Windows:
venv\Scripts\activate.bat
```

4. Перейти в директорию **backend**, обновить pip и установить зависимости из ```requirements.txt```:
```bash
cd backend/
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Выполнить миграции и создать суперпользователя (для доступа к админ панели):
> При создании суперпользователя следовать инструкциям в терминале.
```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```

6. Запустить проект
```bash
python3 manage.py runserver <port>
```
> При запуске опционально можно указать `port`, если стандартный порт **8000** занят. <br />
> Например: `python3 manage.py runserver 8001`

Проект доступен по адресу: http://127.0.0.1
</p>
</details>


<details><summary>Запуск проекта с помощью Docker:</summary>
<p>

> Для корректного запуска проекта необходимо установить Docker на свою рабочую машину. Инструкцию по установке для вашей ОС можно найти на [оффициальном сайте](https://docs.docker.com/get-docker/).

После установки Docker:

1. Клонировать репозиторий:
```bash
git clone https://github.com/Studio-Yandex-Practicum/balapanlar.git
```

2. Перейти в директорию **infra**, запустить сборку и запуск контейнеров:
```bash
cd infra/
docker-compose -f docker-compose.yaml up
```

Проект доступен по адресу: http://localhost
</p>
</details>


## База данных

Для отката к нужной версии миграции из директории с файлом `manage.py` выполнить команду:

```bash
python3 manage.py migrate <app_name> <previous_migration_number>
```
Подробнее о том как откатить миграции в [документации Django](https://docs.djangoproject.com/en/4.1/topics/migrations/#reversing-migrations).

<span style="color: red;">ВНИМАНИЕ!</span>
При откате миграций юзеров сохранить порядок полей в `fields` и переведнные значения `help_text`, `verbose_name` для полей: **is_superuser, last_login, groups, user_permissions**.


[Ссылка на макет проекта](https://www.figma.com/file/K9ovZvLBB1qs5AzjYoZNWm/Balapanlar-design?node-id=0%3A1).
