from django.urls import path
from . import views

app_name = 'app_evaluacion'  # <-- define el namespace

urlpatterns = [

    # path('', views.home, name='home'),
    path('evaluacion/v1/', views.evaluacion_v1, name='evaluacion_v1'),
    path('evaluacion/v2/', views.evaluacion_v2, name='evaluacion_v2'),
    
]