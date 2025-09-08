# config/validate_connection.py
#!/usr/bin/env python3
"""
Script para validar la conexión a SQL Server
"""
import pyodbc
import logging
from pathlib import Path
import sys

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_sql_server_connection():
    """Probar conexión directa a SQL Server"""
    config = {
        'host': 'localhost',
        'database': 'dbGestorPro',
        'user': 'sa',
        'password': 'Sori@.41722758',
        'port': '1433',
        'driver': 'ODBC Driver 17 for SQL Server'
    }
    
    try:
        # Crear string de conexión
        connection_string = (
            f"DRIVER={{{config['driver']}}};"
            f"SERVER={config['host']};"
            f"DATABASE={config['database']};"
            f"UID={config['user']};"
            f"PWD={config['password']};"
            f"PORT={config['port']};"
            f"TrustServerCertificate=yes;"
        )
        
        logger.info("Intentando conectar a SQL Server...")
        logger.info(f"Servidor: {config['host']}")
        logger.info(f"Base de datos: {config['database']}")
        logger.info(f"Usuario: {config['user']}")
        
        # Intentar conexión
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Ejecutar consulta simple
        cursor.execute("SELECT @@VERSION as version")
        version = cursor.fetchone()[0]
        
        # Verificar tablas existentes
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE'
        """)
        tablas = [row[0] for row in cursor.fetchall()]
        
        logger.info("✅ CONEXIÓN EXITOSA!")
        logger.info(f"Versión de SQL Server: {version.split(',')[0]}")
        logger.info(f"Tablas encontradas: {len(tablas)}")
        
        # Verificar tablas específicas de tu sistema
        tablas_requeridas = ['Usuario', 'Rol', 'Permiso', 'UsuarioRol', 'RolPermiso']
        for tabla in tablas_requeridas:
            if tabla in tablas:
                logger.info(f"✅ Tabla {tabla}: EXISTE")
            else:
                logger.warning(f"⚠️  Tabla {tabla}: NO ENCONTRADA")
        
        conn.close()
        return True
        
    except pyodbc.InterfaceError as e:
        logger.error(f"❌ Error de interfaz ODBC: {e}")
        logger.error("Verifica que el ODBC Driver 17 esté instalado")
        return False
        
    except pyodbc.OperationalError as e:
        logger.error(f"❌ Error operacional: {e}")
        logger.error("Verifica:")
        logger.error("1. Que SQL Server esté ejecutándose")
        logger.error("2. Que el servidor y puerto sean correctos")
        logger.error("3. Que la base de datos exista")
        return False
        
    except pyodbc.ProgrammingError as e:
        logger.error(f"❌ Error de programación: {e}")
        logger.error("Verifica:")
        logger.error("1. Usuario y contraseña correctos")
        logger.error("2. Permisos de usuario")
        return False
        
    except Exception as e:
        logger.error(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("VALIDACIÓN DE CONEXIÓN A SQL SERVER")
    print("=" * 50)
    
    success = test_sql_server_connection()
    
    print("=" * 50)
    if success:
        print("✅ CONEXIÓN VALIDADA EXITOSAMENTE")
        sys.exit(0)
    else:
        print("❌ FALLA EN LA CONEXIÓN")
        sys.exit(1)