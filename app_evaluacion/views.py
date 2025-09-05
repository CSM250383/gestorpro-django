from django.shortcuts import render

# Create your views here.

def evaluacion_v1(request):
    return render(request, "app_evaluacion/evaluacion_v1.html")

def evaluacion_v2(request):
    return render(request, "app_evaluacion/evaluacion_v2.html")