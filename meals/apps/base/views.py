"""Views for the base app"""

from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def restoran(request):
    return render(request, 'base/restoran.html')
