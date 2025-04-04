from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas

from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

def generar_etiqueta(datos_producto):
    archivo_salida = "etiqueta3.pdf"
    c = canvas.Canvas(archivo_salida, pagesize=(100 * mm, 70 * mm))
    
    # Secciones con recuadros
    c.rect(5 * mm, 45 * mm, 80 * mm, 20 * mm)  # Descripción
    c.rect(5 * mm, 25 * mm, 15 * mm, 20 * mm)  # Tono
    c.rect(20 * mm, 25 * mm, 15 * mm, 20 * mm)  # Selección
    c.rect(35 * mm, 25 * mm, 15 * mm, 20 * mm)  # Calibre
    c.rect(50 * mm, 25 * mm, 35 * mm, 20 * mm)  # Fecha embalaje
    c.rect(50 * mm, 5 * mm, 35 * mm, 20 * mm)  # CodArticulo
    
    # Texto dentro de los recuadros
    c.setFont("Helvetica", 6)
    c.drawString(7 * mm, 61 * mm, "DESCRIZIONE ARTICOLO")
    c.drawString(7 * mm, 59 * mm, "ARTICLE DESCRIPTION")
    c.drawString(7 * mm, 57 * mm, "DESCRIPCIÓN DEL ARTÍCULO")    

    #paragrafo para el nombre del articulo (hace salto de pagina) Max 60 caracteres
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Helvetica-Bold"
    style.fontSize = 12
    style.leading = 12
    paragraph = Paragraph(datos_producto.nombreArticulo[0:60], style)
    paragraph.wrapOn(c, 78 * mm, 15 * mm)  # Width and height constraints
    if len(datos_producto.nombreArticulo) <= 30:
        paragraph.drawOn(c, 7 * mm, 52 * mm)
    else:
        paragraph.drawOn(c, 7 * mm, 48 * mm)

    c.setFont("Helvetica", 6)
    c.drawString(7 * mm, 41 * mm, "TONO")
    c.drawString(7 * mm, 39 * mm, "TONE")
    c.drawString(7 * mm, 37 * mm, "TONO")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(7 * mm, 32 * mm, datos_producto.tono[0:4])

    c.setFont("Helvetica", 6)
    c.drawString(22 * mm, 41 * mm, "SCELTA")
    c.drawString(22 * mm, 39 * mm, "CHOICE")
    c.drawString(22 * mm, 37 * mm, "SELECCIÓN")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(22 * mm, 32 * mm, str(datos_producto.seleccion)[0:3])

    c.setFont("Helvetica", 6)
    c.drawString(37 * mm, 41 * mm, "CALIBRO")
    c.drawString(37 * mm, 39 * mm, "CALIBER")
    c.drawString(37 * mm, 37 * mm, "CALIBRE")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(37 * mm, 32 * mm, str(datos_producto.calibre)[0:5])

    c.setFont("Helvetica", 6)
    c.drawString(52 * mm, 41 * mm, "DATA CONFEZIONAMENTO")
    c.drawString(52 * mm, 39 * mm, "PACKAGING DATE")
    c.drawString(52 * mm, 37 * mm, "FECHA DE EMBALAJE")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(52 * mm, 32 * mm, datos_producto.fecha)

    c.setFont("Helvetica", 6)
    c.drawString(52 * mm, 20 * mm, "CODICE ARTICOLO")
    c.drawString(52 * mm, 18 * mm, "ITEM NUMBER")
    c.drawString(52 * mm, 16 * mm, "CÓDIGO ARTÍCULO")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(52 * mm, 11 * mm, str(datos_producto.numOrden)[0:10])
    
    #generar codigo de barras
    barcode_ean = eanbc.Ean13BarcodeWidget(datos_producto.codBarras)
    barcode_ean.barHeight = 16 * mm
    barcode_drawing = Drawing(380 * mm, 17 * mm)
    barcode_drawing.add(barcode_ean)       
    renderPDF.draw(barcode_drawing, c, 7 * mm, 6 * mm)

    c.showPage()
    c.save()    
   



