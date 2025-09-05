from django.urls import path
from . import views

app_name = 'app_configuracion'  # <-- define el namespace

urlpatterns = [
    #path('', views.home, name='home'),
    path('configuracion/v1/', views.configuracion_v1, name='configuracion_v1'),
    path('configuracion/v2/', views.configuracion_v2, name='configuracion_v2'),
]
