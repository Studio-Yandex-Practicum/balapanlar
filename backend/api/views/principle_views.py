from rest_framework import mixins, viewsets

from npo_project.models import Principle
from ..serializers import PrincipleSerializer


class PrincipleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Наши принципы"

    ---
    """
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
