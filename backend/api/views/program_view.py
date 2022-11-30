from rest_framework import mixins, viewsets

from npo_project.models import Program, ProgramCharacteristic
from ..serializers import (
    ProgramSerializer, ProgramCharacteristicSerializer
)


class ProgramViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "О нас"

    ---
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramCharacteristicViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Характеристики карточек раздела "О нас"

    ---
    """
    queryset = ProgramCharacteristic.objects.all()
    serializer_class = ProgramCharacteristicSerializer
