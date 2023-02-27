from django.contrib import admin

from ..models import (IncludedInCoursePrice, NotIncludedInCoursePrice,
                      CoursePrice)


@admin.register(CoursePrice)
class CoursePriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'payment_url')
    list_editable = ('payment_url',)


@admin.register(IncludedInCoursePrice)
class IncludedInCoursePriceAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(NotIncludedInCoursePrice)
class NotIncludedInCoursePriceAdmin(admin.ModelAdmin):
    list_display = ('text',)
