"""
This file contents the CourseAdmin class and all classes related to it:
CourseCategoryAdmin, CourseTagAdmin.
"""

from tinymce.widgets import TinyMCE

from django import forms
from django.contrib import admin

from ..models import Course, CourseCategory, CourseTag


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CourseAdminForm(forms.ModelForm):
    skills = forms.CharField(
        label='Какие умения даст курс',
        widget=TinyMCE,
        help_text='(необязательное поле) По желанию напишите список умений, '
                  'которые учащиеся приобретут по окончании курса.',
        required=False
    )

    class Meta:
        model = Course
        fields = ('name', 'category', 'age_groups', 'duration',
                  'description', 'tags', 'skills')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('name', 'category', 'age_groups', 'duration',
                    'description',)
    search_fields = ('name',)
