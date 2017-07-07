"""Views for the base app"""

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import Restoran, Meal, Menu
from django.views.generic.edit import DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def restoran(request):
    return render(request, 'base/restoran.html')

def new_restoran(request):
    if request.method == 'POST':
        form = RestoranForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RestoranForm()
    return render(request, 'base/add_item.html', {'type': 'Restoran', 'form': form})

def new_meal(request):
    if request.method == 'POST':
        form = NewMealForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewMealForm()
    return render(request, 'base/add_item.html', {'type': 'Meal', 'form': form})

def new_menu(request):
    if request.method == 'POST':
        form = NewMenuForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewMenuForm()
    return render(request, 'base/add_item.html', {'type': 'Menu', 'form': form})

def edit_restoran(request, pk):
    restoran_instance = get_object_or_404(Restoran, pk=pk)
    if restoran_instance.owner == None or restoran_instance.owner == request.user or request.user.is_superuser:
        if request.method == 'POST':
            form = RestoranForm(data=request.POST, files=request.FILES, instance=restoran_instance)
            if form.is_valid():
                form.save()
                return redirect(reverse('restoran2', kwargs={'pk': pk}))
        else:
            form = RestoranForm(instance=restoran_instance)
        return render(request, 'base/edit_restoran.html', {'r': restoran_instance, 'form': form})
    else:
        return redirect('home')

def tester(request):
    return render(request, 'base/tester.html', {'items': Restoran.objects.all()})

def restoran2(request, pk):
    r= get_object_or_404(Restoran, pk=pk)
    return render(request, 'base/restoran_2.html', context={'r': r, 'lista_restorani': Restoran.objects.all()})

class Delete_restoran(DeleteView):
    model = Restoran
    success_url = reverse_lazy('tester')
    template_name = 'base/delete_restoran.html'

class Delete_meal(DeleteView):
    model = Meal
    success_url = reverse_lazy('home')
    template_name = 'base/delete_restoran.html'

class Delete_menu(DeleteView):
    model = Menu
    success_url = reverse_lazy('home')
    template_name = 'base/delete_restoran.html'

def edit_meal(request, pk):
    meal_instance = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = EditMealForm(data=request.POST, files=request.FILES, instance=meal_instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('edit_restoran', kwargs={'pk': meal_instance.menu.restoran.id}))
    else:
        form = EditMealForm(instance=meal_instance)
    return render(request, 'base/edit_meal.html', {'r': meal_instance, 'form': form})

def edit_menu(request, pk):
    menu_instance = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = EditMenuForm(data=request.POST, files=request.FILES, instance=menu_instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('edit_restoran', kwargs={'pk': menu_instance.restoran.id}))
    else:
        form = EditMenuForm(instance=menu_instance)
    return render(request, 'base/edit_meal.html', {'r': menu_instance, 'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'base/signup.html', {'form': form})
