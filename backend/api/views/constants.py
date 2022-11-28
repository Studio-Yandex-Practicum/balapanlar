from drf_yasg import openapi

SCHEMA_PARAMS = {
    'beneficial_to': [openapi.Parameter(
        'beneficial_to',
        openapi.IN_QUERY,
        description='Выбор раздела "Почему вашему ребёнку понравится у нас?"'
                    ' или "Почему это удобно родителям?"',
        type=openapi.TYPE_STRING,
        enum=('PARENT', 'CHILD')
    )],
    'id': [openapi.Parameter(
        'id',
        openapi.IN_PATH,
        description='Уникальный идентификатор записи',
        type=openapi.TYPE_INTEGER
    )],
}
