from rest_framework import mixins, viewsets

from npo_project.models import FAQ
from ..serializers import FAQSerializer


class FAQViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Раздел "Часто задаваемые вопросы"

    ---
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
