from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home/home.html")

# Create your views here.
