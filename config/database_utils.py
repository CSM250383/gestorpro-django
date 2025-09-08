# config/database_utils.py
from .database import db_manager
from typing import Any, List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class DatabaseUtils:
    """Utilidades profesionales para operaciones de base de datos"""
    
    @staticmethod
    def execute_query(query: str, params: Optional[list] = None) -> List[Dict[str, Any]]:
        """Ejecutar query y retornar resultados como lista de diccionarios"""
        try:
            with db_manager.get_connection() as conn:
                cursor = conn.cursor()
                
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                # Obtener nombres de columnas
                columns = [column[0] for column in cursor.description]
                
                # Convertir resultados a lista de diccionarios
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                
                return results
                
        except Exception as e:
            logger.error(f"Error ejecutando query: {e}")
            raise
    
    @staticmethod
    def execute_non_query(query: str, params: Optional[list] = None) -> int:
        """Ejecutar query que no retorna resultados (INSERT, UPDATE, DELETE)"""
        try:
            with db_manager.get_connection() as conn:
                cursor = conn.cursor()
                
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                conn.commit()
                return cursor.rowcount
                
        except Exception as e:
            logger.error(f"Error ejecutando non-query: {e}")
            if 'conn' in locals():
                conn.rollback()
            raise
    
    @staticmethod
    def execute_scalar(query: str, params: Optional[list] = None) -> Any:
        """Ejecutar query y retornar primer valor del primer registro"""
        try:
            with db_manager.get_connection() as conn:
                cursor = conn.cursor()
                
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                result = cursor.fetchone()
                return result[0] if result else None
                
        except Exception as e:
            logger.error(f"Error ejecutando scalar: {e}")
            raise
    
    @staticmethod
    def bulk_insert(table: str, data: List[Dict[str, Any]]) -> int:
        """Inserción masiva de datos"""
        if not data:
            return 0
        
        columns = list(data[0].keys())
        placeholders = ', '.join(['?'] * len(columns))
        column_names = ', '.join(columns)
        
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
        
        try:
            with db_manager.get_connection() as conn:
                cursor = conn.cursor()
                
                # Convertir datos a lista de valores
                values = [tuple(item[col] for col in columns) for item in data]
                
                cursor.executemany(query, values)
                conn.commit()
                return cursor.rowcount
                
        except Exception as e:
            logger.error(f"Error en bulk insert: {e}")
            if 'conn' in locals():
                conn.rollback()
            raise

# Instancia global de utilidades de base de datos
db_utils = DatabaseUtils()