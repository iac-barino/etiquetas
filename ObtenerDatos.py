import pyodbc

def obtener_datos(numero_orden):
    """Consulta la base de datos y devuelve nombreArticulo y codBarras dado un numeroOrden."""
    server = 'NTNOW'
    database = 'INALCO_PRUEBAS'
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        'UID=flexygo;'
        'PWD=FL3XYG0I@c;'
        
    )
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Consulta SQL
        cursor.execute("SELECT nombreArticulo, codBarras FROM EtiquetasDatos WHERE numeroOrden = ?", (numero_orden,))
        resultado = cursor.fetchone()
        
        return resultado if resultado else None
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    finally:
        if 'conn' in locals():
            conn.close()

# Permite importar el método desde otro fichero
__all__ = ['obtener_datos']
