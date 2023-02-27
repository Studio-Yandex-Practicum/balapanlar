from django.contrib import admin

from .benefit_admin import BenefitAdmin
from .course_price_admin import (
    CoursePriceAdmin,
    IncludedInCoursePriceAdmin,
    NotIncludedInCoursePriceAdmin,
)
from .course_admin import CourseAdmin, CourseTagAdmin
from .faq_admin import FAQAdmin
from .location_admin import LocationAdmin
from .partner_admin import PartnerAdmin
from .principle_admin import PrincipleAdmin
from .program_admin import ProgramAdmin, ProgramCharacteristicAdmin
from .requisite_admin import RequisiteAdmin
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
    'PartnerAdmin',
    'PrincipleAdmin',
    'ProgramAdmin',
    'ProgramCharacteristicAdmin',
    'RequisiteAdmin',
    'TeamMemberAdmin'
]

admin.AdminSite.site_header = 'Администрирование - Балапанлар'
