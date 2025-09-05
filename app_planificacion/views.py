from django.shortcuts import render

# Create your views here.

def planificacion_v1(request):
    return render(request, "app_planificacion/planificacion_v1.html")

def planificacion_v2(request):
    return render(request, "app_planificacion/planificacion_v2.html")