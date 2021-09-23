from django.urls import path

from .views import workgroups, workgroup

app_name = 'workgroups'

urlpatterns = [
    path('', workgroups, name='workgroups'),
    path('<int:team_id>workgroup/', workgroup, name='workgroup'),
]