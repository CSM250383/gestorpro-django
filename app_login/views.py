# app_login/views.py
from django.shortcuts import render, redirect
from .backends import auth_manager

def login_view(request):
    """Vista personalizada de login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"📨 Login attempt - Usuario: '{username}', Password: '{password}'")
        
        # Verificar que los campos no estén vacíos
        if not username or not password:
            print("❌ Campos vacíos")
            return render(request, 'app_login/login.html', {
                'error': 'Usuario y contraseña son requeridos',
                'username': username
            })
        
        # Usar nuestro sistema personalizado
        user_data = auth_manager.authenticate(username, password)
        
        if user_data:
            print(f"✅✅✅ Login exitoso: {user_data['nombre_usuario']}")
            
            # Crear sesión personalizada
            request.session['usuario_autenticado'] = True
            request.session['usuario_id'] = user_data['usuario_id']
            request.session['usuario_nombre'] = user_data['nombre_usuario']
            request.session['usuario_nombres'] = user_data['nombres']
            request.session['usuario_apellidos'] = user_data['apellidos']
            request.session['usuario_correo'] = user_data['correo']
            
            print(f"💾 Sesión creada: {request.session.items()}")
            
            # Redirigir al dashboard
            return redirect('app_dashboard:dashboard_v1')
        else:
            print("❌❌❌ Login fallido - Redirigiendo a login con error")
            return render(request, 'app_login/login.html', {
                'error': 'Usuario o contraseña incorrectos',
                'username': username
            })
    
    return render(request, 'app_login/login.html')

def logout_view(request):
    """Cerrar sesión personalizada"""
    print("🚪 Cerrando sesión")
    # Limpiar sesión
    request.session.flush()
    return redirect('app_login:login')