from django.urls import path

from .views import activities

app_name = 'activities'

urlpatterns = [
    path('', activities, name='activities'),
]