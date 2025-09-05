"""
URL configuration for GestorPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # 👈 aquí está la clave
from django.views.generic import RedirectView

urlpatterns = [
    
    path('admin/', admin.site.urls),

    # app_login
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', include('app_login.urls')),

    # app_dashboard
    path('dashboard/', include("app_dashboard.urls")),

    # app_planificacion
    path('planificacion/', include("app_planificacion.urls")),

    # app_ejecucion
    path('ejecucion/', include("app_ejecucion.urls")),

    # app_evaluacion
    path('evaluacion/', include("app_evaluacion.urls")),
     
    # app_reportes
    path('reportes/', include("app_reportes.urls")),

    # app_soporte
    path('soporte/', include("app_soporte.urls")),

    # app_configuracion
    path('configuracion/', include("app_configuracion.urls")),

    # app_administrar
    path('administrar/', include("app_administrar.urls")),



]



