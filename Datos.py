class DatosEtiqueta:
    def __init__(self, numOrden=None, nombreArticulo=None, tono=None, fecha=None, codBarras=None, seleccion=None, calibre=None):
        self.numOrden = numOrden
        self.nombreArticulo = nombreArticulo
        self.tono = tono
        self.fecha = fecha
        self.codBarras = codBarras
        self.seleccion = seleccion
        self.calibre = calibre


    # Método para mostrar los datos
    def mostrar_datos(self):
        print(f"Numero de Orden: {self.numOrden}")
        print(f"Nombre del Artículo: {self.nombreArticulo}")
        print(f"Tono: {self.tono}")
        print(f"Fecha de Embalaje: {self.fecha}")
        print(f"Código de Barras: {self.codBarras}")
        print(f"Selección: {self.seleccion}")
        print(f"Calibre: {self.calibre}")


    def is_valid(self):
        """Verifica si todos los campos son válidos."""
        return all([self.numOrden, self.nombreArticulo, self.tono, self.fecha, self.codBarras, self.seleccion, self.calibre])



