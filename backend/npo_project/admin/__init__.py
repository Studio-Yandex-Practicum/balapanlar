from .course_price_admin import (
    CoursePriceAdmin, IncludedInCoursePriceAdmin,
    NotIncludedInCoursePriceAdmin,
)
from .program_admin import ProgramAdmin, ProgramCharacteristicAdmin
from .user_admin import CustomUserAdmin
from .FAQ_admin import FAQAdmin
from .Location_admin import LocationAdmin

__all__ = [
    CoursePriceAdmin,
    CustomUserAdmin,
    FAQAdmin,
    IncludedInCoursePriceAdmin,
    LocationAdmin,
    NotIncludedInCoursePriceAdmin,
    ProgramAdmin,
    ProgramCharacteristicAdmin,
]
