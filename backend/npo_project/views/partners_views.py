from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Partners
from ..serializers import PartnersSerializer


class PartnersViewSet(ReadOnlyModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
