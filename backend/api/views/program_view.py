from rest_framework import viewsets

from npo_project.models import Program, ProgramCharacteristic
from ..serializers import (
    ProgramSerializer, ProgramCharacteristicSerializer
)


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramCharacteristicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProgramCharacteristic.objects.all()
    serializer_class = ProgramCharacteristicSerializer
