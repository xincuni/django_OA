# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from libs import (create_captcha_img,
                  get_mobile_code_libs,
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
    """
    验证码
    """

    def get(self, request):
        getdata = request.GET.copy()
        pre_code = getdata.get('pre_code', '')
        code = getdata.get('code', '')
        img_data = create_captcha_img(pre_code, code)
        resopnse = HttpResponse(img_data, content_type='image/jpg')
        return resopnse


# class SendMoblieCode(View):
#     def get(self, request):
#         return render(request, 'account/text.html')
#
#     def post(self, request):
#         # return HttpResponse('ok')
#         postdata = request.POST.copy()
#         print 'dsad'
#         mobile = postdata.get('mobile', '')
#         code = postdata.get('code', '')
#         captcha = postdata.get('captcha', '')
#         print locals()
#         return JsonResponse({'status': 200, 'mes': u'ok'})


def send_mobile_code(request):
    """
    发送邮件
    :param request:
    :return:
    """
    if request.method == "POST":
        postdata = request.POST.copy()
        mobile = postdata.get('mobile', '')
        code = postdata.get('code', '')
        captcha = postdata.get('captcha', '')

        get_mobile_code_libs(mobile, code, captcha)

        print mobile, code, captcha
        return JsonResponse({'status': 200, 'msg': mobile})
