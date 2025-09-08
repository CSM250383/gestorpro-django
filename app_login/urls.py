from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'app_login'

urlpatterns = [  # ← Sin espacios al inicio ✅
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]