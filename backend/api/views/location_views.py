from rest_framework import mixins, viewsets

from npo_project.models import Location
from ..serializers import LocationSerializer


class LocationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Как нас найти"

    ---
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
