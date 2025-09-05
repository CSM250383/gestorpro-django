from django.shortcuts import render

# Create your views here.

def reportes_v1(request):
    return render(request, "app_reportes/reportes_v1.html")

def reportes_v2(request):
    return render(request, "app_reportes/reportes_v2.html")