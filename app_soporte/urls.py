from django.urls import path
from . import views

app_name = 'app_soporte'  # <-- define el namespace

urlpatterns = [
    #path('', views.home, name='home'),
    path('soporte/v1/', views.soporte_v1, name='soporte_v1'),
    path('soporte/v2/', views.soporte_v2, name='soporte_v2'),
]
