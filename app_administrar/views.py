from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def registrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_administrar:registrar_usuario")
    else:
        form = UsuarioForm()

    usuarios = Usuario.objects.all()
    return render(request, "app_administrar/registrar_usuario.html", {
        "form": form,
        "usuarios": usuarios
    })

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "app_administrar/lista_usuarios.html", {"usuarios": usuarios})