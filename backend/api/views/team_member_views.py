from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from npo_project.models import TeamMember
from .constants import SCHEMA_PARAMS
from ..serializers import TeamMemberSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        manual_parameters=SCHEMA_PARAMS['id']
    )
)
class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Раздел "Команда"
    
    ---
    """
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
