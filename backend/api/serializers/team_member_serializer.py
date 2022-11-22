from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from npo_project.models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = TeamMember
