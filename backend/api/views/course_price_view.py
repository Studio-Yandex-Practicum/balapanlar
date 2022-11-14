from rest_framework import viewsets

from npo_project.models import (
    CoursePrice, IncludedInCoursePrice, NotIncludedInCoursePrice
)
from ..serializers import (
    CoursePriceSerializer, IncludedInCoursePriceSerializer,
    NotIncludedInCoursePriceSerializer
)


class IncludedInCoursePriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IncludedInCoursePrice.objects.all()
    serializer_class = IncludedInCoursePriceSerializer


class NotIncludedInCoursePriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NotIncludedInCoursePrice.objects.all()
    serializer_class = NotIncludedInCoursePriceSerializer


class CoursePriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer
