# -*- coding: utf-8 -*-
from django.views import View
from functools import wraps
from django.shortcuts import redirect, reverse
import urllib
from django.contrib.auth.mixins import LoginRequiredMixin


def get_userid(request):
    user_id = request.session.get('user_id', None)
    return user_id


# def login_required(method):
#     @wraps(method)
#     def wrapper(request, *args, **kwargs):
#         rel = get_userid(request)
#         if not rel:
#             url = reverse('account:UserLogin') + '?next=' + urllib.quote(request.get_full_path())
#             print urllib.quote(request.get_full_path())
#             return redirect(url)
#         return method(request, *args, **kwargs)
#
#     return wrapper
def login_required(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id', ''):
            url = reverse('account:UserLogin')+'?next='+ urllib.quote(request.get_full_path())
            return redirect(url)
        return method(request, *args, **kwargs)
    return wrapper


class MyLoginRequired(LoginRequiredMixin, View):
    login_url = '/account/user_login'
    redirect_field_name = ''
