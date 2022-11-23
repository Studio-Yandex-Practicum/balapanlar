from rest_framework import viewsets

from npo_project.models import Principle
from ..serializers import PrinciplesSerializer


class PrinciplesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrinciplesSerializer
