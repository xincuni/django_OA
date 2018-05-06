# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import load_backend
from django.contrib.auth.backends import RemoteUserBackend
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from account.models import User


def get_current_user(request):
    user_id = request.session.get('user_id', None)
    if user_id:
        user = User.by_id(user_id)
        return user if user else None


def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = get_current_user(request)
    return request._cached_user


class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        请求之前
        :param request:
        :return:
        """
        request.current_user = SimpleLazyObject(lambda: get_user(request))

    # def process_response(self, request, response):
        """
        请求之后,需要返回resopnse
        """
    #     print 'data'
    #     return response
    #
