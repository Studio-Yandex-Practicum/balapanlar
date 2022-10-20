from django.urls import path

from npo_project.views import index

app_name = 'npo_project'

urlpatterns = [
    path('', index, name='index')
]
