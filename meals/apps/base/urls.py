"""urlconf for the base application"""

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^restoran$', restoran, name='restoran'),
    url(r'^restoran/add$', new_restoran, name='new_restoran'),
    url(r'^meal/add$', new_meal, name='new_meal'),
    url(r'^menu/add$', new_menu, name='new_menu'),
    url(r'^test$', tester, name='tester'),
    url(r'^restoran2/(?P<pk>\d+)/$', restoran2)
]
