from django.shortcuts import render

def anouncements(request):
    return render(request, 'anouncements/anouncements.html')

# Create your views here.
