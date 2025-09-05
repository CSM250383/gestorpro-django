# 🚀 GestorPro - Sistema de Gestión Proyectos

## 📦 Tecnologías
- **Backend:** Django 5.2.5 + Django REST Framework
- **Frontend:** Bootstrap 5 + AdminLTE
- **Database:** SQL Server / PostgreSQL
- **Autenticación:** Sistema personalizado

## 🛠️ Instalación

```bash
# 1. Clonar repositorio
git clone [tu-repo-url]
cd GestorPro

# 2. Entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# 3. Dependencias
pip install -r requirements.txt

# 4. Configuración
cp GestorPro/settings/local.py.example GestorPro/settings/local.py

# 5. Base de datos
python manage.py migrate
python manage.py runserver
