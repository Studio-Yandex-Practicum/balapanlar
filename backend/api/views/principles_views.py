from rest_framework.viewsets import ReadOnlyModelViewSet

from npo_project.models import Principles
from ..serializers import PrinciplesSerializer


class PrinciplesViewSet(ReadOnlyModelViewSet):
    queryset = Principles.objects.all()
    serializer_class = PrinciplesSerializer
