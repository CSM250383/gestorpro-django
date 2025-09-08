from django.urls import path
from . import views

app_name = 'app_dashboard'  # <-- define el namespace

urlpatterns = [
   # path('', views.home, name='home'),
    path('t1/', views.dashboard_v1, name='dashboard_v1'),
    path('t2/', views.dashboard_v2, name='dashboard_v2'),
]




