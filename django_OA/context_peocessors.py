# -*- coding: utf-8 -*-

def current_user_processors(request):
    return {'current_user': request.current_user}
