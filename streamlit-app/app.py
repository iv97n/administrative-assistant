import streamlit as st
from styles import inject_custom_css
#path a Salamandra client: ainahack/src/summarizer/salamandra_client.py
#path a app.py: ainahack/streamlit-app/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.summarizer.salamandra_client import SalamandraClient

file_path = '../src/summarizer/data/finetune.txt'


with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


client = SalamandraClient()
# Set the Streamlit configuration for the app
st.set_page_config(
    page_title="Campus Global Upf",
    page_icon="https://www.upf.edu/o/upf-portal-6-2-theme/images/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Título de la app
st.title("Chatbot Simple")

# Instrucciones iniciales
st.write("Escriu la teva pregunta.")

# Recibir input del usuario
instrucció = st.text_input("Pregunta:")

# Si el usuario ha ingresado una pregunta, obtener la respuesta
if instrucció:
    res = client.givePrediction(instrucció, file_content)
    st.write(f"Respuesta: {res}")

