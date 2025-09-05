from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'app_login'  # <-- define el namespace

urlpatterns = [

    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
  #  path('l2/', views.panel_view, name='panel'),

]


