from django.shortcuts import render

def whoarewe(request):
    return render(request, 'whoarewe/whoarewe.html')

# Create your views here.
