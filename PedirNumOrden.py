import tkinter as tk
from tkinter import messagebox

def pedir_numero_orden():
    """
    Muestra un formulario con un único campo para ingresar el número de orden.
    Valida si el número está entre 10000 y 99999 antes de aceptarlo.
    """
    def enviar():
        """Valida que se haya ingresado un número entero dentro del rango permitido."""
        try:
            numero_orden = int(entry_orden.get())  # Convierte la entrada a entero
            
            # Aquí se realiza la comprobación de que el número exista en la base de datos
            if 10000 <= numero_orden <= 99999:
                #messagebox.showinfo("Número válido", "El número de orden es válido.",parent=root)
               # tk.messagebox.showinfo("Número válido", "El número de orden es válido.")
                datos["numero_orden"] = numero_orden
                root.quit()  # Cierra la ventana si el número es correcto
            else:
                messagebox.showerror("Número inválido", "El número de orden debe tener 5 cifras.")
        
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Por favor, ingrese un número entero.")

    # Crear ventana principal
    root = tk.Tk()
    root.title("Generador de Etiqueta")  # Título de la ventana
    root.geometry("300x320")  # Tamaño fijo
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

    root.resizable(False, False)  # Evita que la ventana cambie de tamaño

    datos = {"numero_orden": None}  # Diccionario para almacenar el número de orden

    # Crear un frame para centrar todos los elementos
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centra el frame en la ventana

    # Etiqueta para indicar qué debe ingresar el usuario
    tk.Label(frame, text="Ingrese un número de orden:").pack(pady=10)

    # Campo de entrada para el número de orden
    entry_orden = tk.Entry(frame)
    entry_orden.pack(pady=5)

    # Botón para confirmar la entrada
    btn_aceptar = tk.Button(frame, text="Aceptar", command=enviar)
    btn_aceptar.pack(pady=10)

    root.mainloop()  # Mantiene la ventana abierta hasta que el usuario interactúe
    root.destroy()  # Cierra la ventana al finalizar

    return datos["numero_orden"]  # Retorna el número de orden ingresado si es válido
