from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BenefitViewSet, TeamMemberViewSet

app_name = 'npo_project'

router_v1 = DefaultRouter()
router_v1.register('benefits', BenefitViewSet)
router_v1.register('team_members', TeamMemberViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
