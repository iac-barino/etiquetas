import pyodbc

def obtener_datos(numero_orden, calidad):
    """
    Consulta la base de datos y devuelve el primer registro que coincida con
    la orden (LIKE) y la calidad (idclase).
    
    Args:
        numero_orden (str or int): Parte del número de orden a buscar.
        calidad (int): ID de clase o calidad del producto (por ejemplo, 1, 2, etc.).
    
    Returns:
        tuple or None: Primer registro que coincida o None si no hay resultados.
    """
    
    server = r'172.31.16.101\HERE'
    database = 'DAPNew'

    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        'UID=limitronic;'
        'PWD=inalco@limitronic;'
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Preparar y ejecutar la consulta
        cadenaNumeroOrden = str(numero_orden) + "%"
        #cursor.execute(
        #    "SELECT * FROM iac_Etiquetas WHERE idclase = ? AND Orden LIKE ?",
        #    (calidad, cadenaNumeroOrden)
        #)
        cursor.execute(
            "SELECT * FROM iac_Etiquetas WHERE Orden LIKE ?",
            ( cadenaNumeroOrden)
        )


        resultado = cursor.fetchone()
        #print (resultado)
        return resultado if resultado else None

    except Exception as e:
        print(f" Error al consultar la base de datos: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()


# Para permitir importar esta función desde otro fichero
__all__ = ['obtener_datos']
