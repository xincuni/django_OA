# -*- coding: utf-8 -*-
from random import randint
from utils.captcha.captcha import create_captcha
from public_libs.yun_tong_xun.yun_tong_xun import sendTemplateSMS
from public_libs.redis_conn.redis_conn import conn
from models import User
from datetime import datetime


def create_captcha_img(pre_code, code):
    """图形验证码"""
    text, img = create_captcha()
    if pre_code:
        conn.delete('captcha:%s' % pre_code)
    conn.setex('captcha:%s' % code, text.lower(), 60)
    return img


def get_mobile_code_libs(mobile, code, captcha):
    """手机验证码"""
    print conn.get(('captcha:%s' % code).lower())
    print captcha
    if conn.get(('captcha:%s' % code).lower()) != captcha.lower():
        return {'status': False, 'meg': u'验证码错误'}
    mobile_code = randint(1000, 9999)
    conn.setex('mobile:%s' % mobile, mobile_code, 120)
    print '手机验证码', mobile_code
    return {'status': True}

    # sendTemplateSMS(mobile, [mobile_code, 30], 1)


def regiest(request, mobile, name, mobile_captcha, code, captcha, password1, password2):
    if mobile == '' or name == '':
        return {'status': False, 'msg': '参数不能为空'}

    if conn.get("captcha:%s" % code) != captcha.lower() or \
                    conn.get("mobile_code:%s" % mobile) != mobile_captcha:
        return {'status': False, 'msg': '验证码不正确'}

    if User.by_name(name) is not None:
        return {'status': False, 'msg': '用户已经存在'}

    if password1 != password2:
        return {'status': False, 'msg': '两次密码不一致'}

    user = User()
    user.name = name
    user.password = password1
    user.mobile = mobile
    user.save()
    return {'status': True, 'msg': '注册成功'}


def login(request, name, password, remember):
    if name == '' and password == '':
        return {'status': False, 'msg': '请输入用户名密码'}
    user = User.by_name(name)
    if user is None:
        return {'status': False, 'msg': '用户不存在'}
    if user.auth_password(password) is True:
        user.last_login = datetime.now()
        user.loginnum += 1
        user.save()
        request.session['user_id'] = user.id
        if remember == 'remember':
            request.session.set_expiry(None)
        else:
            request.session.set_expiry(1800)

        return {'status': True, 'msg': '登录成功', 'user': user}
    return {'status': False, 'msg': '密码输入错误'}


def auth_captche(captcha_code, code):
    """
    图形验证码
    :param captcha_code:
    :param code:
    :return:
    """
    if captcha_code == '' or code == '':
        return {'status': False, 'msg': u'验证码错误'}
    if conn.get(('captcha:%s' % code).lower()) != captcha_code.lower():
        return {'status': False, 'msg': u'验证码错误'}
    return {'status': True, 'msg': ''}
