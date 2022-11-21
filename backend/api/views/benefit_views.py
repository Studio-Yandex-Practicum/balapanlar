from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from npo_project.models import Benefit
from ..filters import BenefitFilter
from ..serializers import BenefitRoleSerializer, BenefitSerializer


class BenefitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Benefit.objects.all()
    filterset_class = BenefitFilter

    def get_serializer_class(self):
        if 'for_' in self.request.get_full_path():
            return BenefitRoleSerializer
        return BenefitSerializer

    @action(methods=["get", ], detail=False)
    def for_children(self, request):
        beneficial_to = self.queryset.filter(beneficial_to='CHILD')
        serializer = self.get_serializer(beneficial_to, many=True)
        return Response(serializer.data)

    @action(methods=["get", ], detail=False)
    def for_parents(self, request):
        beneficial_to = self.queryset.filter(beneficial_to='PARENT')
        serializer = self.get_serializer(beneficial_to, many=True)
        return Response(serializer.data)
