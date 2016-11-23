from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^winepage/$', views.wine_page, name='wine_page'),
]