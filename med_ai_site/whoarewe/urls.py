from django.urls import path

from .views import whoarewe

app_name = 'whoarewe'

urlpatterns = [
    path('', whoarewe, name='whoarewe'),
]