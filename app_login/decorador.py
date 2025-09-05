from django.shortcuts import redirect
from functools import wraps
  
def login_required_custom(funcion):
    @wraps(funcion)
    def wrapper(request, *args, **kwargs):
        # request.session es dict-like, no función
        if not request.session.get("usuario_id"):
            return redirect("app_login:login")
        return funcion(request, *args, **kwargs)
    return wrapper