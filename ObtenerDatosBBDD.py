import pyodbc
import tkinter as tk
from tkinter import messagebox

# Inicializar tkinter (una sola vez)
root = tk.Tk()
root.withdraw()

server = r'172.31.16.101\HERE'
database = 'DAPNew'

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'UID=limitronic;'
    'PWD=inalco@limitronic;'
    'timeout=3;'
)

def obtener_datos(numero_orden, calidad): 
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Preparar y ejecutar la consulta
        if len(str(numero_orden)) == 5:
            cadenaNumeroOrden = str(numero_orden) + "%"
        else:
            cadenaNumeroOrden = str(numero_orden)

        cursor.execute(
            "SELECT * FROM iac_Etiquetas WHERE Orden LIKE ? AND idclase = ?",
            (cadenaNumeroOrden, calidad)
        )

        resultado = cursor.fetchone()
        return resultado if resultado else None

    except Exception as e:
        messagebox.showerror("Error en la conexión con la base de datos",
                             f"No se pudo conectar a la base de datos. Verifique la conexión y los parámetros.\n\nDetalles: {e}")
        print(f"Error al consultar la base de datos: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()

def obtener_datos_desplegable():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT DISTINCT Orden, Modelo FROM iac_Etiquetas WHERE Modelo NOT LIKE '%ITOP%';"
        )

        resultado = cursor.fetchall()
        return resultado if resultado else None

    except Exception as e:
        messagebox.showerror("Error en la conexión con la base de datos",
            f"No se pudo conectar a la base de datos. Verifique la conexión y los parámetros.\n\nDetalles: {e}")
        print(f"Error al consultar la base de datos: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()

def obtener_datos_calidades(numero_orden):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        if len(str(numero_orden)) == 5:
            cadenaNumeroOrden = str(numero_orden) + "%"
        else:
            cadenaNumeroOrden = str(numero_orden)

        cursor.execute(
            "SELECT DISTINCT idclase FROM iac_Etiquetas WHERE Orden LIKE ?",
            (cadenaNumeroOrden,)
        )

        resultado = cursor.fetchall()
        return resultado if resultado else None

    except Exception as e:
        messagebox.showerror("Error en la conexión con la base de datos",
            f"No se pudo conectar a la base de datos. Verifique la conexión y los parámetros.\n\nDetalles: {e}")
        print(f"Error al consultar la base de datos: {e}")
        return None

    finally:
        if 'conn' in locals():
            conn.close()

# Para permitir importar esta función desde otro fichero
__all__ = ['obtener_datos', 'obtener_datos_desplegable', 'obtener_datos_calidades']
