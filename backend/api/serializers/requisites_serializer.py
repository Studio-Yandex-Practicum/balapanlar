from rest_framework import serializers

from npo_project.models import Requisite


class RequisitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisite
        fields = ('id', 'text')
