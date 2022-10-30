from enum import Enum

FIRST_NAME = 'Имя'
LAST_NAME = 'Фамилия'


class TestUser1(str, Enum):
    """Fields for creating a user for tests.
    ALl fields are valid.
    """
    EMAIL = 'valid-email@example.com'
    PASSWORD = 'testpassword123'
    FIRST_NAME = 'User'
    LAST_NAME = 'Valid'


class TestUser2(str, Enum):
    """Fields for creating a user for tests.
    ALl fields are valid.
    """
    EMAIL = 'goodemail@example.com'
    PASSWORD = 'veryhardpassword123'
    FIRST_NAME = 'UserValid'
    LAST_NAME = 'Valid-User'


class TestUser3(str, Enum):
    """Fields for creating a user for tests.
    Valid fields: email, password, last_name.
    Invalid field: first_name.
    """
    EMAIL = 'testuser3@gmail.com'
    PASSWORD = 'newStrongPa$$'
    FIRST_NAME = 'InvalidName11!'
    LAST_NAME = 'UserSurname'


class TestUser4(str, Enum):
    """Fields for creating a user for tests.
    Valid fields: email, password, first_name.
    Invalid field: last_name.
    """
    EMAIL = 'testuser3@gmail.com'
    PASSWORD = 'newStrongPa$$'
    FIRST_NAME = 'UserName'
    LAST_NAME = 'InvalidSurname22!'


class TestSuperUser(str, Enum):
    """Fields for creating a superuser for tests.
    All fields are valid.
    """
    EMAIL = 'admin@admin.com'
    PASSWORD = '$trongpa$$word'
    FIRST_NAME = 'admin-super'
    LAST_NAME = 'super-admin'


class CustomUserVerboseNames(str, Enum):
    """Expected verbose names for testing fields of CustomUser."""
    ID = 'UUID Пользователя'
    EMAIL = 'Электронная почта'
    PASSWORD = 'Пароль'
    FIRST_NAME = 'Имя'
    LAST_NAME = 'Фамилия'
    IS_TEAM = 'Команда Балапанлар'
    IS_ACTIVE = 'Аккаунт активен'


class CustomUserHelpTexts(str, Enum):
    """Expected help texts for testing fields of CustomUser."""
    ID = 'Уникальный идентификатор пользователя.'
    EMAIL = 'Электронная почта пользователя.'
    PASSWORD = (
        'Пароль пользователя длиной не менее 8 символов и не более 128.'
    )
    FIRST_NAME = (
        'Имя пользователя длиной не более 128 символов. Может содержать '
        'заглавные и строчные буквы русского и английского '
        'алфавитов и символ "-".'
    )
    LAST_NAME = (
        'Фамилия пользователя длиной не более 128 символов. '
        'Может содержать заглавные и строчные буквы русского '
        'и английского алфавитов и символ "-".'
    )
    IS_TEAM = (
        'Данное поле указывает на принадлежность'
        ' пользователя к команде Балапанлар.'
    )
    IS_ACTIVE = (
        'Данное поле указывает, что аккаунт пользователя "Действующий".'
    )
