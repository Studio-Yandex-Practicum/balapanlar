from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = TeamMember
        exclude = ('id',)
