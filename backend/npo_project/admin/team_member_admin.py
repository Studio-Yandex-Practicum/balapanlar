from sorl.thumbnail import get_thumbnail

from django import forms
from django.contrib import admin
from django.utils.html import format_html

from balapanlar.settings import EMPTY_VALUE_ADMIN_PANEL
from ..models import TeamMember


class TeamRoleWidget(forms.MultiWidget):
    DEFAULT_ROLES = set([
        ('', ''),
        ('Основательница', 'Основательница'),
        ('Администратор', 'Администратор'),
        ('Куратор', 'Куратор')
    ])

    def __init__(self, attrs=None):
        self.roles = self.get_roles()
        self.widgets = [
            forms.Select(attrs=attrs, choices=self.roles),
            forms.TextInput(attrs=attrs),
        ]
        super().__init__(self.widgets, attrs)

    def get_roles(self):
        try:
            roles = set(
                [
                    (
                        i.get('role'), i.get('role')
                    ) for i in TeamMember.objects.all().values('role')
                ]
            )
            return sorted(self.DEFAULT_ROLES.union(roles))
        except Exception:
            return sorted(self.DEFAULT_ROLES)

    def update(self, **kwargs):
        self.__init__(**kwargs)

    def decompress(self, value):
        self.update()
        if value:
            return [value, '']
        return [None, None]

    def value_from_datadict(self, data, files, name):
        choice_value, input_value = super().value_from_datadict(
            data, files, name
        )
        if (input_value.split() and (
            input_value, input_value
        ) not in self.get_roles()):
            return input_value
        return choice_value


class TeamMemberAdminForm(forms.ModelForm):
    role = forms.CharField(
        label='Роль в команде',
        widget=TeamRoleWidget,
        help_text='Выберите из списка. Если подходящего нет - '
                  'введите новое значение.'
    )

    class Meta:
        model = TeamMember
        exclude = ('id', 'full_name')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberAdminForm
    list_display = ('full_name', 'role', 'image', 'preview')
    list_editable = ('image',)
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL
    list_filter = ('role',)
    search_fields = ('name',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            image = get_thumbnail(
                obj.image, '200x200', upscale=False, crop=False, quality=100
            )
            return format_html(
                f'<img src="{image.url}" '
                f'width="{image.width}" height="{image.height}">'
            )
        return 'Фотография еще не сохранена'
    preview.allow_tags = True
    preview.short_description = 'Предпросмотр загруженной фотографии'
