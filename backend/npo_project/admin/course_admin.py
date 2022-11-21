'''
This file contents the CourseAdmin class and all classes related to it:
CourseCategoryAdmin, CourseTagAdmin.
'''

from django import forms
from django.contrib import admin
from tinymce.widgets import TinyMCE

from ..models import Course, CourseCategory, CourseTag


class HiddenAdmin(admin.ModelAdmin):
    '''
    Inheriting from this model when creating an admin model
    allows hiding the admin model from the list on the admin page
    while keeping it registered there.
    This makes the models list on the admin page clearer but keeps
    the functionality for the related models, which otherwise (without
    registering the "hidden" model at all) would be lost.
    '''
    def get_model_perms(self, request):
        '''
        Return empty perms dict thus hiding the model from admin index.
        '''
        return {}


@admin.register(CourseCategory)
class CourseCategoryAdmin(HiddenAdmin):
    pass


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
