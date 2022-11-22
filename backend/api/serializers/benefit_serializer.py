from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from npo_project.models import Benefit


class BenefitSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Benefit


class BenefitRoleSerializer(BenefitSerializer):

    class Meta(BenefitSerializer.Meta):
        exclude = ('beneficial_to',)
