from django.shortcuts import render, HttpResponse

def falan(request):
    return render(request, "home/home.html")

# Create your views here.
