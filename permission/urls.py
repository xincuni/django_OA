# -*- coding: utf-8 -*-
from django.conf.urls import url
from permission import views

urlpatterns = [
    url(r'^manage/', views.manage, name='manege'),
]
