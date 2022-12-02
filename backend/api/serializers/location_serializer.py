from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from npo_project.models import Location


class LocationSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Location
        fields = (
            'id',
            'full_address',
            'latitude',
            'longitude',
            'image',
            'schema_description'
        )
