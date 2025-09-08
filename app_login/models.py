# app_login/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contrasena_hash = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    esta_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField()  # Cambiado a DateTimeField sin auto_now
    fecha_actualizacion = models.DateTimeField()  # Cambiado a DateTimeField sin auto_now
    
    # Campos requeridos para AbstractBaseUser

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['correo']

    class Meta:
        managed = False
        db_table = 'app_administrar_usuario'

    def __str__(self):
        return self.nombre_usuario

    def get_full_name(self):
        return f"{self.nombres or ''} {self.apellidos or ''}".strip()

    def get_short_name(self):
        return self.nombres or self.nombre_usuario


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = False
        db_table = 'app_administrar_rol'

    def __str__(self):
        return self.nombre_rol


class Permiso(models.Model):
    permiso_id = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=100, unique=True)

    class Meta:
        managed = False
        db_table = 'app_administrar_permiso'

    def __str__(self):
        return self.nombre_permiso


class UsuarioRol(models.Model):
    id = models.BigAutoField(primary_key=True)  # ← Campo adicional encontrado
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuario_id')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id')

    class Meta:
        managed = False
        db_table = 'app_administrar_usuariorol'
        unique_together = ('usuario', 'rol')  # Mantener la constraint única


class RolPermiso(models.Model):
    id = models.BigAutoField(primary_key=True)  # ← Campo adicional encontrado
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id')
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, db_column='permiso_id')

    class Meta:
        managed = False
        db_table = 'app_administrar_rolpermiso'
        unique_together = ('rol', 'permiso')  # Mantener la constraint única