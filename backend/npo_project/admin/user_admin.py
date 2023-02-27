from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from balapanlar.settings import EMPTY_VALUE_ADMIN_PANEL
from ..forms import CustomUserChangeForm, CustomUserCreationForm
from ..models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_team',
        'is_active',
        'is_superuser',
    )
    list_filter = ('email', 'first_name', 'first_name', 'is_team')
    list_editable = ('first_name', 'last_name', 'is_team')
    fieldsets = (
        (
            'Информация об аккаунте',
            {'fields': ('email', 'password', 'is_active', 'last_login')},
        ),
        ('Персональная информация', {'fields': ('first_name', 'last_name')}),
        (
            'Права доступа',
            {'fields':
                ('is_team', 'is_superuser', 'groups', 'user_permissions')
             },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'first_name',
                    'last_name',
                ),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = (
        'groups',
        'user_permissions',
    )
    empty_value_display = EMPTY_VALUE_ADMIN_PANEL
