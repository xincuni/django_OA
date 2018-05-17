# #coding=utf-8
# import functools
# from django.http import HttpResponse
# from models import Menu, Handler, Role, Permission
#
#
# class ModelBackend(object):
#
#     def _get_user_permissions(self, user_obj):
#         """获取用户（特权）的权限"""
#         return user_obj.permission_set.all()
#
#     def _get_role_permissions(self, user_obj):
#         """获取角色的权限"""
#         return Permission.objects.filter(roles__users__id=user_obj.id)
#
#     def _get_permissions(self, user_obj, from_name):
#         """获取权限，返回权限码列表 """
#         perms = getattr(self, '_get_%s_permissions' % from_name)(user_obj)
#         perms = perms.values_list('strcode')
#         return set("%s" % name for name in perms)
#
#     def get_user_permissions(self, user_obj):
#         """获取用户单独的权限"""
#         return self._get_permissions(user_obj, 'user')
#
#     def get_role_permissions(self, user_obj):
#         """获取用户角色的权限"""
#         return self._get_permissions(user_obj, 'role')
#
#     def get_all_permissions(self, user_obj):
#         """获取用户的全部权限，缓存到当前用户的对象中"""
#         if not hasattr(user_obj, '_perm_cache'):
#             #获取用户单独的权限（获取特权）
#             user_obj._perm_cache = self.get_user_permissions(user_obj)
#             #获取用户角色的权限
#             user_obj._perm_cache.update(self.get_role_permissions(user_obj))#在集合加多个元素 []
#         return user_obj._perm_cache
#
#     def has_perm(self, user_obj, perm):
#         """当前用户有没有这个权限"""
#         return perm in self.get_all_permissions(user_obj)
#
#
# def has_perm(user, perm):
#     """进行权限验证的函数
#      1、获取菜单的权限
#      2、获取用户的权限集合
#      3、判断菜单的权限是不是在用户的权限集合中，在就代表有权限，不在就是没权限
#     """
#     backend = ModelBackend()
#     if backend.has_perm(user, perm):
#         print '----------true--------'
#         return True
#     print '----------False--------'
#     return False
#
# #有缓存的
# class PermWrapper(object):
#     def __init__(self, current_user):
#         print current_user
#         self.current_user = current_user
#
#     def __getitem__(self, menu_name):
#         perm_name = Menu.by_name(menu_name).permission.strcode
#         print perm_name, '----------'
#         return has_perm(self.current_user, perm_name)
#
#
#
# def handler_permission(handlername):
#     def func(method):
#         @functools.wraps(method)
#         def wrapper(self, *args, **kwargs):
#             #perm_name = Handler.by_name(handlername).permission.strcode
#             if has_perm(self.current_user, handlername):
#                 return method(self, *args, **kwargs)
#             else:
#                 return HttpResponse('你没有权限')
#         return wrapper
#     return func
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #没有缓存的
# # class PermWrapper(object):
# #     def __init__(self, current_user):
# #         print current_user
# #         self.current_user = current_user
# #
# #     def __getitem__(self, menu_name):
# #         perm_name = Menu.by_name(menu_name).permission.strcode
# #         print perm_name, '----------'
# #         #permission ---> roles ---->users.id
# #         #判断当前用户是不是有操作这个菜单的权限
# #         #1、获取菜单的权限
# #         #2、获取用户的权限集合
# #         #3、判断菜单的权限是不是在用户的权限集合中，在就代表有权限，不在就是没权限
# #         return Permission.objects.filter(
# #             roles__users__id=self.current_user.id).filter(strcode=perm_name).exists()
# #
# #
# #
# # def handler_permission(handlername):
# #     def func(method):
# #         @functools.wraps(method)
# #         def wrapper(self, *args, **kwargs):
# #             #perm_name = Handler.by_name(handlername).permission.strcode
# #             if Permission.objects.filter(
# #                     roles__users__id=self.current_user.id).filter(strcode=handlername).exists():
# #                 return method(self, *args, **kwargs)
# #             else:
# #                 return HttpResponse('你没有权限')
# #         return wrapper
# #     return func
#
