# -*- coding: utf-8 -*-

from utils.captcha.captcha import create_captcha


def create_captcha_img(pre_code, code):
    text, img = create_captcha()
    return img
