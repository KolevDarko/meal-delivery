from django.forms import ModelForm
from .models import Restoran, Meal, Menu


class RestoranForm(ModelForm):
    class Meta:
        model = Restoran
        exclude= []

class MealForm(ModelForm):
    class Meta:
        model = Meal
        exclude = []

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        exclude = []
