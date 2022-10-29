from django.contrib import admin
from .models import (Course, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'age_groups', 'duration', 'description', 'skills')
    search_fields = ('name',)
    list_editable = ('category', 'age_groups', 'duration', 'description', 'skills')