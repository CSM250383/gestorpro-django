from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .decorador import login_required_custom
from app_administrar.models import Usuario

def login_view(request):
    if request.method == "POST":
        nombre = request.POST.get("usuario")
        password = request.POST.get("contrasena")

        try:
            user = Usuario.objects.get(nombre_usuario=nombre)
            if check_password(password, user.contrasena_hash):
                # Guardar datos del usuario en la sesión
                request.session["usuario_id"] = user.usuario_id
                request.session["usuario_nombre"] = user.nombre_usuario
                request.session["usuario_nombres"] = user.nombres
                request.session["usuario_apellidos"] = user.apellidos
                request.session["usuario_correos"] = user.correo 
                messages.success(request, f"Bienvenido {user.nombres} {user.apellidos}")
                
                return redirect("app_dashboard:dashboard_v1")
            else:
                messages.error(request, "Contraseña incorrecta")
                
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no encontrado")
        
        # Si hay error, mostrar el formulario nuevamente
        return render(request, "app_login/login.html")
    
    # Si es GET, mostrar el formulario
    return render(request, "app_login/login.html")

def logout_view(request):
    # Limpieza completa en un solo paso
    request.session.flush()
    request.session.cycle_key()
    
    # Limpiar mensajes específicamente
    list(messages.get_messages(request))  # Esto consume y limpia los mensajes
    
    messages.success(request, "Sesión cerrada correctamente")
    return redirect("app_login:login")