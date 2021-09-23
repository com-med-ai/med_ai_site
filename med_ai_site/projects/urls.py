from django.urls import path

from .views import projects

app_name = 'projects'

urlpatterns = [
    path('', projects, name='projects'),
]