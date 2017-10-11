# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

import django_tables2 as tables

class Trip(models.Model):
    """
    This model defines a trip for user travels. Includes destination, plans, dates of travel.
    """
    destination = models.CharField(max_length=200)
    plans = models.CharField(max_length=200)
    travel_from = models.DateField(
        verbose_name='Departure Date', blank=True, null=True)
    travel_to = models.DateField(
        verbose_name='Arrival Date', blank=True, null=True)
    travelers = models.ManyToManyField('Traveler', through='Trip_Travelers', blank=True)
    created_at = models.DateTimeField(
        verbose_name='Date Added', default=timezone.now)
    updated_at = models.DateTimeField(
        verbose_name='Last Updated', blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def get_absolute_url(self):
         """Returns the url to access a particular instance of a Trip."""
         return reverse('trip_detail', args=[str(self.id)])

    def __str__(self):
        """String representing the Trip object."""
        return self.destination

class Traveler(models.Model):
    """ 
    This model defines a traveler. Includes user and their trips.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    trips = models.ManyToManyField('Trip', through='Trip_Travelers', blank=True)
    created_at = models.DateTimeField(verbose_name='Date Added', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Last Updated', blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ["user"]


class Trip_Travelers(models.Model):
    """
    This model connects the models for Trip and Travelers through a many-to-many relationship.
    """
    trip = models.ForeignKey('Trip')
    traveler = models.ForeignKey('Traveler')

    class Meta:
        ordering = ["trip"]
