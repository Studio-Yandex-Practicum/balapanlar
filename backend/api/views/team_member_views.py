from rest_framework import viewsets

from npo_project.models import TeamMember
from serializers import TeamMemberSerializer


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
