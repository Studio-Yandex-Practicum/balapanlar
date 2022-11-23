from rest_framework import viewsets

from npo_project.models import Requisite
from ..serializers import RequisitesSerializer


class RequisitesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Requisite.objects.all()
    serializer_class = RequisitesSerializer
