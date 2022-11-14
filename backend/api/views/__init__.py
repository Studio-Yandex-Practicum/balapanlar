from .course_price_view import (
    CoursePriceViewSet, IncludedInCoursePriceViewSet,
    NotIncludedInCoursePriceViewSet
)
from .partners_views import PartnersViewSet
from .principles_views import PrinciplesViewSet
from .program_view import ProgramViewSet, ProgramCharacteristicViewSet
from .requisites_views import RequisitesViewSet


__all__ = [
    CoursePriceViewSet,
    IncludedInCoursePriceViewSet,
    NotIncludedInCoursePriceViewSet,
    PartnersViewSet,
    PrinciplesViewSet,
    ProgramViewSet,
    ProgramCharacteristicViewSet,
    RequisitesViewSet
]
