from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from npo_project.models import Location


class LocationSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Location
        fields = ('id', 'address', 'image')
