# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4
from datetime import datetime
from django.db import models
from account.models import User
# Create your models here.


class SecondComment(models.Model):
    """二级评论"""

    uuid = models.UUIDField(verbose_name=u'uuid', unique=True, default=uuid4)
    content = models.TextField()
    createtime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    #与文章表建立外键关系
    comment = models.ForeignKey('Comment')#默认是CASCADE
    #与用户表建立外键关系
    user = models.ForeignKey(User)
    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return cls.objects.filter(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s content: %s" % (self.id, self.content)


class Comment(models.Model):
    """评论表"""
    uuid = models.UUIDField(verbose_name=u'uuid', unique=True, default=uuid4)
    content = models.TextField()
    createtime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    #与文章表建立外键关系
    article = models.ForeignKey('Article')  #默认是CASCADE
    #与用户表建立外键关系
    user = models.ForeignKey(User)
    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return cls.objects.filter(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s content: %s" % (self.id, self.content)

class Article(models.Model):
    """文章表"""
    uuid = models.UUIDField(verbose_name=u'uuid', unique=True, default=uuid4)
    title = models.CharField(verbose_name=u'标题', max_length=50, unique=True)
    desc = models.TextField()
    thumbnail = models.CharField(verbose_name=u'缩略图', max_length=200,)
    readnum = models.IntegerField(verbose_name=u'阅读次数', default=0)
    content = models.TextField()
    createtime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)


    # 与用户建立外键关系
    user = models.ForeignKey(User,related_name='articles')

    #与分类建立外键关系
    category = models.ForeignKey('Category')

    # 建立orm查询关系,标签表与文章表的多对多关系
    tags = models.ManyToManyField('Tag')

    #建立orm查询关系，用户表与文章表多对多的点赞关系
    likes=models.ManyToManyField(User, related_name='likes')

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return cls.objects.filter(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s title: %s" % (self.id, self.title)


class Category(models.Model):
    """分类表"""

    uuid = models.UUIDField(verbose_name=u'uuid', unique=True, default=uuid4)

    name = models.CharField(verbose_name=u'姓名', max_length=50, unique=True)

    createtime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return cls.objects.filter(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s name: %s" % (self.id, self.name)

class Tag(models.Model):
    """标签表"""

    uuid = models.UUIDField(verbose_name=u'uuid', unique=True, default=uuid4)

    name = models.CharField(verbose_name=u'姓名', max_length=50, unique=True)

    createtime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return cls.objects.filter(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s name: %s" % (self.id, self.name)



