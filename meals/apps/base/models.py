"""Base models"""
from django.db import models


class Restoran(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return "{0}: {1} id:{2}".format(self.name, self.description, self.id)


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

    def __str__(self):
        return "{0}: {1} - menu: {2}".format(self.name, self.description, self.menu)
