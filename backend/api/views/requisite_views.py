from rest_framework import mixins, viewsets

from npo_project.models import Requisite
from ..serializers import RequisiteSerializer


class RequisiteViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Данные организации: реквизиты

    ---
    """
    queryset = Requisite.objects.all()
    serializer_class = RequisiteSerializer
