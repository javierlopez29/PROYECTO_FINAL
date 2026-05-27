# Agente Multimodal enfocado en el análisis financiero

## Descripción

Este proyecto consiste en el desarrollo de un agente multimodal de inteligencia artificial enfocado en el análisis financiero. La idea principal es que el usuario pueda subir documentos en formato CSV o PDF y hacer preguntas sobre su contenido.

El agente está pensado para analizar datos financieros sencillos, como ventas de productos, tendencias o información incluida en informes. A partir de esos documentos, el sistema genera respuestas claras y estructuradas, manteniendo el contexto de la conversación.

El proyecto funciona completamente en local utilizando Ollama con el modelo `mistral:latest`. Para organizar el flujo del agente se utiliza LangChain, y la interfaz principal está desarrollada con Streamlit para facilitar la carga de archivos y la interacción con el usuario.

---

## Dominio elegido

El dominio elegido para este agente es el análisis financiero.

He elegido este enfoque porque permite trabajar con ejemplos prácticos y fáciles de entender, como archivos CSV con datos de ventas o documentos PDF con informes financieros. Además, este dominio permite demostrar cómo el agente puede extraer información de un documento, analizarla y generar conclusiones útiles.

---

## Funcionalidades principales

El agente permite:

- Subir archivos CSV con datos financieros.
- Subir documentos PDF con informes financieros.
- Realizar preguntas en lenguaje natural sobre los documentos cargados.
- Analizar ventas, productos y tendencias.
- Resumir información relevante de documentos PDF.
- Generar respuestas estructuradas.
- Mantener el contexto de la conversación para preguntas de seguimiento.
- Ejecutarse de forma local sin utilizar APIs externas.

---

## Tecnologías utilizadas

- Python 3.11.15
- Ollama
- Modelo `mistral:latest`
- LangChain
- Streamlit
- Pandas
- PyPDF2

---

## Estructura del proyecto

```text
agente-multimodal/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── loader.py
│   ├── memory.py
│   └── prompts.py
│
├── app.py
├── streamlit_app.py
├── ventas_vts.csv
├── informe_financiero.pdf
├── requirements.txt
└── README.md
```

---

## Explicación de los archivos principales

### `streamlit_app.py`

Es la interfaz principal del proyecto. Permite subir archivos PDF o CSV y escribir preguntas desde una página web creada con Streamlit.

### `app.py`

Es una versión básica por terminal. Sirve para probar el agente desde consola. Aunque existe esta opción, la versión principal del proyecto es la interfaz con Streamlit.

### `app/agent.py`

Contiene la lógica principal del agente. Se encarga de recibir la pregunta del usuario, comprobar si hay un documento cargado, procesar la información y enviar el prompt al modelo local mediante LangChain.

### `app/loader.py`

Se encarga de procesar los documentos. Actualmente permite leer archivos CSV mediante Pandas y archivos PDF mediante PyPDF2.

### `app/prompts.py`

Contiene los prompts utilizados por el agente. Hay prompts específicos para CSV, PDF y texto libre, por lo que el agente no depende de un único prompt genérico.

### `app/memory.py`

Gestiona la memoria conversacional del agente para mantener el contexto entre preguntas.

---

## Instalación

### 1. Entrar en la carpeta del proyecto

```bash
cd ~/Escritorio/agente-multimodal
```

### 2. Crear el entorno virtual

El proyecto se ha desarrollado y probado con Python 3.11.15.

```bash
python3.11 -m venv venv
```

### 3. Activar el entorno virtual

```bash
source venv/bin/activate
```

Si se ha activado correctamente, la terminal debería mostrar algo parecido a esto:

