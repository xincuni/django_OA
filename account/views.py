# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.views import View
from django_OA.common_fun import login_required, MyLoginRequired
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from libs import (create_captcha_img,
                  get_mobile_code_libs,
                  regiest,
                  login,
                  edit_profile,
                  bind_email_libs,
                  auth_captche, )


# Create your views here.
class UserRegiest(View):
    """
    用户注册
    """

    def get(self, request):
        # return HttpResponse(u'ok')
        return render(request, 'account/auth_regist.html')

    def post(self, request):
        postdata = request.POST.copy()
        mobile = postdata.get('mobile', '')
        name = postdata.get('name', '')
        module_captcha = postdata.get('module_captcha', '')
        code = postdata.get('code', '')
        captcha = postdata.get('captcha', '')
        password1 = postdata.get('password1', '')
        password2 = postdata.get('password2', '')

        result = regiest(request, mobile, name, module_captcha, code, captcha, password1, password2)
        if result['status'] is False:
            kw = {'message': result['msg']}
            return render(request, 'account/auth_regist.html', kw)
        else:
            return redirect('/account/user_login/')


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

        rel = get_mobile_code_libs(mobile, code, captcha)
        print rel
        print type(rel)
        if rel['status'] is False:
            return JsonResponse({'status': 400, 'msg': rel['meg']})
        return JsonResponse({'status': 200, 'msg': mobile})


class UserLogin(View):
    """
    用户登录
    """

    def get(self, request):
        next = request.GET.get('next', '')
        kw = {'next': next if next else '/account/profile'}
        return render(request, 'account/auth_login.html', kw)

    def post(self, request):
        postdata = request.POST.copy()
        name = postdata.get('name', '')
        password = postdata.get('password', '')
        code = postdata.get('code', '')
        captcha_code = postdata.get('captcha', '')
        remember = postdata.get('remember', '')

        result = auth_captche(captcha_code, code)
        if result['status'] is False:
            return JsonResponse({'status': 400, 'msg': result['msg']})

        result = login(request, name, password, remember)
        if result['status'] is False:
            return JsonResponse({'status': 400, 'msg': result['msg']})
        else:
            if result['user'].loginnum == 1:
                return JsonResponse({'status': 200, 'msg': '你好新用户'})
            else:
                return JsonResponse({'status': 200, 'msg': result['msg']})


# class Profile(MyLoginRequired, View):
#     """
#     用户主页
#     """
#
#     # @login_required
#     def get(self, request):
#         return render(request, 'account/account_profile.html')


@login_required
def Profile(request):
    """
    用户登录后显示个人主页
    :param request:
    :return:
    """
    return render(request, 'account/account_profile.html')


@login_required
def logout(request):
    """
    登出函数
    :param request:
    :return:
    """
    request.session.flush()
    return redirect(reverse('account:UserLogin'))


@login_required
def user_edit(request):
    """
    用户个人中心修改
    :param request:
    :return:
    """
    if request.method == "POST":
        postdata = request.POST.copy()
        name = postdata.get('name', '')
        password = postdata.get('password', '')
        result = edit_profile(request, name, password)
        kw = {'message': result['msg']}
        if result['status'] is False:
            return render(request, 'account/account_edit.html', kw)
        return render(request, 'account/account_edit.html', kw)
    return render(request, 'account/account_edit.html')


@login_required
def bind_user_email(request):
    if request.method == "POST":
        postdata = request.POST.copy()
        email = postdata.get('email', '')
        result = bind_email_libs(request, email)
        kw = {'message': result['msg']}
        if result['status'] is False:
            return HttpResponse(result['msg'])
        return HttpResponse(result['msg'])

    return render(request, 'account/account_bind_email.html')
