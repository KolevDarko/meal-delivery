from django.forms import ModelForm
from .models import Restoran, Meal, Menu


class RestoranForm(ModelForm):
    class Meta:
        model = Restoran
        exclude= []

class NewMealForm(ModelForm):
    class Meta:
        model = Meal
        exclude = []

class NewMenuForm(ModelForm):
    class Meta:
        model = Menu
        exclude = []

class EditMealForm(ModelForm):
    class Meta:
        model = Meal
        exclude = ['menu']

class EditMenuForm(ModelForm):
    class Meta:
        model = Menu
        exclude = ['restoran']
