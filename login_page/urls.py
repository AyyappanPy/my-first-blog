from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login_page/$', views.login_page, name='login_page'),
]