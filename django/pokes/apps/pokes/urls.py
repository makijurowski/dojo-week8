# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib.auth.urls import *
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^poke/(?P<user_id>\d+)$', views.add_poke, name='add'),
]
