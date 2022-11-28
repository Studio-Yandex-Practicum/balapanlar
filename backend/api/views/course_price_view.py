from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from npo_project.models import (
    CoursePrice, IncludedInCoursePrice, NotIncludedInCoursePrice
)
from .constants import SCHEMA_PARAMS
from ..serializers import (
    CoursePriceSerializer, IncludedInCoursePriceSerializer,
    NotIncludedInCoursePriceSerializer
)


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class IncludedInCoursePriceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Что включено в стоимость

    ---
    """
    queryset = IncludedInCoursePrice.objects.all()
    serializer_class = IncludedInCoursePriceSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class NotIncludedInCoursePriceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Что не включено в стоимость

    ---
    """
    queryset = NotIncludedInCoursePrice.objects.all()
    serializer_class = NotIncludedInCoursePriceSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class CoursePriceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Раздел "Стоимость курсов"

    ---
    """
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer
