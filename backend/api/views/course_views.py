from rest_framework import mixins, viewsets

from npo_project.models import Course
from ..serializers import CourseSerializer


class CourseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Наши курсы"

    ---
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
