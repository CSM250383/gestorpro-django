import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=dbGestorPro;'  # ← ¡Misma base de datos!
        'UID=sa;'
        'PWD=Sori@.41722758;'
        'TrustServerCertificate=yes;'
    )
    print("✅ Conexión a dbGestorPro exitosa!")
    conn.close()
except Exception as e:
    print(f"❌ Error específico: {e}")