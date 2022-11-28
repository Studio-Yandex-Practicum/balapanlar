from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ReadOnlyModelViewSet

from npo_project.models import Partners
from .constants import SCHEMA_PARAMS
from ..serializers import PartnersSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class PartnersViewSet(ReadOnlyModelViewSet):
    """
    Раздел "Наши партнеры"

    ---
    """
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
