from .benefit_views import BenefitViewSet
from .course_price_view import (
    CoursePriceViewSet, IncludedInCoursePriceViewSet,
    NotIncludedInCoursePriceViewSet
)
from .partners_views import PartnersViewSet
from .principles_views import PrinciplesViewSet
from .program_view import ProgramViewSet, ProgramCharacteristicViewSet
from .requisites_views import RequisitesViewSet
from .team_member_views import TeamMemberViewSet


__all__ = [
    BenefitViewSet,
    CoursePriceViewSet,
    IncludedInCoursePriceViewSet,
    NotIncludedInCoursePriceViewSet,
    PartnersViewSet,
    PrinciplesViewSet,
    ProgramViewSet,
    ProgramCharacteristicViewSet,
    RequisitesViewSet,
    TeamMemberViewSet
]
