from django.shortcuts import render
from app_login.decorador import login_required  # ← Usa nuestro decorador personalizado

@login_required
def dashboard_v1(request):
    """Dashboard después del login"""
    return render(request, "app_dashboard/dashboard_v1.html", {
        "usuario": request.session.get('usuario_nombres', ''),
        "apellido": request.session.get('usuario_apellidos', ''),
        "correo": request.session.get('usuario_correo', ''),
    })

@login_required
def dashboard_v2(request):
    return render(request, "app_dashboard/dashboard_v2.html")