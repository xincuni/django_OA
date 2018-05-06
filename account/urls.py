# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import (UserRegiest,
                   send_mobile_code,
                   UserLogin,
                   Profile,
                   logout,
                   user_edit,
                   bind_user_email,
                   Captcha)

urlpatterns = [
    url(r'^user_regiest/$', UserRegiest.as_view(), name='user_regiest'),
    url(r'^captcha/$', Captcha.as_view(), name='captcha'),
    # url(r'^send_moblie_code/$', SendMoblieCode.as_view(), name='send_mobile_code'),
    url(r'^send_mobile_code/$', send_mobile_code, name='send_mobile_code'),
    url(r'^user_login/$', UserLogin.as_view(), name='UserLogin'),
    url(r'^profile/$', Profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^user_edit/$', user_edit, name='user_edit'),
    url(r'^bind_user_email/$', bind_user_email, name='bind_user_email'),
]
