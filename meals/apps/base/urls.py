"""urlconf for the base application"""

from django.conf.urls import url

from .views import home, restoran


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^restoran$', restoran, name='restoran'),
]
