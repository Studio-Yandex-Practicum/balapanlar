from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CoursePriceViewSet,
    IncludedInCoursePriceViewSet,
    NotIncludedInCoursePriceViewSet,
    ProgramViewSet,
    ProgramCharacteristicViewSet
)


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('programs', ProgramViewSet)
router_v1.register('programs_characteristics', ProgramCharacteristicViewSet)
router_v1.register('course_prices', CoursePriceViewSet)
router_v1.register('included_in_course_price', IncludedInCoursePriceViewSet)
router_v1.register('not_included_in_course_price',
                   NotIncludedInCoursePriceViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
