from rest_framework import serializers

from npo_project.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'category', 'age_groups', 'duration',
                  'description', 'tags', 'skills')
