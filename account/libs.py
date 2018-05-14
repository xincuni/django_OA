# -*- coding: utf-8 -*-
from random import randint
from random import randint, choice
from string import printable
from uuid import uuid4
import json
import traceback
from utils.captcha.captcha import create_captcha
from public_libs.yun_tong_xun.yun_tong_xun import sendTemplateSMS
from public_libs.send_email.send_email_libs import send_qq_html_email
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


def edit_profile(request, name, password):
    """
    修改用户信息
    :param request:
    :param name:
    :param password:
    :return:
    """
    if name == '':
        return {'status': False, 'msg': '缺少用户名'}
    if password == '':
        return {'status': False, 'msg': '缺少密码'}
    user = request.current_user
    user.username = name
    user.password = password
    user.update_time = datetime.now()
    user.save()
    return {'status': True, 'msg': '修改成功'}


def bind_email_libs(request, email):
    # send_qq_html_email('40308351@qq.com', [email], u'联系', u'你好')
    # pass
    # return {'status': True, 'msg': '发送ok'}
    email = email.encode('utf-8')
    if email:
        ttl = conn.ttl('email:%s' % email)
        if ttl is not None:
            return {"status": True, "msg": '邮件发送了，过%s秒在发送' % str(ttl)}
        # #生成验证码
        email_code = ''.join([choice(printable[:62]) for i in xrange(4)])
        u = str(uuid4())
        text_dict = {
            'email_code': email_code,
            u: request.current_user.id
        }
        redis_text = json.dumps(text_dict)
        content = """
             <p>html邮件格式练习</p>
              <p><a href="http://127.0.0.1:8000/account/auth_email_code?code={}&email={}&current={}">
              点击链接验证
              href="http://127.0.0.1:8000/account/auth_email_code
              </a></p>
            """.format(email_code, email, u)
        send_qq_html_email('40308351@qq.com', [email], u'Django练习', content)
        print '邮箱验证码是', email
        conn.setex('email:%s' % email, redis_text, 120)
        return {"status": True, "msg": '邮件发送成功'}
    return {"status": False, "msg": '没有邮箱'}


def auth_email_code_libs(request, emial_code, email, current):
    """
    验证邮箱
    :param request:
    :param emial_code:
    :param email:
    :param current:
    :return:
    """
    redis_text = conn.get('email:%s' % email)
    if redis_text is not None:
        text_dict = json.loads(redis_text)
        print '-------------------------'
        print text_dict
        if text_dict and text_dict['email_code'] == emial_code:
            # user = request.current_user
            # print user
            # if user is None:
            user = User.by_id(text_dict[current])  # text_dict['seifjalsjgiae']
            # print user
            user.email = email
            user.update_time = datetime.now()
            user.save()
            return {'status': True, 'msg': "邮箱修改成功"}
        return {'status': False, 'msg': "验证码错误"}
    else:
        return {'status': False, 'msg': "邮箱不正确或者验证码已经过期"}


def add_avatar_libs(request, avatar):
    """
    头像上传
    :param request:
    :param avatar:
    :return:
    """
    if avatar.multiple_chunks(chunk_size=None) is True:
        return {'status': False, 'msg': "头像图片要求小于2兆"}
    try:

        user = request.current_user
        user.avatar = avatar.read()
        user.update_time = datetime.now()
        user.save()
        return {'status': True, 'msg': '图片上传成功'}
    except Exception as e:
        print e
        send_qq_html_email('40308351@qq.com', ['40308351@qq.com'], u'django_error',
                           traceback.format_exc().replace('\n', '</br>'))
        return {'status': False, 'msg': e}
