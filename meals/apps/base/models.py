"""Base models"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Restoran(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, null=True)
    type = models.CharField(max_length=20, default='restoran')
    image = models.ImageField(upload_to="documents/", blank=True, null=True)
    city = models.CharField(max_length=30)
    free_delivery_limit = models.IntegerField(default=0)
    recomended = models.BooleanField(default=False)
    status = models.CharField(max_length=30, default='open', choices=[
        ('open', 'отворено (достава: 15-40 минути)'),
        ('busy', 'средно зафатено (достава: 30-60 минути)'),
        ('extra_busy', 'презафатен (достава: повеќе од еден час)'),
        ('closed', 'затворено'),
    ]);

    def __str__(self):
        return "{0}: {1} id:{2}".format(self.name, self.description, self.id)

    def average_rating(self):
        if self.ratings.all().count() == 0:
            return 0
        sum = 0
        for r in self.ratings.all():
            sum += r.rating
        return int((sum / self.ratings.all().count()) / 5 * 100)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    restoran = models.ForeignKey(Restoran, related_name='menus', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - restoran: {1}".format(self.name, self.restoran)


class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    menu = models.ForeignKey(Menu, related_name='meals', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="documents/", blank=True, null=True)
    price_small = models.IntegerField(default=0)
    price_large = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}: {1} - menu: {2}".format(self.name, self.description, self.menu)

    def average_rating(self):
        if self.ratings.all().count() == 0:
            return 0
        sum = 0
        for r in self.ratings.all():
            sum += r.rating
        return int((sum / self.ratings.all().count()) / 5 * 100)

    def average_rating(self):
        if self.ratings.all().count() == 0:
            return 0
        sum = 0
        for r in self.ratings.all():
            sum += r.rating
        return int((sum / self.ratings.all().count()) / 5 * 100)


class Order(models.Model):
    restoran = models.ForeignKey(Restoran, related_name='orders', on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    buyer_uid = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    special_request = models.CharField(max_length=200, default='')
    delivery = models.BooleanField(default=True)
    creation_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=25, default='unassigned', choices=[
        ('unassigned', 'Неопределена'),
        ('unapproved', 'Одбиена'),
        ('approved', 'Одобрена'),
        ('finished', 'Завршена')
    ]);

    def __str__(self):
        return self.buyer.username + " - " + self.restoran.name


class My_key_val(models.Model):
    container = models.ForeignKey(Order, related_name='meals', db_index=True)
    key = models.CharField(max_length=100, db_index=True)
    value = models.CharField(max_length=100, db_index=True)
    price = models.IntegerField(default=0, db_index=True)


class RestoranComment(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    restoran = models.ForeignKey(Restoran, related_name='comments')

    def __str__(self):
        return str.format("{0} -> {1}: {2}", self.user.username, self.restoran.name, self.text[:20]);


class MealComment(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal, related_name='comments')


class MealRating(models.Model):
    rating = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal, related_name='ratings')

    def __str__(self):
        return str.format("{0} -> {1}, {2}", self.user.username, self.meal.name, self.meal.menu.restoran.name)


class RestoranRating(models.Model):
    rating = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    user = models.ForeignKey(User)
    restoran = models.ForeignKey(Restoran, related_name='ratings')

    def __str__(self):
        return str.format("{0} -> {1}", self.user.username, self.restoran.name)
