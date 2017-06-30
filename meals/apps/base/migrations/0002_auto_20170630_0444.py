# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='restoran',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
