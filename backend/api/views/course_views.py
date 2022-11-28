from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from npo_project.models import Course
from .constants import SCHEMA_PARAMS
from ..serializers import CourseSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Раздел "Наши курсы"

    ---
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
