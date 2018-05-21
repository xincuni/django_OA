# -*- coding: utf-8 -*-
from models import User, Article, Tag, Comment, Category, SecondComment
from django.contrib import messages


def add_catgory_libs(catgory_name, tag_name):
    """
    添加标签和分类
    :param catgory_name:
    :param tag_name:
    :return:
    """
    if catgory_name != '':
        Catgory = Category()
        Catgory.name = catgory_name
        Catgory.save()
        return {
            'status': True,
            'msg': '分类添加成功'
        }
    if tag_name != '':
        Tags = Tag()
        Tags.name = tag_name
        Tags.save()
        return {
            'status': True,
            'msg': '标签添加成功'
        }
    return {
        'status': False,
        'msg': '请输入名称'
    }


def article_get_catgorys_tags_lib():
    """
    获取标签和分类
    :return:
    """
    categorys = Category.all()
    tags = Tag.all()
    # print tags,'---------------'
    return categorys, tags


def add_article_libs(request, title, article_content, category, tags, article_id, desc, thumbnail):
    """
    添加文档或者编辑文档
    title, article, category, tags, article_id, desc, thumbnail
    :param args:
    :return:
    """
    print 'category', category
    print 'tags', tags
    if title == '' or article_content == '':
        return {'status': False, 'msg': '标题和文章不能是空'}
    if category == '' or tags == '':
        return {'status': False, 'msg': '分类和标签不能为空'}
    if article_id != '':
        article = Article.by_id(article_id)
        article.tags = []
    else:
        article = Article()

    article.user = request.current_user
    article.title = title
    article.content = article_content
    article.desc = desc
    article.category_id = category
    article.thumbnail = thumbnail
    for tag in tags:
        tag = Tag.by_id(tag)
        print tag
        article.tags.add(tag)
    article.save()
    if article_id != '':
        return {'status': True, 'msg': '文章修改成功'}
    return {'status': True, 'msg': '文章添加成功'}


def get__article_libs():
    """
    获取文章和评论,按照时间倒叙排列
    :return:
    """
    articles = Article.all().order_by('-createtime')
    comments = Comment.all().order_by('-createtime')
    return articles, comments


def article_lib(article_id):
    """
    文章
    :param article_id:
    :return:
    """
    if article_id == '':
        return {'status': False, 'msg': '缺少文章id'}
    article = Article.by_id(article_id)
    article.readnum += 1
    article.save()
    comments = article.comment_set.all()
    return {'status': True, 'msg': '修改成功', 'article': article, 'comments': comments}


def add_comment_lib(request, content, article_id):
    """
    添加评论
    :param request:
    :param content:
    :param article_id:
    :return:
    """
    if article_id == '' or content == '':
        return {'status': False, 'msg': '缺少文章id或者评论内容'}
    if article_id is None:
        return {'status': False, 'msg': '文章id错误'}
    print content, article_id
    contents = Comment()
    contents.content = content
    contents.article_id = article_id
    contents.user = request.current_user
    contents.save()
    return {'status': True, 'msg': '评论提交成功'}


def add_second_comment_lib(request, content, article_id):
    """
    添加二级评论
    :param request:
    :param content:
    :param article_id:
    :return:
    """
    if article_id == '' or content == '':
        return {'status': False, 'msg': '缺少一级评论id或者评论内容'}
    if article_id is None:
        return {'status': False, 'msg': '一级评论id错误'}
    print content, article_id
    Scontent = SecondComment()
    Scontent.content = content
    Scontent.comment_id = article_id
    Scontent.user = request.current_user
    Scontent.save()
    return {'status': True, 'msg': '评论提交成功'}


def add_like_lib(request, article_id):
    """
    点赞
    :param request:
    :param article_id:
    :return:
    """
    if article_id == '':
        return {'status': False, 'msg': '缺少id'}
    if article_id is None:
        return {'status': False, 'msg': 'id错误'}
    article = Article.by_id(article_id)

    if request.current_user in article.likes.all():
        article.likes.remove(request.current_user)
        return {'status': False, 'msg': '已经删除'}

    article.likes.add(request.current_user)

    return {'status': True, 'msg': '点赞成功'}


def article_modify_list_lib():
    """
    返回修改列表
    :return:
    """
    return Article.all()


def article_delete_lib(request, article_id):
    """
    删除
    :param request:
    :param article_id:
    :return:
    """
    article = Article.by_id(article_id)
    print article_id
    print article
    if article_id is None:
        messages.error(request, '文章不存在')
        return
    article.delete()
    messages.success(request, '已经删除')
    return


def article_get_lib(article_id):
    return Article.by_id(article_id)
