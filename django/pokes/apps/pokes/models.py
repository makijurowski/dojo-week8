# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Poke(models.Model):
    send_user = models.ForeignKey(User, related_name='send_user', blank=True, null=True)
    receive_user = models.ForeignKey(User, verbose_name='Alias', related_name='receive_user', blank=True, null=True)
    counter = models.IntegerField(verbose_name='Poke History', blank=True, null=True, default=0)

    def __unicode__(self):
        try:
            message = "Poke from {0} to {1}".format(self.send_user.username, self.receive_user.username)
        except:
            message = "No pokes for {0}".format(self.receive_user.username)
        return message

    def receive_user_name(self):
        name = self.receive_user.first_name
        return name
