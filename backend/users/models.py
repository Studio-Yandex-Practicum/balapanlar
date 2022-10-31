import uuid
from collections import namedtuple

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.validators import RegexValidator
from django.db import models

VALID_TEXT = r'^[а-яА-ЯёЁa-zA-Z][а-яА-ЯёЁa-zA-Z -]*[а-яА-ЯёЁa-zA-Z]$'
INVALID_FIELD_MSG = (
    'В поле {} можно вводить только русские или английские буквы и "-".'
)
INVALID_CODE = 'Неверное значение'
IS_TEAM_ERROR_MSG = 'Значение "is_team" для суперпользователь должно быть True'
IS_SUPERUSER_ERROR_MSG = (
    'Значение "is_superuser" для '
    'суперпользователя должно быть True'
)
USER_REQUIRED_FIELDS = namedtuple(
    'Feild', 'email password first_name last_name'
)
RUSSIA_EQUIVALENTS = USER_REQUIRED_FIELDS(
    'Адрес электронной почты', 'Пароль', 'Имя', 'Фамилию'
)


class CustomUserManager(BaseUserManager):
    def _create_user(
        self, email, first_name, last_name, password, **extra_fields
    ):
        fields_values = (email, password, first_name, last_name)
        fields_values_data = dict(
            zip(self.model.REQUIRED_FIELDS, fields_values)
        )

        for field_name, field_value in fields_values_data.items():
            if not field_value:
                invalid_field_value = getattr(RUSSIA_EQUIVALENTS, field_name)
                raise ValueError(
                    f'Необходимо указать "{invalid_field_value}"'
                )
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        extra_fields.setdefault('is_team', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, first_name, last_name, password, **extra_fields
        )

    def create_superuser(
        self, first_name, last_name, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault('is_team', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_team') is not True:
            raise ValueError(
                IS_TEAM_ERROR_MSG
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                IS_SUPERUSER_ERROR_MSG
            )
        return self._create_user(
            email, first_name, last_name, password, **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        'uuid пользователя',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Уникальный идентификатор пользователя.'
    )
    email = models.EmailField(
        'электронная почта',
        max_length=255,
        unique=True,
        help_text='Электронная почта пользователя.'
    )
    password = models.CharField(
        'пароль',
        max_length=128,
        blank=False,
        help_text=(
            'Пароль пользователя длиной не менее 8 символов и не более 128.'
        )
    )
    first_name = models.CharField(
        'имя',
        max_length=128,
        blank=False,
        validators=(
            RegexValidator(
                regex=VALID_TEXT,
                message=INVALID_FIELD_MSG.format('Имя'),
                code=INVALID_CODE
            ),
        ),
        help_text=(
            'Имя пользователя длиной не более 128 символов. Может содержать '
            'заглавные и строчные буквы русского и английского '
            'алфавитов и символ "-".'
        )
    )
    last_name = models.CharField(
        'фамилия',
        max_length=128,
        blank=False,
        validators=(
            RegexValidator(
                regex=VALID_TEXT,
                message=INVALID_FIELD_MSG.format('Фамилия'),
                code=INVALID_CODE
            ),
        ),
        help_text=(
            'Фамилия пользователя длиной не более 128 символов. '
            'Может содержать заглавные и строчные буквы русского '
            'и английского алфавитов и символ "-".'
        )
    )
    is_team = models.BooleanField(
        'команда Балапанлар',
        default=False,
        help_text=(
            'Данное поле указывает на принадлежность пользователя '
            'к команде Балапанлар.'
        )
    )
    is_active = models.BooleanField(
        'аккаунт активен',
        default=True,
        help_text=(
            'Данное поле указывает, что аккаунт пользователя "Действующий".'
        )
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password', 'first_name', 'last_name')

    class Meta:
        db_table = 'custom_user'
        ordering = ('email',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        constraints = (
            models.UniqueConstraint(
                fields=('email', 'first_name', 'last_name'),
                name='unique_email_first_name_and_last_name'
            ),
        )

    def __str__(self):
        """Returns string string representation of user."""
        return (
            f'Пользователь {self.get_full_name()}, '
            f'email: {self.email}'
        )

    def get_full_name(self):
        """Returns full name of user."""
        return f'{self.first_name} {self.last_name}'

    @property
    def is_staff(self):
        """Returns is the user a member of team."""
        return self.is_team
