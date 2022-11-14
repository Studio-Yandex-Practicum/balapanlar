from rest_framework.viewsets import ReadOnlyModelViewSet

from npo_project.models import Requisites
from ..serializers import RequisitesSerializer


class RequisitesViewSet(ReadOnlyModelViewSet):
    queryset = Requisites.objects.all()
    serializer_class = RequisitesSerializer
