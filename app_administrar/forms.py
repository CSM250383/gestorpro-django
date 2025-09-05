from django import forms
from .models import Usuario, Rol, Permiso

# Formularios en Django registrar_usuario----------------------------------------------------

class UsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'contrasena', 'correo', 'nombres', 'apellidos', 'esta_activo']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        from django.contrib.auth.hashers import make_password
        usuario.contrasena_hash = make_password(self.cleaned_data['contrasena'])
        if commit:
            usuario.save()
        return usuario

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre_rol']


class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['nombre_permiso']
