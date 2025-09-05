from django.shortcuts import render

# Create your views here.

def configuracion_v1(request):
    return render(request, "app_configuracion/configuracion_v1.html")

def configuracion_v2(request):
    return render(request, "app_configuracion/configuracion_v2.html")