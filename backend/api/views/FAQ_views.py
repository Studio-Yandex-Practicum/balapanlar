from rest_framework.viewsets import ReadOnlyModelViewSet

from npo_project.models import FAQ
from ..serializers import FAQSerializer


class FAQViewSet(ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
