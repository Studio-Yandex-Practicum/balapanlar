from rest_framework import serializers

from npo_project.models import (
    CoursePrice, IncludedInCoursePrice, NotIncludedInCoursePrice
)


class IncludedInCoursePriceSerializer(serializers.ModelSerializer):
    course_price = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='price'
    )  # переделать slug_field на название курса с данной стоимостью

    class Meta:
        model = IncludedInCoursePrice
        fields = ('id', 'text', 'course_price')


class NotIncludedInCoursePriceSerializer(serializers.ModelSerializer):
    course_price = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='price'
    )  # переделать slug_field на название курса с данной стоимостью

    class Meta:
        model = NotIncludedInCoursePrice
        fields = ('id', 'text', 'course_price')


class CoursePriceSerializer(serializers.ModelSerializer):
    included_in_price = IncludedInCoursePriceSerializer(
        many=True, read_only=True
    )
    not_included_in_price = NotIncludedInCoursePriceSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = CoursePrice
        fields = ('id', 'price', 'included_in_price',
                  'not_included_in_price', 'payment_url')
