from rest_framework import mixins, viewsets

from npo_project.models import Partner
from ..serializers import PartnerSerializer


class PartnerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Наши партнеры"

    ---
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
