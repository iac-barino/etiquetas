import os
from GeneraEtiqueta import generar_etiqueta 
from PedirDemasDatos import pedir_datos
from PedirNumOrden import pedir_numero_orden
from Datos import DatosEtiqueta
from ObtenerDatosBBDD import obtener_datos
from tkinter import messagebox


datos_producto = DatosEtiqueta()

#En primer lugar buscamos el número de orden en nuestra base de datos
numOrden=pedir_numero_orden(datos_producto)

#Si llega aquí es que el número de orden es correcto y se encuentra en la bbdd

while(1): #Nop para de pedir datos hasta que se introduzcan correctamente
    pedir_datos(datos_producto)
   
    if datos_producto.is_valid():
        if(datos_producto.seleccion!=1): #vuelve a buscar el cod de barras si la calidad es diferente a 1
            datosRecibidos = obtener_datos(datos_producto.numOrden,datos_producto.seleccion)
            datos_producto.codBarras= datosRecibidos[3]
        break
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, rellene todos los campos correctamente.")




archivo_salida = "etiqueta3.pdf"
# Ejecutar la función para generar la etiqueta
generar_etiqueta(datos_producto)

# Abrir el archivo automáticamente en Windows
if os.name == "nt":  
    os.startfile(archivo_salida)
elif os.name == "posix":
    os.system(f"xdg-open {archivo_salida}")  # Para Linux y macOS
