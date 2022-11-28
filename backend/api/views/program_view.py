from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from npo_project.models import Program, ProgramCharacteristic
from .constants import SCHEMA_PARAMS
from ..serializers import (
    ProgramSerializer, ProgramCharacteristicSerializer
)


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Раздел "О нас"

    ---
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class ProgramCharacteristicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Характеристики карточек раздела "О нас"

    ---
    """
    queryset = ProgramCharacteristic.objects.all()
    serializer_class = ProgramCharacteristicSerializer
