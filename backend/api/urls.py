from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import (
    PartnersViewSet,
    PrinciplesViewSet,
    RequisitesViewSet,
    LocationViewSet)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('locations', LocationViewSet, basename='locations')
router_v1.register('partners', PartnersViewSet, basename='partners')
router_v1.register('principles', PrinciplesViewSet, basename='principles')
router_v1.register('requisites', RequisitesViewSet, basename='requisites')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
