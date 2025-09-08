# app_login/backends.py - Versión alternativa
import pyodbc
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password

class AuthManager:
    """Gestor de autenticación personalizado"""
    
    def authenticate(self, username, password):
        try:
            print(f"🔐 Autenticando: {username}")
            print(f"🔐 Password recibido: {password}")
            
            connection_string = (
                f"DRIVER={{{settings.DATABASES['default']['OPTIONS']['driver']}}};"
                f"SERVER={settings.DATABASES['default']['HOST']};"
                f"DATABASE={settings.DATABASES['default']['NAME']};"
                f"UID={settings.DATABASES['default']['USER']};"
                f"PWD={settings.DATABASES['default']['PASSWORD']};"
                f"TrustServerCertificate=yes;"
            )
            
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()
                
                # PRIMERO: Buscar por nombre de usuario
                cursor.execute("""
                    SELECT usuario_id, nombre_usuario, contrasena_hash, correo, 
                           nombres, apellidos, esta_activo
                    FROM app_administrar_usuario 
                    WHERE nombre_usuario = ? AND esta_activo = 1
                """, (username,))
                
                user_data = cursor.fetchone()
                
                if not user_data:
                    # SEGUNDO: Si no encuentra, buscar por correo
                    cursor.execute("""
                        SELECT usuario_id, nombre_usuario, contrasena_hash, correo, 
                               nombres, apellidos, esta_activo
                        FROM app_administrar_usuario 
                        WHERE correo = ? AND esta_activo = 1
                    """, (username,))
                    user_data = cursor.fetchone()
                
                if user_data:
                    usuario_id, nombre_usuario, contrasena_hash, correo, \
                    nombres, apellidos, esta_activo = user_data
                    
                    print(f"✅ Usuario encontrado: {nombre_usuario}")
                    print(f"🔐 Hash en BD: {contrasena_hash}")
                    
                    # Verificación de contraseña hasheada
                    if check_password(password, contrasena_hash):
                        print(f"✅✅✅ CONTRASEÑA VÁLIDA")
                        return {
                            'usuario_id': usuario_id,
                            'nombre_usuario': nombre_usuario,
                            'correo': correo,
                            'nombres': nombres,
                            'apellidos': apellidos,
                            'esta_activo': esta_activo
                        }
                    else:
                        print("❌❌❌ CONTRASEÑA INCORRECTA")
                        # Debug: crear hash temporal para comparar
                        test_hash = make_password(password)
                        print(f"🔐 Hash de prueba: {test_hash}")
                        return None
                else:
                    print("❌ Usuario NO encontrado en la BD")
                    return None
                        
        except Exception as e:
            print(f"🔥 Error en autenticación: {str(e)}")
            return None

auth_manager = AuthManager()