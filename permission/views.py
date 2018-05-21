# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.views import View
from django_OA.common_fun import login_required, MyLoginRequired
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from libs import (
    premission_manage_libs
)


# Create your views here.
@login_required
def manage(request):
    roles, permissions, menus, users, handlers = premission_manage_libs()
    kw = {
        'roles': roles,
        'permission': permissions,
        'menus': menus,
        'handlers': handlers,
        'users': users,
        'dev_users': [],
        'dev_role_id': [],
    }

    # print menus ,'..............'
    return render(request, 'permission/permission_list.html',kw)
