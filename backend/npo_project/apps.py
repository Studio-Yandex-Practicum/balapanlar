from django.apps import AppConfig
from django.contrib import admin
from django.http import Http404
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _

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
        'Principle',
        'TeamMember',
        'FAQ',
        'Partner',
        'Location',
        'Requisite',
        'CustomUser',
    ]),
]


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, models_list in ADMIN_ORDERING:
        app = app_dict[app_name]
        # Sort the models according to ADMIN_ORDERING
        app['models'].sort(key=lambda x: models_list.index(x['object_name']))
        yield app


def app_index(self, request, app_label, extra_context=None):
    app_dict = self._build_app_dict(request, app_label)
    if not app_dict:
        raise Http404('The requested admin page does not exist.')

    # Sort the models within each app according to ADMIN_ORDERING
    models_list = ADMIN_ORDERING[0][1]
    app_dict['models'].sort(key=lambda x: models_list.index(x['object_name']))

    context = {
        **self.each_context(request),
        'title': _('%(app)s administration') % {'app': app_dict['name']},
        'subtitle': None,
        'app_list': [app_dict],
        'app_label': app_label,
        **(extra_context or {}),
    }

    request.current_app = self.name

    return TemplateResponse(request, self.app_index_template or [
        'admin/%s/app_index.html' % app_label,
        'admin/app_index.html'
    ], context)


admin.AdminSite.get_app_list = get_app_list
admin.AdminSite.app_index = app_index


class NpoProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'npo_project'
    verbose_name = 'Управление проектом'
