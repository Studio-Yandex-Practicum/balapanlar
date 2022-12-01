from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import (
    BenefitViewSet,
    CourseViewSet,
    CoursePriceViewSet,
    FAQViewSet,
    IncludedInCoursePriceViewSet,
    LocationViewSet,
    NotIncludedInCoursePriceViewSet,
    PartnerViewSet,
    PrincipleViewSet,
    ProgramViewSet,
    ProgramCharacteristicViewSet,
    RequisiteViewSet,
    TeamMemberViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()


router_v1.register('benefits', BenefitViewSet, basename='benefits')
router_v1.register('questions', FAQViewSet, basename='questions')
router_v1.register('locations', LocationViewSet, basename='locations')
router_v1.register('partners', PartnerViewSet, basename='partners')
router_v1.register('principles', PrincipleViewSet, basename='principles')
router_v1.register('requisites', RequisiteViewSet, basename='requisites')
router_v1.register('programs', ProgramViewSet, basename='programs')
router_v1.register('programs_characteristics', ProgramCharacteristicViewSet,
                   basename='programs_characteristics')
router_v1.register('course_prices', CoursePriceViewSet,
                   basename='course_prices')
router_v1.register('included_in_course_price', IncludedInCoursePriceViewSet,
                   basename='included_in_course_price')
router_v1.register('not_included_in_course_price',
                   NotIncludedInCoursePriceViewSet,
                   basename='not_included_in_course_price')
router_v1.register('team_members', TeamMemberViewSet, basename='team_members')
router_v1.register('courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
