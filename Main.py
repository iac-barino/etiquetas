import os
from generaEtiqueta import generar_etiqueta 
from pedirDatos import pedir_datos
from PedirNumOrden import pedir_numero_orden
from Datos import DatosEtiqueta
from ObtenerDatos import obtener_datos


datos_producto = DatosEtiqueta()

#En primer lugar buscamos el número de orden en nuestra base de datos
numOrden=pedir_numero_orden(datos_producto)

#Si llega aquí es que el número de orden es correcto y se encuentra en la bbdd

# Obtener los datos desde el formulario
pedir_datos(datos_producto)
print ("ya ha recibido los datos")

if datos_producto.is_valid():
    archivo_salida = "etiqueta3.pdf"

    # Ejecutar la función para generar la etiqueta
    generar_etiqueta(datos_producto)
    print ("ya ha generado la etiqueta")
    # Abrir el archivo automáticamente en Windows
    if os.name == "nt":  
        os.startfile(archivo_salida)
    elif os.name == "posix":
        os.system(f"xdg-open {archivo_salida}")  # Para Linux y macOS
