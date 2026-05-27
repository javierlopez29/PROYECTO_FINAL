from langchain_community.chat_models import ChatOllama
from app.loader import CargadorDocumentos
from app.memory import GestorMemoria
from app.prompts import prompt_csv, prompt_pdf, prompt_texto


class AgenteMultimodal:

    def __init__(self):

        self.modelo = ChatOllama(
            model="mistral",
            base_url="http://localhost:11434"
        )

        self.cargador = CargadorDocumentos()
        self.memoria = GestorMemoria()

    def ejecutar(self, entrada_usuario):

        ruta = None
        texto_usuario = entrada_usuario

        if "[Archivo:" in entrada_usuario:
            partes = entrada_usuario.split("[Archivo:")
            texto_usuario = partes[0].strip()
            ruta = partes[1].replace("]", "").strip()

        contenido = ""
        tipo = "texto"

        if ruta:
            contenido, tipo = self.cargador.procesar(ruta)

        memoria = self.memoria.obtener()

        # PROMPTS ESPECIALIZADOS
        if tipo == "csv":
            prompt = prompt_csv(texto_usuario, contenido, memoria)

        elif tipo == "pdf":
            prompt = prompt_pdf(texto_usuario, contenido, memoria)

        else:
            prompt = prompt_texto(texto_usuario, memoria)

        respuesta = self.modelo.invoke(prompt)

        self.memoria.guardar(entrada_usuario, respuesta.content)

        return respuesta.content
