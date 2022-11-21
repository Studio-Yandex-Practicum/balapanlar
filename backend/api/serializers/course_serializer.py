from rest_framework import serializers

from npo_project.models import Course


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name'
    )

    class Meta:
        model = Course
        fields = ('id', 'name', 'category', 'age_groups', 'duration',
                  'description', 'tags', 'skills')
