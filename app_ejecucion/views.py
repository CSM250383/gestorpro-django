from django.shortcuts import render

# Create your views here.

def ejecucion_v1(request):
    return render(request, "app_ejecucion/ejecucion_v1.html")

def ejecucion_v2(request):
    return render(request, "app_ejecucion/ejecucion_v2.html")