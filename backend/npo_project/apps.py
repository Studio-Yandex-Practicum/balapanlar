from django.apps import AppConfig
from django.contrib import admin

ADMIN_ORDERING = [
    ('npo_project', [
        'Course',
        'CourseCategory',
        'CourseTag',
        'CoursePrice',
        'IncludedInCoursePrice',
        'NotIncludedInCoursePrice',
        'Benefit',
        'Program',
        'ProgramCharacteristic',
        'Principles',
        'TeamMember',
        'FAQ',
        'Partners',
        'Location',
        'Requisites',
        'CustomUser',
    ]),
]


def custom_get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in ADMIN_ORDERING:
        app = app_dict[app_name]
        app['models'].sort(key=lambda x: object_list.index(x['object_name']))
        yield app


admin.AdminSite.get_app_list = custom_get_app_list


class NpoProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'npo_project'
    verbose_name = 'Управление проектом'
