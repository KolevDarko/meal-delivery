
from .models import Restoran
from django.db.utils import OperationalError


def restorani(request):
    rests = Restoran.objects.filter(type='restoran')
    return {
        'restorani': rests
    }


def picerii(request):
    return {
        'picerii': Restoran.objects.filter(type='picerija')
    }


def sendvicari(request):
    return {
        'sendvicari': Restoran.objects.all()
    }


def burekcilnici(request):
    return {
        'burekcilnici': Restoran.objects.filter(type='burekcilnica')
    }
