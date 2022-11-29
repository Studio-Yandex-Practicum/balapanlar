from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from npo_project.models import Partner


class PartnersSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Partner
        fields = ('id', 'description', 'image', 'url')
