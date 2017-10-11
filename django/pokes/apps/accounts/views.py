# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic.edit import FormView, CreateView
from .forms import SignUpForm, LoginForm, ProfileForm
from ..pokes.models import Poke


@login_required
def index(request):
    pass
    return redirect(reverse('pokes:index'))

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()
        user.profile.birthday = form.cleaned_data.get('birthday')
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        poke = Poke()
        poke.receive_user = user
        poke.counter = 0
        poke.save()
        login(self.request, user)
        return redirect(reverse('pokes:index'))


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect(reverse('pokes:index'))


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('users:profile'))
        else:
            return redirect(reverse('users:profile'))
    else:
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
