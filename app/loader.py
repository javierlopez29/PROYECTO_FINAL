import os
import pandas as pd
from PyPDF2 import PdfReader


class CargadorDocumentos:

    def procesar(self, ruta):

        if not os.path.exists(ruta):
            return "Archivo no encontrado", "error"

        # CSV
        if ruta.endswith(".csv"):

            df = pd.read_csv(ruta)

            return df.head(10).to_string(), "csv"

        # PDF
        elif ruta.endswith(".pdf"):

            lector = PdfReader(ruta)

            texto = ""

            for pagina in lector.pages[:3]:

                contenido = pagina.extract_text()

                if contenido:
                    texto += contenido

            return texto[:2500], "pdf"

        return "Formato no soportado", "error"
