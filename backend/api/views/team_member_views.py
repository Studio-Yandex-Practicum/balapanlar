from rest_framework import mixins, viewsets

from npo_project.models import TeamMember
from ..serializers import TeamMemberSerializer


class TeamMemberViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Команда"

    ---
    """
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
