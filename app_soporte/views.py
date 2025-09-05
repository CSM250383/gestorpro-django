from django.shortcuts import render

# Create your views here.

def soporte_v1(request):
    return render(request, "app_soporte/soporte_v1.html")

def soporte_v2(request):
    return render(request, "app_soporte/soporte_v2.html")