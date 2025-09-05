from django.urls import path
from . import views

app_name = 'app_ejecucion'  # <-- define el namespace

urlpatterns = [

    # path('', views.home, name='home'),
    path('ejecucion/v1/', views.ejecucion_v1, name='ejecucion_v1'),
    path('ejecucion/v2/', views.ejecucion_v2, name='ejecucion_v2'),
    
]
