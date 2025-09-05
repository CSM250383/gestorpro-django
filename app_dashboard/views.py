from django.shortcuts import render
from app_login.decorador import login_required_custom

# Create your views here.

@login_required_custom
def dashboard_v1(request):
    usuario = request.session.get("usuario_nombres", "")
    apellido = request.session.get("usuario_apellidos", "")
    correo = request.session.get("usuario_correos","")
    return render(request, "app_dashboard/dashboard_v1.html", {
        "usuario": usuario,
        "apellido": apellido,
        "correo": correo,
    })

def dashboard_v2(request):
    return render(request, "app_dashboard/dashboard_v2.html")
