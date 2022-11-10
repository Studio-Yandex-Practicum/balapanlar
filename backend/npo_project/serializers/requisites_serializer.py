from rest_framework import serializers

from ..models import Requisites


class RequisitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisites
        fields = ['text']
