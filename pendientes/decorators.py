from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        user = request.user
        LOGIN_URL = '/'
        user_groups = user.groups.values_list("name", flat=True)
        if 'Academica' in user_groups:
            LOGIN_URL = 'peticionesacede/'
        elif 'Administracion' in user_groups:
            LOGIN_URL = 'peticionesadmin/'
        elif 'Planeacion' in user_groups:
            LOGIN_URL = 'peticionesplan/'
        elif 'Direccion' in user_groups:
            LOGIN_URL = '/'        
        elif user.is_admin:
            LOGIN_URL = '/'
        else:
            LOGIN_URL = 'peticionesacede/'

        if user.is_authenticated:  # esto puede variar de acuerdo a la versión de django que uses, pero si no funciona usa if user.is_authenticated()
            return view_func(request, *args, **kwargs)
        return redirect(LOGIN_URL)
    return wrapped_view