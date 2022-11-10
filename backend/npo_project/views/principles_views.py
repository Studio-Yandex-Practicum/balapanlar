from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Principles
from ..serializers import PrinciplesSerializer


class PrinciplesViewSet(ReadOnlyModelViewSet):
    queryset = Principles.objects.all()
    serializer_class = PrinciplesSerializer
