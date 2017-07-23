"""urlconf for the base application"""

from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^restoran$', restoran, name='restoran'),
    url(r'^restoran/add$', new_restoran, name='new_restoran'),
    url(r'^restoran/edit/(?P<pk>\d+)/$', edit_restoran, name='edit_restoran'),
    url(r'^meal/add$', new_meal, name='new_meal'),
    url(r'^menu/add$', new_menu, name='new_menu'),
    url(r'^test$', tester, name='tester'),
    url(r'^restoran/(?P<pk>\d+)/$', restoran2, name='restoran2'),
    url(r'^restoran/delete/(?P<pk>\d+)/$', Delete_restoran.as_view(), name='delete_restoran'),
    url(r'^meal/edit/(?P<pk>\d+)/$', edit_meal, name='edit_meal'),
    url(r'^meal/delete/(?P<pk>\d+)/$', Delete_meal.as_view(), name='delete_meal'),
    url(r'^menu/edit/(?P<pk>\d+)/$', edit_menu, name='edit_menu'),
    url(r'^menu/delete/(?P<pk>\d+)/$', Delete_menu.as_view(), name='delete_menu'),

    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, {'template_name': 'base/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
]
