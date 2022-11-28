from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from npo_project.models import Benefit
from .constants import SCHEMA_PARAMS
from ..filters import BenefitFilter
from ..serializers import BenefitRoleSerializer, BenefitSerializer


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['beneficial_to']
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class BenefitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Разделы "Почему вашему ребёнку понравится у нас?"
    и "Почему это удобно родителям?"

    ---
    """
    queryset = Benefit.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BenefitFilter

    def get_serializer_class(self):
        if not self.request or self.request.query_params:
            return BenefitRoleSerializer
        return BenefitSerializer
