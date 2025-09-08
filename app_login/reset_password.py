# reset_password.py
import sys
from django.db import connection
from django.contrib.auth.hashers import make_password

if len(sys.argv) != 3:
    print("Uso: python manage.py shell < reset_password.py usuario password")
    sys.exit(1)

username = sys.argv[1]
new_password = sys.argv[2]

try:
    cursor = connection.cursor()
    password_hash = make_password(new_password)
    
    cursor.execute(
        "UPDATE app_administrar_usuario SET contrasena_hash = ? WHERE nombre_usuario = ?",
        (password_hash, username)
    )
    
    if cursor.rowcount > 0:
        print(f"✅ Contraseña reseteda para usuario: {username}")
        print(f"📝 Nueva contraseña: {new_password}")
    else:
        print(f"❌ Usuario no encontrado: {username}")
        
except Exception as e:
    print(f"❌ Error: {e}")