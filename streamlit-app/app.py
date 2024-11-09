import streamlit as st
from styles import inject_custom_css
import sys
import os

# Path setup for SalamandraClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
<<<<<<< Updated upstream
from src.llm.clients.salamandra_client import SalamandraClient
import base64

# ChatEngine Class
class ChatEngine:
    def __init__(self, salamandra_client):
        self.salamandra_client = salamandra_client
        self.chat_history = []

    def add_message(self, sender, message):
        """Adds a new message to the chat history."""
        self.chat_history.append({"sender": sender, "message": message})

    def get_chat_history(self):
        """Returns the chat history."""
        return self.chat_history

    def generate_response(self, prompt, context):
        """Generates a bot response using the SalamandraClient."""
        return self.salamandra_client.givePrediction(prompt, context)

# Initialize SalamandraClient and ChatEngine
salamandra_client = SalamandraClient()
chat_engine = ChatEngine(salamandra_client)

# Load File Paths
file_paths = ['../data/finetune.txt','../data/output_admissio.data','../data/output_agenda.data',
              '../data/output_admissio.data', '../data/output_abans-de-matricular-te-estudis-iniciats.data', 
              '../data/output_acreditacio-de-coneixements-d-idiomes.data']

# Set Streamlit configuration
=======
from src.summarizer.salamandra_client import SalamandraClient
import base64

file_paths = ['../data/output_admissio.data','../data/output_agenda.data','../data/output_admissio.data', '../data/output_abans-de-matricular-te-estudis-iniciats.data', '../data/output_acreditacio-de-coneixements-d-idiomes.data']
client = SalamandraClient()
# Set the Streamlit configuration for the app
>>>>>>> Stashed changes
st.set_page_config(
    page_title="Campus Global Upf",
    page_icon="https://www.upf.edu/o/upf-portal-6-2-theme/images/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Custom local background image
background_image_path = "media/fondo.png"  # Replace with the path to your background image

# Function to convert image to base64 for embedding
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

base64_image = get_image_base64("media/fondo.png")

# Get the context for Salamandra
@st.cache_data
def get_context(file_paths):
    context = ""
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File not found - {file_path}")
        else:
            print(f"File found: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                context += file.read() + "\n"
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='ISO-8859-1') as file:
                    context += file.read() + "\n"
            except UnicodeDecodeError:
                raise Exception(f"Cannot read file {file_path} with 'utf-8' or 'ISO-8859-1'.")
    return context

<<<<<<< Updated upstream
inject_custom_css()

context = get_context(file_paths)

# Chat UI Setup
st.title("Campus Global Chat")

# Initialize chat history
if 'chat_manager' not in st.session_state:
    st.session_state['chat_manager'] = chat_engine

user_avatar_path = "media/user_avatar.jpg"
bot_avatar_path = "media/bot_avatar.png"


chat_manager = st.session_state['chat_manager']

# User input section - place input box at the bottom
# Display chat history first (before the input box)
for chat in chat_manager.get_chat_history():
    avatar_image = user_avatar_path if chat["sender"] == "user" else bot_avatar_path
    with st.chat_message(chat["sender"], avatar=avatar_image):
        st.write(chat["message"])

# User input section - place input box at the bottom
user_input = st.text_input("Type your message:")
if user_input:
    # Add user message to the chat history
    chat_manager.add_message("user", user_input)
    
    # Generate the bot's response
    bot_response = chat_manager.generate_response(user_input, context)
    
    # Add bot response to the chat history
    chat_manager.add_message("bot", bot_response)

    # Redisplay the chat history after new messages are added
    for chat in chat_manager.get_chat_history():
        avatar_image = user_avatar_path if chat["sender"] == "user" else bot_avatar_path
        with st.chat_message(chat["sender"], avatar=avatar_image):
            st.write(chat["message"])
=======
# Full absolute path to the image
full_image_path = os.path.abspath("media/fondo.png")
st.markdown(
    f"""
    <style>
        body {{
            background-image: url('file://{full_image_path}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

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
        instrucció = st.text_input("Pregunta:")

        # Si el usuario ha ingresado una pregunta, obtener la respuesta
        if instrucció:
            res = client.givePrediction(instrucció, file_paths)
            st.write(f"Respuesta: {res}")
>>>>>>> Stashed changes
