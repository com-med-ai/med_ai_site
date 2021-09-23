from django.urls import path

from .views import workgroups

app_name = 'workgroups'

urlpatterns = [
    path('', workgroups, name='workgroups'),
]