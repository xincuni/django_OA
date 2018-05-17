# -*- coding: utf-8 -*-
from models import Role, Handler, Permission, User, Menu


def premission_manage_libs():
    roles = Role.all()
    permissions = Permission.all()
    menus = Menu.all()
    # menus = menus.by_id(1)
    # print 'permissions',permissions
    users = User.all()
    handlers = Handler.all()
    return roles, permissions, menus, users, handlers

