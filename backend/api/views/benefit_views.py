from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from npo_project.models import Benefit
from ..filters import BenefitFilter
from ..serializers import BenefitRoleSerializer, BenefitSerializer


class BenefitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Benefit.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BenefitFilter

    def get_serializer_class(self):
        if not self.request or self.request.query_params:
            return BenefitRoleSerializer
        return BenefitSerializer
