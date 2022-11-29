<<<<<<< HEAD
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ReadOnlyModelViewSet

from npo_project.models import Requisites
from .constants import SCHEMA_PARAMS
from ..serializers import RequisitesSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class RequisitesViewSet(ReadOnlyModelViewSet):
    """
    Данные организации: реквизиты

    ---
    """
    queryset = Requisites.objects.all()
=======
from rest_framework import viewsets

from npo_project.models import Requisite
from ..serializers import RequisitesSerializer


class RequisitesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Requisite.objects.all()
>>>>>>> 91bf0de0d3f9e5afcd578ad35d58cbcb3c5c6aa3
    serializer_class = RequisitesSerializer
