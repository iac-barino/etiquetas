import tkinter as tk
from tkinter import messagebox
from datetime import datetime
#from Datos import Datos 

def pedir_datos(datos_producto):
    """
    Muestra un formulario para ingresar los datos necesarios y los retorna en un diccionario.
    """
    def enviar():
        """Recoge los datos ingresados y cierra la ventana."""
        try:
            
            datos_producto.tono = entry_tono.get().upper()
            datos_producto.seleccion = int(entry_seleccion.get())          
            datos_producto.calibre = entry_calibre.get().upper()
            datos_producto.fecha = entry_fecha.get()

            if datos_producto.seleccion <=3:
               root.quit()  # Cierra la ventana si los datos son correctos
            else:
                messagebox.showerror("Seleccion inválida", "El número de calidad debe ser igual o menor a 3")

            
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Asegúrese de ingresar valores correctos.", parent=root)

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresa Datos")
    root.geometry("300x270")

     # Calcular el tamaño de la pantalla y centrar la ventana
    pantalla_ancho = root.winfo_screenwidth()  # Obtener el ancho de la pantalla
    pantalla_alto = root.winfo_screenheight()  # Obtener el alto de la pantalla
    ventana_ancho = 300  # Ancho de la ventana
    ventana_alto = 320  # Alto de la ventana
    
    # Calcular las coordenadas para centrar la ventana
    x = (pantalla_ancho // 2) - (ventana_ancho // 2)
    y = (pantalla_alto // 2) - (ventana_alto // 2)

    # Establecer la posición en el centro de la pantalla
    root.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")

    root.resizable(False, False)

     # Poner nombre y que no deje modificarlo
    nombreDelArticulo = datos_producto.nombreArticulo
    tk.Label(root, text="Nombre de artículo:").pack(pady=2)
    entry_articulo = tk.Entry(root, font=("Arial", 10), width=32)  # Aumento del tamaño
    entry_articulo.insert(0, nombreDelArticulo)  # Insertar el nombre por defecto
    entry_articulo.pack()
    entry_articulo.config(state="disabled")

    # Como máximo 3
    tk.Label(root, text="Calidad:").pack(pady=2)
    entry_seleccion = tk.Entry(root, font=("Arial", 10), width=32)  # Aumento del tamaño
    entry_seleccion.pack()


    tk.Label(root, text="Tono:").pack(pady=2)
    entry_tono = tk.Entry(root, font=("Arial", 10), width=32)  # Aumento del tamaño
    entry_tono.pack()

    tk.Label(root, text="Calibre:").pack(pady=2)
    entry_calibre = tk.Entry(root, font=("Arial", 10), width=32)  # Aumento del tamaño
    entry_calibre.pack()

    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    tk.Label(root, text="Fecha:").pack(pady=2)
    entry_fecha = tk.Entry(root, font=("Arial", 10), width=32)  # Aumento del tamaño
    entry_fecha.insert(0, fecha_actual)  # Insertar la fecha actual
    entry_fecha.pack(pady=5)

    # Botón para aceptar
    btn_aceptar = tk.Button(root, text="Aceptar", command=enviar)
    btn_aceptar.pack(pady=10)

    root.mainloop()
    root.destroy()

