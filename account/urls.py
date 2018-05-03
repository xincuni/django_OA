# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import (UserRegiest,
                   Captcha)

urlpatterns = [
    url(r'^user_regiest/$', UserRegiest.as_view(), name='user_regiest'),
    url(r'^captcha/$', Captcha.as_view(), name='captcha'),
]