```text
(venv) alumno@alumno-VirtualBox:~/Escritorio/agente-multimodal$
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Archivo `requirements.txt`

El proyecto incluye un archivo `requirements.txt` con las librerías necesarias para ejecutar el agente.

Contenido del archivo:

```txt
langchain==0.1.20
langchain-community==0.0.38
langchain-core==0.1.53
pandas==2.2.2
PyPDF2
streamlit
```

---

## Configuración de Ollama

Este proyecto utiliza Ollama para ejecutar el modelo de lenguaje en local.

### 1. Comprobar que Ollama está instalado

```bash
ollama --version
```

### 2. Descargar el modelo Mistral

```bash
ollama pull mistral
```

### 3. Comprobar que el modelo está disponible

```bash
ollama list
```

Debe aparecer un modelo similar a este:

```text
mistral:latest
```

---

## Ejecución del proyecto

Para ejecutar el proyecto correctamente se recomienda utilizar dos terminales.

---

### Terminal 1: iniciar Ollama

En la primera terminal se inicia el servidor local de Ollama:

```bash
ollama serve
```

Esta terminal debe permanecer abierta mientras se utiliza el agente.

Para cerrar el servidor de Ollama se puede usar:

```text
Ctrl + C
```

---

### Terminal 2: ejecutar Streamlit

En otra terminal se activa el entorno virtual y se ejecuta la aplicación:

```bash
cd ~/Escritorio/agente-multimodal
source venv/bin/activate
streamlit run streamlit_app.py
```

Después de ejecutar el comando, la aplicación se abrirá en el navegador. Normalmente estará disponible en:

```text
http://localhost:8501
```

Para cerrar Streamlit se puede usar:

```text
Ctrl + C
```

---

## Ejecución por terminal

También se puede ejecutar una versión básica del agente desde consola:

```bash
cd ~/Escritorio/agente-multimodal
source venv/bin/activate
python app.py
```

En esta versión, para cerrar el programa se puede escribir:

```text
salir
```

También se puede cerrar desde la terminal usando:

```text
Ctrl + C
```

---

## Archivos de prueba incluidos

El proyecto incluye archivos de prueba para comprobar el funcionamiento del agente.

### `ventas_vts.csv`

Archivo CSV con datos de ventas de productos tecnológicos. Se utiliza para probar el análisis de datos financieros.

Preguntas de ejemplo:

```text
¿Cuál es el producto más vendido?
```

```text
¿Qué tendencias observas en las ventas?
```

```text
Genera un informe financiero breve basado en estos datos
```

### `informe_financiero.pdf`

Documento PDF con un informe financiero sencillo. Se utiliza para probar la lectura y el resumen de documentos.

Pregunta de ejemplo:

```text
Resume el informe financiero y extrae las conclusiones más importantes
```

---

## Escenarios de uso

### Escenario 1: producto más vendido

El usuario sube el archivo `ventas_vts.csv` y pregunta:

```text
¿Cuál es el producto más vendido?
```

El agente analiza los datos del CSV e identifica el producto con mayor número de ventas. Este escenario sirve para comprobar que el sistema puede leer un archivo de datos y extraer una conclusión concreta.

---

### Escenario 2: análisis de tendencias

El usuario sigue utilizando el archivo `ventas_vts.csv` y pregunta:

```text
¿Qué tendencias observas en las ventas?
```

El agente revisa los datos del CSV y genera una respuesta indicando los patrones más importantes, como productos con crecimiento, estabilidad en ventas o posibles oportunidades.

---

### Escenario 3: informe financiero basado en CSV

En este tercer escenario se sigue usando el mismo archivo `ventas_vts.csv`. En este caso, se le indica al agente que genere un informe financiero breve basado en los datos del CSV.

Pregunta utilizada:

```text
Genera un informe financiero breve basado en estos datos
```

El agente utiliza la información del archivo de ventas para crear una respuesta más completa, organizada como un pequeño informe. Este escenario demuestra que el sistema no solo responde preguntas concretas, sino que también puede generar una salida estructurada a partir de los datos analizados.

---

## Funcionamiento general

El funcionamiento del sistema sigue este flujo:

1. El usuario sube un documento o escribe una pregunta.
2. El sistema detecta si el archivo es CSV o PDF.
3. El contenido del documento se extrae mediante Pandas o PyPDF2.
4. El agente selecciona el prompt adecuado según el tipo de entrada.
5. LangChain envía el prompt al modelo local ejecutado con Ollama.
6. El modelo `mistral:latest` genera una respuesta.
7. La respuesta se muestra en la interfaz de Streamlit.
8. La memoria conversacional guarda el contexto para permitir preguntas de seguimiento.

---

## Prompt engineering

El proyecto utiliza prompts diferentes según el tipo de entrada:

- Para archivos CSV, el prompt está orientado al análisis de ventas, productos y tendencias.
- Para documentos PDF, el prompt está orientado al resumen de informes financieros y extracción de conclusiones.
- Para texto libre, el prompt permite responder preguntas generales relacionadas con el dominio financiero.

Esto permite que el agente adapte su comportamiento al documento recibido y no dependa de un único prompt genérico.

---

## Memoria conversacional

El agente incorpora memoria conversacional mediante LangChain. Esto permite mantener el contexto de la conversación y realizar preguntas de seguimiento sobre el mismo documento.

Ejemplo:

```text
Pregunta 1: ¿Cuál es el producto más vendido?
Pregunta 2: ¿Qué recomendación harías sobre ese producto?
```

---

## Requisitos principales cumplidos

Este proyecto cumple los requisitos principales de la práctica:

- Uso de un modelo LLM libre ejecutado en local.
- Uso de Ollama como herramienta de despliegue local.
- Uso de LangChain como framework de orquestación.
- Interfaz de usuario con Streamlit.
- Ingesta de documentos CSV y PDF.
- Procesamiento y análisis de documentos.
- Generación de respuestas estructuradas.
- Gestión del contexto conversacional.
- Uso de prompts específicos según la funcionalidad.
- Código fuente organizado en módulos.
- Archivo `requirements.txt` incluido.

---

## Autor

JAVIER LOPEZ

Proyecto realizado como práctica de la asignatura de Inteligencia Artificial.

