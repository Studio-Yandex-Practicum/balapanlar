from .benefit_admin import BenefitAdmin
from .course_price_admin import (
    CoursePriceAdmin,
    IncludedInCoursePriceAdmin,
    NotIncludedInCoursePriceAdmin,
)
from .course_admin import CourseAdmin, CourseTagAdmin
from .faq_admin import FAQAdmin
from .location_admin import LocationAdmin
from .partners_admin import PartnersAdmin
from .principles_admin import PrinciplesAdmin
from .program_admin import ProgramAdmin, ProgramCharacteristicAdmin
from .requisites_admin import RequisitesAdmin
from .team_member_admin import TeamMemberAdmin
from .user_admin import CustomUserAdmin

__all__ = [
    'BenefitAdmin',
    'CourseAdmin',
    'CoursePriceAdmin',
    'CourseTagAdmin',
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
    'TeamMemberAdmin'
]
