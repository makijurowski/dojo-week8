# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Alias', max_length=30, required=True, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Name', max_length=30, required=False, help_text='Optional.',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email address.',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=30, required=True, help_text='Required.',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', max_length=30, required=True, help_text='Required.',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='Birthday', required=False, help_text='Optional. Format: MM-DD-YYYY',
                                 widget=forms.DateInput(format="%m/%d/%Y", attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2', 'birthday')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", max_length=30,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(label='Birthday', required=False, help_text='Optional. Format: MM-DD-YYYY', widget=forms.DateInput(format="%m/%d/%Y", attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Profile
        fields = ('birthday',)
