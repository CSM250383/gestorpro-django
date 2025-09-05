from django.urls import path
from . import views

app_name = 'app_administrar'  # <-- define el namespace

urlpatterns = [
  
    path('v1/', views.registrar_usuario, name='registrar_usuario'),

    path('v2/', views.lista_usuarios, name='lista_usuarios'),

    #path('administrar/v3/', views.registrar_rol, name='registrar_rol'),
]
