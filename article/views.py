# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from django_OA.common_fun import login_required

from libs import (add_catgory_libs,
                  article_get_catgorys_tags_lib,
                  get__article_libs,
                  add_article_libs,
                  add_comment_lib,
                  add_second_comment_lib,
                  add_like_lib,
                  article_lib,
                  article_modify_list_lib,
                  article_get_lib,
                  article_delete_lib, )


# Create your views here.
@login_required
def article_list(request):
    """
    文档首页
    :param request:
    :return:
    """
    articles, comments = get__article_libs()
    catgorys, tags = article_get_catgorys_tags_lib()
    kw = {
        'categorys': catgorys,
        'tags': tags,
        'articles': articles,
        'newarticles': articles[:3],
        'newcomments': comments[:3],
    }
    return render(request, 'article/article_list.html', kw)


@login_required
def add_article(request):
    """
    添加文章
    :param request:
    :return:
    """
    if request.method == 'POST':
        postdata = request.POST.copy()
        title = postdata.get('title', '')
        article_content = postdata.get('article', '')
        category = postdata.get('category', '')
        tags = postdata.get('tags', '')
        article_id = postdata.get('article_id', '')
        desc = postdata.get('desc', '')
        thumbnail = postdata.get('thumbnail', '')
        result = add_article_libs(request, title, article_content, category, tags, article_id, desc, thumbnail)
        if result['status'] is True:
            return JsonResponse({
                'status': 200,
                'msg': result['msg']
            })
        return JsonResponse({
            'status': False,
            'msg': result['msg']
        })
    catgorys, tags = article_get_catgorys_tags_lib()
    kw = {
        'categorys': catgorys,
        'tags': tags,
    }
    return render(request, 'article/add_article.html', kw)


@login_required
def add_category_tag(request):
    """
    添加标签
    :param request:
    :return:
    """
    if request.method == 'POST':
        catgory_name = request.POST.get('category_name', '')
        tag_name = request.POST.get('tag_name', '')
        result = add_catgory_libs(catgory_name, tag_name)
        if result['status'] is True:
            return JsonResponse({
                'status': 200,
                'msg': result['msg']
            })
        return JsonResponse({
            'status': False,
            'msg': result['msg']
        })
    catgorys, tags = article_get_catgorys_tags_lib()
    kw = {
        'categorys': catgorys,
        'tags': tags,
    }
    print kw
    return render(request, 'article/article_add_category_tag.html', kw)


def article(request):
    """
    返回文章
    :param request:
    :return:
    """
    article_id = request.GET.get('id', '')
    result = article_lib(article_id)
    if result['status'] is True:
        kw = {
            'article': result['article'],
            'comments': result['comments'],
        }
        return render(request, 'article/article.html', kw)
    return HttpResponse(result['msg'])


@login_required
def add_comment(request):
    """
    添加一级评论
    :param request:
    :return:
    """
    if request.method == 'POST':
        post = request.POST.copy()
        content = post.get('content', '')
        article_id = post.get('id', '')
        print article_id
        result = add_comment_lib(request, content, article_id)
        if result['status'] is True:
            return JsonResponse({
                'status': 200,
                'msg': result['msg']
            })
        return JsonResponse({
            'status': 400,
            'msg': result['msg']
        })
    return render(request, 'article/article.html')


@login_required
def add_second_comment(request):
    """
    添加二级评论
    :param request:
    :return:
    """
    if request.method == 'POST':
        post = request.POST.copy()
        content = post.get('content', '')
        article_id = post.get('id', '')
        result = add_second_comment_lib(request, content, article_id)
        if result['status'] is True:
            return JsonResponse({
                'status': 200,
                'msg': result['msg']
            })
        return JsonResponse({
            'status': 400,
            'msg': result['msg']
        })
    return render(request, 'article/article.html')


@login_required
def add_like(request):
    """
    点赞
    :param request:
    :return:
    """
    if request.method == 'POST':
        post = request.POST.copy()
        article_id = post.get('article_id', '')
        result = add_like_lib(request, article_id)
        if result['status'] is True:
            return JsonResponse({
                'status': 200,
                'msg': result['msg']
            })
        return JsonResponse({
            'status': 400,
            'msg': result['msg']
        })
    return render(request, 'article/article.html')


@login_required
def article_modify_list(request):
    """
    文章列表
    :param request:
    :return:
    """
    article = article_modify_list_lib()
    kw = {
        'articles': article
    }
    return render(request, 'article/article_modify_list.html', kw)


@login_required
def article_delete(request):
    """
    删除文档
    :param request:
    :return:
    """

    article_id = request.GET.get('id', '')
    print article_id
    article_delete_lib(request, article_id)
    return redirect('/article/article_modify_list/')


@login_required
def article_modift(request):
    getdata = request.GET.copy()
    article_id = getdata.get('id', '')
    categorys, tags = article_get_catgorys_tags_lib()
    article = article_get_lib(article_id)
    kw = {
        'categorys': categorys,
        'tags': tags,
        'article': article
    }
    print categorys
    print tags
    return render(request, 'article/article_modify.html', kw)
