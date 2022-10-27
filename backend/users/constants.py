# Constants for testing CustomUser model
VALID_EMAIL_1_TEST = 'valid-email@example.com'
VALID_PASSWORD_1_TEST = 'testpassword123'
VALID_FIRST_NAME_1_TEST = 'User'
VALID_LAST_NAME_1_TEST = 'Valid'

VALID_EMAIL_2_TEST = 'goodemail@example.com'
VALID_PASSWORD_2_TEST = 'veryhardpassword123'
VALID_FIRST_NAME_2_TEST = 'UserValid'
VALID_LAST_NAME_2_TEST = 'Valid-User'

VERBOSE_NAME_ID_TEST = 'UUID Пользователя'
HELP_TEXT_ID_TEST = 'Уникальный идентификатор пользователя.'

VERBOSE_NAME_EMAIL_TEST = 'Электронная почта'
HELP_TEXT_EMAIL_TEST = 'Электронная почта пользователя.'

VERBOSE_NAME_PASSWORD_TEST = 'Пароль'
HELP_TEXT_PASSWORD_TEST = (
    'Пароль пользователя длиной не менее 8 символов и не более 32.'
)

VERBOSE_NAME_FIRST_NAME_TEST = 'Имя'
HELP_TEXT_FIRST_NAME_TEST = (
    'Имя пользователя длиной не более 128 символов. Может содержать '
    'заглавные и строчные буквы русского и английского '
    'алфавитов и символ "-".'
)

VERBOSE_NAME_LAST_NAME_TEST = 'Фамилия'
HELP_TEXT_LAST_NAME_TEST = (
    'Фамилия пользователя длиной не более 128 символов. '
    'Может содержать заглавные и строчные буквы русского '
    'и английского алфавитов и символ "-".'
)

VERBOSE_NAME_TEAM_TEST = 'Команда Балапанлар'
HELP_TEXT_TEAM_TEST = (
    'Данное поле указывает на принадлежность'
    ' пользователя к команде Балапанлар.'
)
VERBOSE_NAME_ACTIVE_TEST = 'Аккаунт активен'
HELP_TEXT_ACTIVE_TEST = (
    'Данное поле указывает, что аккаунт пользователя "Действующий".'
)
