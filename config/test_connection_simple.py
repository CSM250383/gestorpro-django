# test_connection_simple.py
import pyodbc
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_sql_server_connection():
    """Probar conexión directa a SQL Server"""
    try:
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=dbGestorPro;"
            "UID=sa;"
            "PWD=Sori@.41722758;"
            "PORT=1433;"
            "TrustServerCertificate=yes;"
        )
        
        logger.info("Intentando conectar a SQL Server...")
        logger.info("Servidor: localhost")
        logger.info("Base de datos: dbGestorPro")
        logger.info("Usuario: sa")
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Ejecutar consulta simple
        cursor.execute("SELECT @@VERSION as version")
        version = cursor.fetchone()[0]
        
        logger.info("✅ CONEXIÓN EXITOSA!")
        logger.info(f"Versión de SQL Server: {version.split(',')[0]}")
        
        # Verificar tablas existentes
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE'
        """)
        tablas = [row[0] for row in cursor.fetchall()]
        logger.info(f"Tablas encontradas: {len(tablas)}")
        
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
    else:
        print("❌ FALLA EN LA CONEXIÓN")