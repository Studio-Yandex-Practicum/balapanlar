from rest_framework import serializers

from npo_project.models import Course, CourseTag


class CourseTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseTag
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = CourseTagSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'category', 'age_groups', 'duration',
                  'description', 'tags', 'skills')
