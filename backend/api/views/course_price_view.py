from rest_framework import mixins, viewsets

from npo_project.models import (
    CoursePrice, IncludedInCoursePrice, NotIncludedInCoursePrice
)
from ..serializers import (
    CoursePriceSerializer, IncludedInCoursePriceSerializer,
    NotIncludedInCoursePriceSerializer
)


class IncludedInCoursePriceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Что включено в стоимость

    ---
    """
    queryset = IncludedInCoursePrice.objects.all()
    serializer_class = IncludedInCoursePriceSerializer


class NotIncludedInCoursePriceViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    Что не включено в стоимость

    ---
    """
    queryset = NotIncludedInCoursePrice.objects.all()
    serializer_class = NotIncludedInCoursePriceSerializer


class CoursePriceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Стоимость курсов"

    ---
    """
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer
