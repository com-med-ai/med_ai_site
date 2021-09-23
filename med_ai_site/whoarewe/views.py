from django.shortcuts import render
from .models import WhoAreWe

def whoarewe(request):
    """buffer = WhoAreWe.objects.all()
    about_us = []
    for member in buffer:
        member_tuple = (member.name, member.stylist_name, member.text)
        about_us.append(member_tuple)
    print(about_us)"""
    about_us = WhoAreWe.objects.all()
    context = {
        'about_us': about_us
    }
    return render(request, 'whoarewe/whoarewe.html', context)

    




# Create your views here.
