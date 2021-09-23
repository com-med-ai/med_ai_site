from django.shortcuts import render
from .models import Team

def workgroups(request):
    teams = Team.objects.all()
    print(teams)
    print(teams[0].team_name)
    context = {
        'teams': teams
    }
    return render(request, 'workgroups/workgroups.html', context)

def workgroup(request, team_id):
    team = Team.objects.get(pk=team_id)
    context = {
        'team': team,
        'leader': team.team_leader
    }
    return render(request, 'workgroups/workgroup.html', context)

# Create your views here.
