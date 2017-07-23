from django import forms
from .models import Restoran, Meal, Menu
from django.contrib.auth.models import User


class NewRestoranForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5})
    )
    owner = forms.ModelChoiceField(queryset=User.objects.all())

class NewMealForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
    )
    menu = forms.ModelChoiceField(queryset=Menu.objects.all())
    image = forms.ImageField()

class NewMenuForm(forms.Form):
    name = forms.CharField(max_length=50)
    restoran = forms.ModelChoiceField(queryset=Restoran.objects.all())

class EditMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('name', 'description', 'image')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }


class EditMenuForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

    class Meta:
        model = Menu
        fields=['name', ]

class EditRestoranForm(forms.ModelForm):
    class Meta:
        model = Restoran
        exclude = ['owner', ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }
