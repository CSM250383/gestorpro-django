from django.urls import path
from . import views

app_name = 'app_planificacion'  # <-- define el namespace

urlpatterns = [

    # path('', views.home, name='home'),
    path('planificacion/v1/', views.planificacion_v1, name='planificacion_v1'),
    path('planificacion/v2/', views.planificacion_v2, name='planificacion_v2'),

]
