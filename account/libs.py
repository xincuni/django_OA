# -*- coding: utf-8 -*-
from random import randint
from utils.captcha.captcha import create_captcha
from public_libs.yun_tong_xun.yun_tong_xun import sendTemplateSMS


def create_captcha_img(pre_code, code):
    text, img = create_captcha()
    return img


def get_mobile_code_libs(mobile, code, captcha):
    mobile_code = randint(1000, 9999)
    # sendTemplateSMS(mobile, [mobile_code, 30], 1)
