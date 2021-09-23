from django.shortcuts import render

def activities(request):
    return render(request, 'activities/activities.html')

# Create your views here.
