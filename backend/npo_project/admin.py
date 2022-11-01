from django import forms
from django.contrib import admin
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from .models import Benefit, TeamMember

EMPTY = '-пусто-'


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
        roles = set(
            [
                (
                    i.get('role'), i.get('role')
                ) for i in TeamMember.objects.all().values('role')
            ]
        )
        return sorted(self.DEFAULT_ROLES.union(roles))

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
        if (input_value.split()
                and (input_value, input_value) not in self.get_roles()):
            return input_value
        return choice_value


class TeamMemberAdminForm(forms.ModelForm):
    role = forms.CharField(
        label='Роль в команде',
        widget=TeamRoleWidget,
        help_text='Выберите из списка или введите новое значение'
    )

    class Meta:
        model = TeamMember
        fields = ('name', 'role', 'image')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberAdminForm
    list_display = ('name', 'role', 'preview',)
    empty_value_display = EMPTY
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
        return ''
    preview.allow_tags = True
    preview.short_description = 'Предпросмотр'


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('text', 'beneficial_to', 'preview')
    empty_value_display = EMPTY
    list_filter = ('beneficial_to',)
    search_fields = ('text',)
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
        return ''
    preview.allow_tags = True
    preview.short_description = 'Предпросмотр'
