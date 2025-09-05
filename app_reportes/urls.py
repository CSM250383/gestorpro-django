from django.urls import path
from . import views

app_name = 'app_reportes'  # <-- define el namespace

urlpatterns = [
    #path('', views.home, name='home'),
    path('reportes/v1/', views.reportes_v1, name='reportes_v1'),
    path('reportes/v2/', views.reportes_v2, name='reportes_v2'),
]
