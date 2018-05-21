# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from account.models import User
# Create your models here.

class Handler(models.Model):
    """视图函数表"""

    name = models.CharField(verbose_name=u'视图名称', max_length=50, unique=True)
    permission = models.OneToOneField('Permission')

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()


    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

class Menu(models.Model):
    """菜单表"""
    name = models.CharField(verbose_name=u'菜单名称', max_length=50, unique=True)
    permission = models.OneToOneField('Permission')

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()


    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

class Permission(models.Model):
    """权限表"""

    name = models.CharField(verbose_name=u'权限名称', max_length=50, unique=True)
    strcode =  models.CharField(verbose_name=u'权限码', max_length=50, unique=True) #权限码
    roles = models.ManyToManyField('Role')

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()


    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s name: %s strcode: %s" % (self.id, self.name, self.strcode)

class Role(models.Model):
    """角色表"""

    name = models.CharField(verbose_name=u'角色名称', max_length=50, unique=True)
    users = models.ManyToManyField(User)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def by_id(cls, id):
        return cls.objects.filter(id=id).first()


    @classmethod
    def by_name(cls, name):
        return cls.objects.filter(name=name).first()

    def __unicode__(self):
        return "id: %s name: %s" % (self.id, self.name)
