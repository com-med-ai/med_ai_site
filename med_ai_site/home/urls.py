from django.urls import path
from .views import falan


urlpatterns = [
    path('', falan)
]