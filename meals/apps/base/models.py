"""Base models"""
from django.db import models


class Restoran(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)

class Menu(models.Model):
    name = models.TextField(max_length=50)
    restoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)

class Meal(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    menu = models.ForeignKey(Menu, related_name='meals', on_delete=models.CASCADE)






