import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from ObtenerDatosBBDD import obtener_datos_calidades
from tkinter import ttk  # Para usar combobox

def pedir_datos(datos_producto):
    """
    Muestra un formulario para ingresar los datos necesarios y los retorna en un diccionario.
    """
    def enviar():
        """Recoge los datos ingresados y cierra la ventana."""
        try:
            datos_producto.tono = entry_tono.get().upper()
            datos_producto.seleccion = int(selected_calidad.get())          
            datos_producto.calibre = entry_calibre.get().upper()
            datos_producto.fecha = entry_fecha.get()

            if datos_producto.seleccion <= 3:
                root.quit()  # Cierra la ventana si los datos son correctos
            else:
                messagebox.showerror("Seleccion inválida", "El número de calidad debe ser igual o menor a 3")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Asegúrese de ingresar valores correctos.", parent=root)

    # Crear ventana principal
    root = tk.Tk()
    root.title("Ingresa Datos")
    root.geometry("340x320")
    root.attributes("-topmost", True)

    # Calcular el tamaño de la pantalla y centrar la ventana
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()
    ventana_ancho = 340
    ventana_alto = 320
    x = (pantalla_ancho // 2) - (ventana_ancho // 2)
    y = (pantalla_alto // 2) - (ventana_alto // 2)
    root.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")
    root.resizable(False, False)

    # Nombre de artículo (bloqueado)
    nombreDelArticulo = datos_producto.nombreArticulo
    tk.Label(root, text="Nombre de artículo:").pack(pady=2)
    entry_articulo = tk.Entry(root, font=("Arial", 10), width=40)
    entry_articulo.insert(0, nombreDelArticulo)
    entry_articulo.pack()
    entry_articulo.config(state="disabled")

    # Selección (calidad)
   
    # Obtener las calidades posibles usando obtener_datos_calidades
    calidades = obtener_datos_calidades(datos_producto.numOrden)
    
    if not calidades:
        messagebox.showerror("Sin calidades", "No se encontraron calidades para este número de orden.")
        root.quit()
        return

    # Convertir las calidades a una lista de números sin paréntesis ni comas
    calidades = [str(calidad[0]) for calidad in calidades]

    # Crear el combobox con las calidades
    selected_calidad = tk.StringVar()

    # Función para actualizar el valor de calidad seleccionado
    def on_calidad_select(event):
        seleccionada = selected_calidad.get()

    # Crear el combobox para seleccionar la calidad
    tk.Label(root, text="Calidad:").pack()
    calidad_combobox = ttk.Combobox(root, textvariable=selected_calidad, values=calidades, font=("Arial", 10), width=38)
    calidad_combobox.set("1")  # Establecer el valor por defecto como el más bajo (1)
    calidad_combobox.pack(pady=5)
    calidad_combobox.bind("<<ComboboxSelected>>", on_calidad_select)

    # Tono
    tk.Label(root, text="Tono:").pack()
    entry_tono = tk.Entry(root, font=("Arial", 10), width=40)
    entry_tono.pack()

    # Calibre
    tk.Label(root, text="Calibre:").pack(pady=2)
    entry_calibre = tk.Entry(root, font=("Arial", 10), width=40)
    entry_calibre.pack()

    # Fecha
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    tk.Label(root, text="Fecha:").pack(pady=2)
    entry_fecha = tk.Entry(root, font=("Arial", 10), width=40)
    entry_fecha.insert(0, fecha_actual)
    entry_fecha.pack(pady=5)

    # Botón Aceptar
    btn_aceptar = tk.Button(root, text="Aceptar", command=enviar, font=("Arial", 11), width=11)
    btn_aceptar.pack(pady=15)

    # Enfocar tono al inicio
    def enfocar():
        root.focus_force()
        entry_tono.focus_force()
        entry_tono.selection_range(0, tk.END)

    root.after(50, enfocar)

    # Navegación con Enter: Tono → Calibre → Fecha → Aceptar
    entry_tono.bind("<Return>", lambda e: entry_calibre.focus())
    entry_calibre.bind("<Return>", lambda e: entry_fecha.focus())
    entry_fecha.bind("<Return>", lambda e: btn_aceptar.invoke())

    root.mainloop()
    root.destroy()
