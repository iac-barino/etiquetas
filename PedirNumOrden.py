import tkinter as tk
from tkinter import messagebox
from ObtenerDatosBBDD import obtener_datos


def pedir_numero_orden(datos_producto):
    """
    Muestra un formulario con un único campo para ingresar el número de orden.
    Valida si el número está entre 10000 y 99999 antes de aceptarlo.
    """
    def enviar():
        """Valida que se haya ingresado un número entero dentro del rango permitido."""
        try:
            numero_orden = entry_orden.get()
            
            if len(numero_orden) ==5 or len(numero_orden) == 8:
                datosRecibidos = obtener_datos(numero_orden, 1)
                datos_producto.numOrden = numero_orden
                datos_producto.nombreArticulo = datosRecibidos[2] if datosRecibidos else None
                datos_producto.codBarras = datosRecibidos[3] if datosRecibidos else None

                if datosRecibidos is None:
                    messagebox.showerror("Número no encontrado", "El número de orden no se encuentra en la base de datos.")
                elif datos_producto.nombreArticulo is None:
                    messagebox.showerror("Nombre no encontrado", "El nombre del artículo no se encuentra en la base de datos.")
                elif datos_producto.codBarras is None:
                    messagebox.showerror("Código de barras no encontrado", "El código de barras no se encuentra en la base de datos.")
                elif numero_orden[5]!="-":
                    messagebox.showerror("Formato incorrecto", "El formato del número de orden es incorrecto. Debe tener 5 dígitos y opcionalmente un guión seguido de 2 dígitos.")
                else:
                    root.quit()
            else:
                messagebox.showerror("Número inválido", "El número debe tener tener 5 dígitos númericos (opcionalmente se puede añadir un guión y dos díditos más).")
        
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Por favor, ingrese un número entero.")

    # Crear ventana principal
    root = tk.Tk()
    root.title("Generador de Etiqueta")
    root.geometry("300x320")

    # Centrado de ventana
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()
    ventana_ancho = 300
    ventana_alto = 320
    x = (pantalla_ancho // 2) - (ventana_ancho // 2)
    y = (pantalla_alto // 2) - (ventana_alto // 2)
    root.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")
    root.resizable(False, False)

    datos = {"numero_orden": None}

    # Frame para centrar contenido
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Ingrese un número de orden:", font=("Arial", 12)).pack(pady=10)

    entry_orden = tk.Entry(frame, font=("Arial", 12), width=23)
    entry_orden.pack(pady=5)
    entry_orden.focus()

    # Asociar Enter a botón aceptar
    entry_orden.bind("<Return>", lambda e: btn_aceptar.invoke())

    btn_aceptar = tk.Button(frame, text="Aceptar", font=("Arial", 12), command=enviar)
    btn_aceptar.pack(pady=10)

    root.mainloop()
    root.destroy()

    return datos["numero_orden"]
