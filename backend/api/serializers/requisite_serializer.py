from rest_framework import serializers

from npo_project.models import Requisite


class RequisiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisite
        fields = ('id', 'text')
