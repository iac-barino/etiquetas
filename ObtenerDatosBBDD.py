import pyodbc

def obtener_datos(numero_orden, calidad):
    
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
        if len(str(numero_orden)) ==5:
            cadenaNumeroOrden = str(numero_orden) + "%"
        else:
            cadenaNumeroOrden = str(numero_orden)

        cursor.execute(
            "SELECT * FROM iac_Etiquetas WHERE Orden LIKE ?",
            ( cadenaNumeroOrden)
        )

        resultado = cursor.fetchone()
        #print (resultado) #Imprimir el resultado de la consulta
        return resultado if resultado else None

    except Exception as e:
        print(f" Error al consultar la base de datos: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()


# Para permitir importar esta función desde otro fichero
__all__ = ['obtener_datos']
