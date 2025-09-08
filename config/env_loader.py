# config/env_loader.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

class EnvironmentLoader:
    """Cargador profesional de variables de entorno"""
    
    def __init__(self, env_path=None):
        self.env_path = env_path or self.find_env_file()
        self.load_environment()
        self.validate_required_variables()
    
    def find_env_file(self):
        """Buscar archivo .env en el proyecto"""
        base_dir = Path(__file__).resolve().parent.parent
        
        # Buscar archivo .env (sin extensión)
        env_file = base_dir / '.env'
        
        if env_file.exists():
            logger.info(f"Archivo .env encontrado en: {env_file}")
            return env_file
        
        logger.warning("No se encontró archivo .env, usando variables de entorno del sistema")
        return None
    
    def load_environment(self):
        """Cargar variables de entorno desde archivo .env"""
        try:
            if self.env_path:
                # Cargar desde archivo .env específico
                load_dotenv(self.env_path, override=True)
                logger.info("Variables de entorno cargadas desde archivo .env")
            else:
                # Intentar cargar desde .env en directorio actual
                load_dotenv()
                logger.info("Variables de entorno cargadas desde .env en directorio actual")
        except Exception as e:
            logger.error(f"Error cargando variables de entorno: {e}")
            sys.exit(1)
    
    def validate_required_variables(self):
        """Validar que las variables requeridas estén presentes"""
        required_vars = [
            'DB_HOST',
            'DB_NAME', 
            'DB_USER',
            'DB_PASSWORD',
            'SECRET_KEY'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            error_msg = f"Variables de entorno requeridas faltantes: {', '.join(missing_vars)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
    
    def get(self, key, default=None, required=False):
        """Obtener variable de entorno de forma segura"""
        value = os.getenv(key, default)
        
        if required and value is None:
            error_msg = f"Variable de entorno requerida faltante: {key}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        # Para contraseñas, no loggear el valor real
        if 'PASSWORD' in key or 'SECRET' in key or 'KEY' in key:
            log_value = '******' if value else 'None'
        else:
            log_value = value
            
        logger.debug(f"Variable de entorno: {key}={log_value}")
        
        return value

# Instancia global del cargador de entorno
env_loader = EnvironmentLoader()