from django.shortcuts import render

def projects(request):
    return render(request, 'projects/projects.html')

# Create your views here.
