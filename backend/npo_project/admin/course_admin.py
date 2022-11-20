'''
This file contents the CourseAdmin class and all classes related to it:
CourseCategoryAdmin, CourseTagAdmin.
'''

from django.contrib import admin

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
class CourseTagAdmin(HiddenAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'age_groups', 'duration',
                    'description', 'skills',)
    search_fields = ('name',)
