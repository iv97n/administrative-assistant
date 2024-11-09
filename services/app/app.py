import streamlit as st
from styles import inject_custom_css
import sys
import os

# Path setup for SalamandraClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
# from src.llm.clients.salamandra_client import SalamandraClient
from llm.clients.groq_llama_client import GroqClient
from llm.clients.salamandra_client import SalamandraClient
from llm.utils.utils import parse_document
from dotenv import load_dotenv

load_dotenv()

# Initialize SalamandraClient and ChatEngine
groq_client = GroqClient(api_key=os.getenv("GROQ_API_KEY"))
salamandra_client = SalamandraClient()
#Load File Paths
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))
# file_paths = ['../data/finetune.txt','../data/output_admissio.data','../data/output_agenda.data','../data/output_admissio.data', '../data/output_abans-de-matricular-te-estudis-iniciats.data', '../data/output_acreditacio-de-coneixements-d-idiomes.data']
file_paths = [os.path.join(data_path, 'acreditacio_idiomes.json'), os.path.join(data_path, 'nota_mitjana.json'), os.path.join(data_path, 'devolucio_preus_publics.json')]

# Set the Streamlit configuration for the app
st.set_page_config(
    page_title="Campus Global Upf",
    page_icon="https://www.upf.edu/o/upf-portal-6-2-theme/images/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Custom local background image
inject_custom_css()

def get_context(file_paths):
    context = ""
    for file_path in file_paths:
        with open(file_path, "r") as file:
            text_content = parse_document(file)
            context += text_content + "\n"
    return context


# Get context
context = get_context(file_paths)

with st.sidebar:

    model = st.radio(
    "Quin model vols utilitzar?",
    ["Salamandra", "Llama3"],
    index=None,
    )

  
    # Título de la app
    st.title("Chatbot Simple")

    # Instrucciones iniciales
    st.write("Escriu la teva pregunta.")

    # Recibir input del usuario
    instruction = st.text_input("Pregunta:")

    # Si el usuario ha ingresado una pregunta, obtener la respuesta
    if instruction:
        if model == "Salamandra":
            res = salamandra_client.givePrediction(instruction, context)
        if model == "Llama3":
            res = groq_client.generate_response(instruction, context)

        st.markdown(res)
