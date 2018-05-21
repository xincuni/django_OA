# -*- coding: utf-8 -*-
from django.conf.urls import url

from article.views import (
    article_list,
    add_article,
    add_category_tag,
    article,
    add_comment,
    add_second_comment,
    add_like,
    article_delete,
    article_modify_list,
    article_modift,
)

urlpatterns = [
    url(r'^article_list/$', article_list, name='article_list'),
    url(r'^addarticle/$', add_article, name='add_article'),
    url(r'^add_category_tag/$', add_category_tag, name='add_category_tag'),
    url(r'^article/$', article, name='article'),
    url(r'^add_comment/$', add_comment, name='add_comment'),
    url(r'^add_second_comment/$', add_second_comment, name='add_second_comment'),
    url(r'^add_like/$', add_like, name='add_like'),
    url(r'^article_modify_list/$', article_modify_list, name='article_modify_list'),
    url(r'^article_delete/$', article_delete, name='article_delete'),
    url(r'^article_modify/$', article_modift, name='article_modift'),
]
