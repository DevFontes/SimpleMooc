from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^', views.home, name='home'),
]

app_name='core'