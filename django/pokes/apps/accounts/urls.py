# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib.auth.urls import *
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView, FormView
from views import SignUpView, LoginView
from forms import SignUpForm, LoginForm
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', SignUpView.as_view(template_name='register.html', form_class=SignUpForm, success_url='/'), name='register'),
    url(r'^login/$', LoginView.as_view(template_name='login.html', form_class=LoginForm, success_url='/'), name='login'),
    url(r'^edit/$', views.update_profile, name='profile'),
]
