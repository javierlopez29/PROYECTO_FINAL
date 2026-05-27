import streamlit as st
from app.agent import AgenteMultimodal

st.set_page_config(page_title="Agente Multimodal", layout="centered")

st.title("Agente Multimodal (Mistral + Ollama)")

if "agente" not in st.session_state:
    st.session_state.agente = AgenteMultimodal()

if "chat" not in st.session_state:
    st.session_state.chat = []

# SUBIDA DE ARCHIVOS
st.sidebar.header("Documentos")
archivo = st.sidebar.file_uploader("Sube PDF o CSV", type=["pdf", "csv"])

ruta = None

if archivo is not None:
    ruta = f"/tmp/{archivo.name}"
    with open(ruta, "wb") as f:
        f.write(archivo.read())
    st.sidebar.success("Archivo cargado")

# HISTORIAL
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

entrada = st.chat_input("Escribe tu pregunta")

if entrada:

    st.chat_message("user").write(entrada)

    if ruta:
        entrada_final = f"{entrada} [Archivo: {ruta}]"
    else:
        entrada_final = entrada

    respuesta = st.session_state.agente.ejecutar(entrada_final)

    st.chat_message("assistant").write(respuesta)

    st.session_state.chat.append({"role": "user", "content": entrada})
    st.session_state.chat.append({"role": "assistant", "content": respuesta})
