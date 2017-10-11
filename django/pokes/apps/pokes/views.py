# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponse, redirect, render
from .models import *

@login_required
def index(request):
    # Queries and context
    title = 'Poke All Teh People'
    me = request.user
    my_pokes = Poke.objects.filter(receive_user=me)
    all_pokes = Poke.objects.filter(send_user=me)
    all_users_but_me = User.objects.all().exclude(id=me.id)

    all_received_users = []
    for each in all_pokes:
        all_received_users.append(each.receive_user)

    all_no_pokes_received_users = []
    for each in all_users_but_me:
        if each not in all_received_users:
            all_no_pokes_received_users.append(each)
        
    context = {
        'title': title,
        'pokes_list': all_pokes,
        'my_pokes_list': my_pokes,
        'all_users_list': all_users_but_me,
        'no_pokes_list': all_no_pokes_received_users,
    }

    return render(request, 'dashboard.html', context=context)

def add_poke(request, user_id):
    me = request.user
    all_pokes = Poke.objects.all()
    send_user = User.objects.get(id=me.id)
    receive_user = User.objects.get(id=user_id)

    try:
        # for each in all_pokes:
        #     if each.send_user == me and each.receive_user == receive_user:
        #         each.counter += 1
        #         each.save()
        find_user = Poke.objects.filter(receive_user=receive_user).filter(send_user=send_user).order_by('-counter')[0]
        find_user.counter += 1
        find_user.save()
    except:
        find_user = Poke(receive_user=receive_user, send_user=me)
        find_user.counter += 1
        find_user.save()
        # poke = Poke()
        # poke.send_user = send_user
        # poke.receive_user = receive_user
        # poke.counter += 1
        # poke.save()
    return redirect('/')
