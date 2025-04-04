import os
from generaEtiqueta import generar_etiqueta 
from pedirDatos import pedir_datos
from PedirNumOrden import pedir_numero_orden

#En primer lugar buscamos el número de orden en nuestra base de datos
numOrden=pedir_numero_orden()

#Si llega aquí es que el número de orden es correcto y se encuentra en la bbdd

# Obtener los datos desde el formulario
datos = pedir_datos()


if datos and numOrden:
    archivo_salida = "etiqueta3.pdf"

    # Ejecutar la función para generar la etiqueta
    generar_etiqueta(
        nombre_articulo=f"{datos['nombreArticulo']}",
        codigo=numOrden,
        tono=datos['tono'],
        fecha=datos['fecha'],
        barcode="8435451959805",
        seleccion=datos['seleccion'],
        calibre=datos['calibre']
    )

    #print(f"Etiqueta guardada en {archivo_salida}")

    # Abrir el archivo automáticamente en Windows
    if os.name == "nt":  
        os.startfile(archivo_salida)
    elif os.name == "posix":
        os.system(f"xdg-open {archivo_salida}")  # Para Linux y macOS
