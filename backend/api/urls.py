from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CoursePriceViewSet,
    IncludedInCoursePriceViewSet,
    NotIncludedInCoursePriceViewSet,
    PartnersViewSet,
    PrinciplesViewSet,
    ProgramViewSet,
    ProgramCharacteristicViewSet,
    RequisitesViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()


router_v1.register('partners', PartnersViewSet, basename='partners')
router_v1.register('principles', PrinciplesViewSet, basename='principles')
router_v1.register('requisites', RequisitesViewSet, basename='requisites')
router_v1.register('programs', ProgramViewSet, basename='programs')
router_v1.register('programs_characteristics', ProgramCharacteristicViewSet,
                   basename='programs_characteristics')
router_v1.register('course_prices', CoursePriceViewSet, basename='course_prices')
router_v1.register('included_in_course_price', IncludedInCoursePriceViewSet,
                   basename='included_in_course_price')
router_v1.register('not_included_in_course_price',
                   NotIncludedInCoursePriceViewSet,
                   basename='not_included_in_course_price')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
