from django.shortcuts import redirect

def login_required(view_func):
    """Decorador personalizado para requerir autenticación"""
    def wrapper(request, *args, **kwargs):
        if request.session.get('usuario_autenticado'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('app_login:login')
    return wrapper