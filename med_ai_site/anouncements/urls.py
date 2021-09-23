from django.urls import path

from .views import anouncements

app_name = 'anouncements'

urlpatterns = [
    path('', anouncements, name='anouncements'),
]

