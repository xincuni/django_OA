# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from libs import (create_captcha_img
                  )


# Create your views here.
class UserRegiest(View):
    """
    用户注册
    """

    def get(self, request):
        # return HttpResponse(u'ok')
        return render(request, 'account/auth_regist.html')


class Captcha(View):
    def get(self, request):
        getdata = request.GET.copy()
        pre_code = getdata.get('pre_code', '')
        code = getdata.get('code', '')
        img_data = create_captcha_img(pre_code, code)
        resopnse = HttpResponse(img_data, content_type='image/jpg')
        return resopnse