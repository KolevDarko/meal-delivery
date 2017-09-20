"""Views for the base app"""
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *
from django.views.generic.edit import DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .helper_objects import Cart

def home(request):
    user = request.user

    if user.is_anonymous:
        return redirect('login')

    else:
        if user.groups.filter(name='owners').exists():
            restoran = Restoran.objects.get(owner=user)
            return redirect('edit_restoran', pk=restoran.id)
        else:
            if 'city' in request.session:
                """ Default view for the root """
                city = request.session["city"]
                restorans_all = Restoran.objects.filter(city=city)
                restorani = restorans_all.filter(type='restoran')
                picerii = restorans_all.filter(type='picerija')
                burekcilnici = restorans_all.filter(type='burekcilnica')
                sendvicari = restorans_all.filter(type='sendvicara')

                return render(request, 'base/home.html',
                              {
                                  'restorans_all': restorans_all,
                                  'lista_restorani': restorani,
                                  'lista_picerii': picerii,
                                  'lista_burekcilnici': burekcilnici,
                                  'lista_sendvicari': sendvicari,
                                  'city': city,
                              })
            else:
                return redirect('pick_city')

def pick_city(request):
        if request.method == 'POST':
            form = PickCityForm(data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                request.session['city'] = data['city']
                return redirect('home')
        else:
            form = PickCityForm()
            return render(request, 'base/pick_city.html', {'form': form})

def restoran(request):
    if 'city' in request.session:
        city = request.session["city"]
        restorans_all = Restoran.objects.filter(city=city)
    else:
        restorans_all = Restoran.objects.all();

    restorani = restorans_all.filter(type='restoran')
    picerii = restorans_all.filter(type='picerija')
    burekcilnici = restorans_all.filter(type='burekcilnica')
    sendvicari = restorans_all.filter(type='sendvicara')


    return render(request, 'base/restoran.html', {
        'lista_restorani': restorani,
        'lista_picerii': picerii,
        'lista_burekcilnici': burekcilnici,
        'lista_sendvicari': sendvicari,
    })

def new_restoran(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = NewRestoranForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                restoran = Restoran(name=data['name'], description=data['description'], owner=data['owner'],
                                    type=data['type'], image=data['image'])
                restoran.save()
                return redirect('restoran2', pk=restoran.pk)
        else:
            form = NewRestoranForm()
        return render(request, 'base/add_item.html', {'type': 'Restoran', 'form': form})
    else:
        return redirect('home')

def new_meal(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            form = NewMealForm(data=request.POST, files=request.FILES)
            form.fields["menu"].queryset = Menu.objects.all().filter(restoran=Restoran.objects.get(owner=request.user))
            if form.is_valid():
                data = form.cleaned_data
                meal = Meal(name=data['name'], description=data['description'], price=data['price'], menu=data['menu'], image=data['image'])
                meal.save()
                return redirect('restoran2', pk=meal.menu.restoran.pk)
        else:
            form = NewMealForm()
            form.fields["menu"].queryset = Menu.objects.all().filter(restoran=Restoran.objects.get(owner=request.user))
        return render(request, 'base/add_meal.html', {'type': 'Meal', 'form': form})
    else:
        return redirect('home')

def new_menu(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            form = NewMenuForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                menu = Menu(name=data['name'], restoran=Restoran.objects.get(owner=request.user))
                menu.save()
                return redirect('restoran2', pk=menu.restoran.pk)
        else:
            form = NewMenuForm()
        return render(request, 'base/add_item.html', {'type': 'Menu', 'form': form})
    else:
        return redirect('home')

def edit_restoran(request, pk):
    restoran_instance = get_object_or_404(Restoran, pk=pk)
    if restoran_instance.owner == request.user or request.user.is_superuser:
        if request.method == 'POST':

            for menu in restoran_instance.menus.all():
                for meal in menu.meals.all():
                    meal.is_active = False;
                    meal.save()
            for key in request.POST:
                if 'is_active' in key:
                    meal_id = int(request.POST[key])
                    meal = Meal.objects.get(pk=meal_id)
                    meal.is_active = True
                    meal.save()

            form = EditRestoranForm(data=request.POST, files=request.FILES, instance=restoran_instance)
            if form.is_valid():
                form.save()
                # return redirect(reverse('restoran2', kwargs={'pk': pk}))
        else:
            form = EditRestoranForm(instance=restoran_instance)
        return render(request, 'base/edit_restoran.html', {'r': restoran_instance, 'form': form})
    else:
        return redirect('home')

def tester(request):
    cart = request.session.get('cart', Cart)
    return render(request, 'base/tester.html', {'items': cart.items})

def restoran2(request, pk):
    r = get_object_or_404(Restoran, pk=pk)
    comments = RestoranComment.objects.all().filter(restoran=r)
    if 'cart_restoran_name' in request.session:
        if request.session['cart_restoran_name'] != r.name:
            request.session['cart'] = {}
            request.session['cart_restoran_name'] = r.name
    if request.method == 'POST':
        #new comment
        if 'comment_text' in request.POST:
            if len(request.POST['comment_text']):
                comment = RestoranComment(text=request.POST['comment_text'], restoran=r, user=request.user)
                comment.save()

        #if restoran is rated
        elif 'star' in request.POST:
            rating = int(request.POST['star'])
            if RestoranRating.objects.filter(user=request.user, restoran=r).count():
                r = RestoranRating.objects.get(user=request.user, restoran=r)
                r.rating = rating
            else:
                r = RestoranRating(user=request.user, restoran=r, rating=rating)
            r.save()

        else:
            if 'cart_restoran_name' in request.session:
                if request.session['cart_restoran_name'] != r.name:
                    request.session['cart'] = {}
                    request.session['cart_restoran_name'] = r.name
            else:
                request.session['cart'] = {}
                request.session['cart_restoran_name'] = r.name

            form = forms.Form(data=request.POST)
            if form.is_valid():
                meal_id = request.POST['meal_id']
                quantity = request.POST['quantity']
                cart = request.session['cart']
                cart[meal_id] = quantity
                request.session['cart'] = cart

    if 'city' in request.session:
        city = request.session["city"]
        restorans_all = Restoran.objects.filter(city=city)
    else:
        restorans_all = Restoran.objects.all()

    restorani = restorans_all.filter(type='restoran')
    picerii = restorans_all.filter(type='picerija')
    burekcilnici = restorans_all.filter(type='burekcilnica')
    sendvicari = restorans_all.filter(type='sendvicara')
    current_rating = 0

    if RestoranRating.objects.filter(user=request.user, restoran=r).count():
        rat = RestoranRating.objects.get(user=request.user, restoran=r)
        current_rating = rat.rating

    if 'cart_restoran_name' in request.session and 'cart' in request.session:
        cart_restoran_name = request.session['cart_restoran_name']
        cart = request.session['cart'];
    else:
        return render(request, 'base/restoran_2.html', context={
            'r': r,
            'lista_restorani': restorani,
            'lista_picerii': picerii,
            'lista_burekcilnici': burekcilnici,
            'lista_sendvicari': sendvicari,
            'current_rating': current_rating,
            'comments': comments,
            'sum': 0,
        });

    if len(cart) == 0:
        return render(request, 'base/restoran_2.html', context={
            'r': r,
            'lista_restorani': restorani,
            'lista_picerii': picerii,
            'lista_burekcilnici': burekcilnici,
            'lista_sendvicari': sendvicari,
            'current_rating': current_rating,
            'comments': comments,
            'sum': 0,
        });


    meals = []
    sum = 0
    for key, value in cart.items():
        meal = Meal.objects.get(pk=key)
        meals.append((meal, value))
        sum += int(value) * meal.price


    return render(request, 'base/restoran_2.html', context={
        'r': r,
        'lista_restorani': restorani,
        'lista_picerii': picerii,
        'lista_burekcilnici': burekcilnici,
        'lista_sendvicari': sendvicari,
        'current_rating': current_rating,
        'meals': meals,
        'sum': sum,
        'cart_restoran_name': cart_restoran_name,
        'comments': comments,
        })

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
    return render(request, 'base/edit_menu.html', {'r': menu_instance, 'form': form})

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

def show_cart(request):
    if 'cart_restoran_name' in request.session and 'cart' in request.session:
        restoran_name = request.session['cart_restoran_name']
        cart = request.session['cart'];
    else:
        return render(request, 'base/show_cart.html', {'restoran_name': 'Кошничката е празна'})

    if len(cart) == 0:
        return render(request, 'base/show_cart.html', {'restoran_name': 'Кошничката е празна'})

    # if request.method == 'POST':
    #     user = request.user
    #     uid = user.social_auth.get(provider='facebook').uid
    #     restoran = Restoran.objects.get(name=restoran_name)
    #     order = Order(restoran=restoran, buyer=user, buyer_uid=uid)
    #     order.save()
    #     for key, value in cart.items():
    #         pair = My_key_val(container=order, key=key, value=value)
    #         pair.save()
    #     request.session['cart'] = {}
    #     cart = {}

    meals = []
    sum = 0
    for key, value in cart.items():
        meal = Meal.objects.get(pk=key)
        meals.append((meal, value))
        sum += int(value) * meal.price

    return render(request, 'base/show_cart.html', {
        'meals': meals,
        'sum': sum,
        'restoran_name': restoran_name,
    })

def make_order(request):
    restoran_name = request.session['cart_restoran_name']
    cart = request.session['cart'];

    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            uid = user.social_auth.get(provider='facebook').uid
            restoran = Restoran.objects.get(name=restoran_name)
            order = Order(restoran=restoran, buyer=user, buyer_uid=uid, address=data['address'],
                          phone=data['phone'], delivery=data['delivery'], special_request=data['special_request'])
            order.save()
            for key, value in cart.items():
                pair = My_key_val(container=order, key=key, value=value)
                pair.save()
            request.session['cart'] = {}
            return redirect('my_orders')
    else:
        form = OrderForm()
    return render(request, 'base/make_order.html', {'form': form})

def orders_for_restoran(request, pk):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = Order.objects.get(pk=order_id);
        if '_approve' in request.POST:
            order.status = 'approved'
        elif '_cancel' in request.POST:
            order.status = 'unapproved'
        order.save()

    restoran = get_object_or_404(Restoran, pk=pk)
    orders = Order.objects.filter(restoran=restoran, status='unassigned')

    items = []
    for order in orders:
        key_vals = My_key_val.objects.filter(container=order)
        meals_in_order = []
        total_price = 0
        for key_val in key_vals:
            meal = Meal.objects.get(id=key_val.key)
            meal_name = meal.name
            total_price += meal.price * int(key_val.value)
            meals_in_order.append((meal_name, key_val.value))
        items.append((order, meals_in_order, total_price))


    return render(request, 'base/orders_for_restoran.html', {'items': items})

def approved_orders_for_restoran(request, pk):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = Order.objects.get(pk=order_id);
        order.status = 'finished'
        order.save()


    restoran = get_object_or_404(Restoran, pk=pk)
    orders = Order.objects.filter(restoran=restoran, status='approved')

    items = []
    for order in orders:
        key_vals = My_key_val.objects.filter(container=order)
        meals_in_order = []
        total_price = 0
        for key_val in key_vals:
            meal = Meal.objects.get(id=key_val.key)
            meal_name = meal.name
            total_price += meal.price * int(key_val.value)
            meals_in_order.append((meal_name, key_val.value))
        items.append((order, meals_in_order, total_price))

    return render(request, 'base/approved_orders_for_restoran.html', {'items': items})

def orders_for_user(request):
    comments_display = 'none'
    comments = ''
    comment_meal_id = ''
    if request.method == 'POST':
        if 'star' in request.POST:
            m = Meal.objects.get(pk=request.POST['meal_id'])
            rating = int(request.POST['star'])
            if MealRating.objects.filter(user=request.user, meal=m).count():
                r = MealRating.objects.get(user=request.user, meal=m)
                r.rating = rating
            else:
                r = MealRating(user=request.user, meal=m, rating=rating)
            r.save()
        elif 'show_comments' in request.POST:
            comments_display = 'block'
            meal = Meal.objects.get(pk=request.POST['meal_id'])
            comments = MealComment.objects.all().filter(meal=meal)
            comment_meal_id = meal.id
        elif 'comment_text' in request.POST:
            meal = Meal.objects.get(pk=request.POST['meal_id'])
            comment = MealComment(text=request.POST['comment_text'], meal=meal, user=request.user)
            comment.save()
            comments_display = 'block'
            comments = MealComment.objects.all().filter(meal=meal)


    orders = Order.objects.filter(buyer=request.user)
    items = []
    for order in orders:
        key_vals = My_key_val.objects.filter(container=order)
        meals_in_order = []
        total_price = 0
        for key_val in key_vals:
            meal = Meal.objects.get(id=key_val.key)
            meal_name = meal.name
            total_price += meal.price * int(key_val.value)
            meals_in_order.append((meal_name, key_val.value, key_val.key))
        items.append((order, meals_in_order, total_price))

    items = list(reversed(items))

    return render(request, 'base/orders_for_user.html', {
        'items': items,
        'comments_display': comments_display,
        'comments': comments,
        'comment_meal_id': comment_meal_id,
    })

def order_details(request, pk):
    return 0

