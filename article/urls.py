# -*- coding: utf-8 -*-
from django.conf.urls import url

from article.views import (
    article_list,
add_article,
add_category_tag
)

urlpatterns = [
    url(r'^article_list/$', article_list, name='article_list'),
    url(r'^addarticle/$', add_article, name='add_article'),
    url(r'^add_category_tag/$', add_category_tag, name='add_category_tag'),
]