from rest_framework import viewsets

from npo_project.models import Partner
from ..serializers import PartnersSerializer


class PartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnersSerializer
