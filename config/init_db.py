# config/init_db.py
#!/usr/bin/env python3
"""
Script de inicialización y verificación de base de datos
"""
import logging
from .database import db_manager
from .env_loader import env_loader

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_database():
    """Inicializar y verificar la conexión a la base de datos"""
    logger.info("Inicializando conexión a base de datos...")
    
    # Mostrar configuración (sin password)
    logger.info(f"Configuración de BD: {db_manager.get_connection_string()}")
    
    # Probar conexión
    if db_manager.test_connection():
        logger.info("✅ Conexión a base de datos exitosa")
        return True
    else:
        logger.error("❌ No se pudo conectar a la base de datos")
        return False

def check_required_tables():
    """Verificar que las tablas requeridas existan"""
    required_tables = ['Usuario', 'Rol', 'Permiso', 'UsuarioRol', 'RolPermiso']
    
    try:
        with db_manager.get_connection() as conn:
            cursor = conn.cursor()
            
            for table in required_tables:
                cursor.execute(f"""
                    SELECT COUNT(*) 
                    FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_NAME = ?
                """, (table,))
                
                exists = cursor.fetchone()[0] > 0
                status = "✅" if exists else "❌"
                logger.info(f"{status} Tabla {table}: {'EXISTE' if exists else 'FALTANTE'}")
                
                if not exists:
                    return False
            
            return True
            
    except Exception as e:
        logger.error(f"Error verificando tablas: {e}")
        return False

if __name__ == "__main__":
    print("=== Verificación de Base de Datos ===")
    
    if initialize_database():
        print("\n=== Verificación de Tablas ===")
        if check_required_tables():
            print("\n✅ Todas las verificaciones pasaron correctamente")
        else:
            print("\n❌ Algunas tablas requeridas no existen")
            exit(1)
    else:
        exit(1)