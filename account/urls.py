# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import (UserRegiest,
                   send_mobile_code,SendMoblieCode,
                   Captcha)

urlpatterns = [
    url(r'^user_regiest/$', UserRegiest.as_view(), name='user_regiest'),
    url(r'^captcha/$', Captcha.as_view(), name='captcha'),
    # url(r'^send_moblie_code/$', SendMoblieCode.as_view(), name='send_mobile_code'),
    url(r'^send_mobile_code/$', send_mobile_code, name='send_mobile_code'),
]
