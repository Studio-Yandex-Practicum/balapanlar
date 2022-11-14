from .course_price_admin import (
    CoursePriceAdmin,
    IncludedInCoursePriceAdmin,
    NotIncludedInCoursePriceAdmin,
)
from .course_tag_admin import CourseAdmin, TagAdmin
from .faq_admin import FAQAdmin
from .location_admin import LocationAdmin
from .partners_admin import PartnersAdmin
from .principles_admin import PrinciplesAdmin
from .program_admin import ProgramAdmin, ProgramCharacteristicAdmin
from .requisites_admin import RequisitesAdmin
from .user_admin import CustomUserAdmin

__all__ = [
    'CourseAdmin',
    'CoursePriceAdmin',
    'CustomUserAdmin',
    'FAQAdmin',
    'IncludedInCoursePriceAdmin',
    'LocationAdmin',
    'NotIncludedInCoursePriceAdmin',
    'PartnersAdmin',
    'PrinciplesAdmin',
    'ProgramAdmin',
    'ProgramCharacteristicAdmin',
    'RequisitesAdmin',
    'TagAdmin',
]
