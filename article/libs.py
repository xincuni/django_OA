# -*- coding: utf-8 -*-
from models import User, Article, Tag, Comment, Category, SecondComment


def add_catgory_libs(catgory_name, tag_name):
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
    category = Category.all()
    tags = Tag.all()
    # print tags,'---------------'
    return category, tags


def add_article_libs(request, title, article_content, category, tags, article_id, desc, thumbnail):
    """
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
    article = Article()

    article.user = request.current_user
    article.title = title
    article.content = article_content
    article.desc = desc
    article.category_id = category
    article.article_id = article_id
    article.thumbnail = thumbnail
    # print request.current_user
    article.save()
    """
        'data': {
                'title': title,
                'article': article,
                'desc': desc,
                'category': category,
                'thumbnail': thumbnail,
                'tags': tags,
                'article_id': $('#title-input').attr('data-article-id')"""
    # for tag in tags:
    #     tag = Tag.by_id(tag)
    #     print tag
    #     article.tags.add(tag)
    # article.save()
    return {'status': True, 'msg': '文章添加成功'}
