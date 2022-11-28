from rest_framework import viewsets

from npo_project.models import Course
from ..serializers import CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
