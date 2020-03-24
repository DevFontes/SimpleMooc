from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^', views.index, name='index'),
]

app_name='courses'