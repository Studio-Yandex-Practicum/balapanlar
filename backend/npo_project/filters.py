from django_filters import ChoiceFilter, FilterSet

from .models import Benefit


class BenefitFilter(FilterSet):
    beneficial_to = ChoiceFilter(choices=Benefit.RoleChoices.choices)

    class Meta:
        model = Benefit
        fields = ('beneficial_to',)
