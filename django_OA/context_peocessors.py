# -*- coding: utf-8 -*-
# from permission.perssion_interface_libs import PermWrapper
def current_user_processors(request):
    return {'current_user': request.current_user,
            # 'user_perms':PermWrapper(request.current_user)
            }
