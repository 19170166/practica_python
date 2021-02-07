from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

# c = canvas.Canvas("prueba.pdf")
ruta = '/Users/angel/Downloads/practicas_python/practica_1.pdf'
file = open("prueba.txt", "w")


#datos={'id':'1','nombre':'angel','objeto':'balon'}
#df=pd.read_json(datos)
#df.to_json(ruta)
# c.drawString(50, 50, '%s' % datos)
# c.save()
class prueba:

    def escribir_datos(self, dato):
        # c.drawString(50, 50, '%s' % dato)
        # c.save()
        file.write(str(dato))
        # df=pd.read_json(datos)
        # df.to_csv(ruta)

    def guardar(self):
        file.close()
        # c.save()
