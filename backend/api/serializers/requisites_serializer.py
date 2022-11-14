from rest_framework import serializers

from npo_project.models import Requisites


class RequisitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisites
        fields = ['text']
