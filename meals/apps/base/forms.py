from django import forms
from .models import *
from django.contrib.auth.models import User



RESTORAN_TYPE_CHOICES = (
    ('restoran', 'Ресторан'),
    ('picerija', 'Пицерија'),
    ('burekcilnica', 'Бурекчилница'),
    ('sendvicara', 'Сендвичара')
)

CITIES = (
    ('Кочани', 'Кочани'),
    ('Штип', 'Штип'),
    ('Виница', 'Виница'),
)

class NewRestoranForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5})
    )
    owner = forms.ModelChoiceField(queryset=User.objects.all())
    type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RESTORAN_TYPE_CHOICES,
    )
    image = forms.ImageField()

class NewMealForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
    )
    price = forms.IntegerField()
    menu = forms.ModelChoiceField(queryset=Menu.objects.all())
    image = forms.ImageField()

class NewMenuForm(forms.Form):
    name = forms.CharField(max_length=50)
    #restoran = forms.ModelChoiceField(queryset=Restoran.objects.all())

class EditMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('name', 'description', 'image', 'price')
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
        fields = ['description', 'image', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }

class OrderForm(forms.ModelForm):

    special_request = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        )

    class Meta:
        model = Order
        fields = ['address', 'phone', 'special_request', 'delivery']


class PickCityForm(forms.Form):
    city = forms.ChoiceField(
        choices=CITIES,
    )
