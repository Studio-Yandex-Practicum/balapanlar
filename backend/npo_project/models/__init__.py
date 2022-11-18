from .benefit import Benefit
from .cource_tags import Course, Tag
from .course_price import (
    CoursePrice,
    IncludedInCoursePrice,
    NotIncludedInCoursePrice,
)
from .faq import FAQ
from .location import Location
from .partners import Partners
from .principles import Principles
from .program import Program, ProgramCharacteristic
from .requisites import Requisites
from .team_member import TeamMember
from .user import CustomUser

__all__ = [
    'Benefit',
    'Course',
    'CoursePrice',
    'CustomUser',
    'FAQ',
    'IncludedInCoursePrice',
    'Location',
    'NotIncludedInCoursePrice',
    'Partners',
    'Principles',
    'Program',
    'ProgramCharacteristic',
    'Requisites',
    'Tag',
    'TeamMember'
]
