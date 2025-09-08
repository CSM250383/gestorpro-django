# config/settings.py
import os
from pathlib import Path
from .env_loader import env_loader

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de base de datos para Django
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': env_loader.get('DB_NAME', 'GestorProDB'),
        'USER': env_loader.get('DB_USER', 'sa'),
        'PASSWORD': env_loader.get('DB_PASSWORD', ''),
        'HOST': env_loader.get('DB_HOST', 'localhost'),
        'PORT': env_loader.get('DB_PORT', '1433'),
        'OPTIONS': {
            'driver': env_loader.get('DB_DRIVER', 'ODBC Driver 17 for SQL Server'),
            'extra_params': 'TrustServerCertificate=yes',  # Para desarrollo
        },
    }
}

# Configuración adicional para producción
if env_loader.get('DJANGO_ENV') == 'production':
    DATABASES['default']['OPTIONS']['extra_params'] = 'Encrypt=yes;TrustServerCertificate=no'