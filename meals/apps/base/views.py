"""Views for the base app"""

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestoranForm, MealForm, MenuForm
from .models import Restoran, Meal, Menu


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def restoran(request):
    return render(request, 'base/restoran.html')

def new_restoran(request):
    if request.method == 'POST':
        form = RestoranForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RestoranForm()
    return render(request, 'base/add_item.html', {'type': 'Restoran', 'form': form})

def new_meal(request):
    if request.method == 'POST':
        form = MealForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MealForm()
    return render(request, 'base/add_item.html', {'type': 'Meal', 'form': form})

def new_menu(request):
    if request.method == 'POST':
        form = MenuForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MenuForm()
    return render(request, 'base/add_item.html', {'type': 'Menu', 'form': form})

def tester(request):
    return render(request, 'base/tester.html', {'items': Restoran.objects.all()})

def restoran2(request, pk):
    r= get_object_or_404(Restoran, pk=pk)
    return render(request, 'base/restoran_2.html', context={'r': r})
