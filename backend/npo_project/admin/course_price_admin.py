from django.contrib import admin

from ..models import (IncludedInCoursePrice, NotIncludedInCoursePrice,
                      CoursePrice)


@admin.register(CoursePrice)
class CoursePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'payment_url')
    list_editable = ('price', 'payment_url',)


@admin.register(IncludedInCoursePrice)
class IncludedInCoursePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_editable = ('text',)


@admin.register(NotIncludedInCoursePrice)
class NotIncludedInCoursePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_editable = ('text',)
