from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models import Benefit


class BenefitSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Benefit
        exclude = ('id',)


class BenefitRoleSerializer(BenefitSerializer):

    class Meta(BenefitSerializer.Meta):
        exclude = ('id', 'beneficial_to',)
