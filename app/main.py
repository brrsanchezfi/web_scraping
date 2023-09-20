import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors
import schedule
import time

# URL de la página web a consultar
url = 'https://www.ejemplo.com'

def consultar_y_generar_informe():
    try:
        # Realizar la solicitud GET
        response = requests.get(url)

        # Comprobar si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Obtener el encabezado de la respuesta
            headers = response.headers

            # Crear un archivo PDF para el informe
            pdf_filename = 'informe.pdf'
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Establecer el estilo del informe
            styles = getSampleStyleSheet()
            normal_style = styles['Normal']
            title_style = styles['Title']

            # Crear el contenido del informe
            story = []

            # Título del informe
            story.append(Paragraph("Informe del Encabezado de la Respuesta", title_style))
            story.append(Spacer(1, 12))

            # Agregar el contenido del encabezado al informe
            for key, value in headers.items():
                header_info = f"<b>{key}:</b> {value}"
                story.append(Paragraph(header_info, normal_style))
                story.append(Spacer(1, 6))

            # Construir el informe
            doc.build(story)
            print(f"Informe generado y guardado como {pdf_filename}")

        else:
            print(f"La solicitud GET no fue exitosa. Código de respuesta: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud GET: {e}")

# Programar la consulta y generación de informes cada 6 horas
schedule.every(6).hours.do(consultar_y_generar_informe)

while True:
    schedule.run_pending()
    time.sleep(1)
