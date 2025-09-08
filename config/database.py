# config/database.py
import pyodbc
from django.conf import settings
from .env_loader import env_loader
import logging
from contextlib import contextmanager
from typing import Optional, Generator
import time
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class DatabaseConfig:
    """Configuración de base de datos"""
    host: str
    database: str
    user: str
    password: str
    port: int = 1433
    driver: str = "ODBC Driver 17 for SQL Server"
    timeout: int = 30
    max_retries: int = 3
    retry_delay: int = 2

class DatabaseConnectionManager:
    """Manejador profesional de conexiones a BD"""
    
    _instance = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Inicializar configuración desde variables de entorno"""
        self._config = DatabaseConfig(
            host=env_loader.get('DB_HOST', required=True),
            database=env_loader.get('DB_NAME', required=True),
            user=env_loader.get('DB_USER', required=True),
            password=env_loader.get('DB_PASSWORD', required=True),
            port=int(env_loader.get('DB_PORT', '1433')),
            driver=env_loader.get('DB_DRIVER', 'ODBC Driver 17 for SQL Server'),
            timeout=int(env_loader.get('DB_TIMEOUT', '30')),
            max_retries=int(env_loader.get('DB_MAX_RETRIES', '3')),
            retry_delay=int(env_loader.get('DB_RETRY_DELAY', '2'))
        )
    
    def get_connection_string(self) -> str:
        """Generar string de conexión seguro (sin password en logs)"""
        return (
            f"DRIVER={{{self._config.driver}}};"
            f"SERVER={self._config.host};"
            f"DATABASE={self._config.database};"
            f"UID={self._config.user};"
            f"PWD=******;"
            f"PORT={self._config.port};"
            f"Connection Timeout={self._config.timeout};"
        )
    
    def get_actual_connection_string(self) -> str:
        """Generar string de conexión real (con password)"""
        return (
            f"DRIVER={{{self._config.driver}}};"
            f"SERVER={self._config.host};"
            f"DATABASE={self._config.database};"
            f"UID={self._config.user};"
            f"PWD={self._config.password};"
            f"PORT={self._config.port};"
            f"Connection Timeout={self._config.timeout};"
        )
    
    @contextmanager
    def get_connection(self) -> Generator[pyodbc.Connection, None, None]:
        """Context manager para obtener conexión con reintentos"""
        connection = None
        attempt = 0
        
        while attempt < self._config.max_retries:
            try:
                connection = pyodbc.connect(self.get_actual_connection_string())
                logger.info("Conexión a BD establecida exitosamente")
                yield connection
                break
                
            except pyodbc.OperationalError as e:
                attempt += 1
                logger.warning(f"Intento {attempt} de conexión falló: {e}")
                
                if attempt == self._config.max_retries:
                    logger.error("Máximo número de reintentos alcanzado")
                    raise
                
                time.sleep(self._config.retry_delay)
                
            except pyodbc.Error as e:
                logger.error(f"Error de conexión a BD: {e}")
                raise
                
            finally:
                if connection:
                    try:
                        connection.close()
                        logger.debug("Conexión a BD cerrada")
                    except:
                        pass
    
    def test_connection(self) -> bool:
        """Probar conexión a la base de datos"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                return result[0] == 1
        except Exception as e:
            logger.error(f"Test de conexión falló: {e}")
            return False

# Instancia global del manejador de base de datos
db_manager = DatabaseConnectionManager()

# Función de conveniencia para obtener conexión
def get_db_connection():
    """Obtener conexión a la base de datos"""
    return db_manager.get_connection()