import streamlit as st
from styles import inject_custom_css
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.llm.clients.salamandra_client import SalamandraClient
from src.llm.clients.groq_llama_client import GroqClient
import base64
from dotenv import load_dotenv
import html

load_dotenv()

# Initialize client
# client = SalamandraClient()
groq_client = GroqClient()

#Load File Paths
# file_paths = ['../data/finetune.txt','../data/output_admissio.data','../data/output_agenda.data','../data/output_admissio.data', '../data/output_abans-de-matricular-te-estudis-iniciats.data', '../data/output_acreditacio-de-coneixements-d-idiomes.data']
file_paths = ['data/acreditacio_idiomes.json', 'data/nota_mitjana.json', 'data/devolucio_preus_publics.json']

# Set the Streamlit configuration for the app
st.set_page_config(
    page_title="Campus Global Upf",
    page_icon="https://www.upf.edu/o/upf-portal-6-2-theme/images/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

#Get context
@st.cache_data
def get_context(file_paths):
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File not found - {file_path}")
        else:
            print(f"File found: {file_path}")
    context = ""
    for file_path in file_paths:
        # Try opening the file with different encodings
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # html.unescape(file.read())
                file_content = file.read()
                file_content = html.unescape(file_content)
                context += file_content + "\n"
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='ISO-8859-1') as file:
                    file_content = file.read()
                    file_content = html.unescape(file_content)
                    context += file_content + "\n"
            except UnicodeDecodeError:
                raise Exception(f"No se pudo leer el archivo {file_path} con 'utf-8' ni 'ISO-8859-1'.")
    
    return context

inject_custom_css()


context = get_context(file_paths)
# Use the cached function
if 'context' not in st.session_state:
    st.session_state.context = context  # Initialize context in session_state

# Accessing context from session_state
context = st.session_state.context

col1, col2 = st.columns([5, 1])


with col2:
    # Button to toggle the chatbot
    if st.button("Chatbot"):
        st.session_state.chatbot_visible = True

    if 'chatbot_visible' in st.session_state and st.session_state.chatbot_visible:
        # Título de la app
        st.title("Chatbot Simple")

        # Instrucciones iniciales
        st.write("Escriu la teva pregunta.")

        # Recibir input del usuario
        instruction = st.text_input("Pregunta:")

        # Si el usuario ha ingresado una pregunta, obtener la respuesta
        if instruction:
            # res = client.givePrediction(instrucció, context)
            res = groq_client.generate_response(instruction, context)


            st.markdown(f"Respuesta: {res}")
