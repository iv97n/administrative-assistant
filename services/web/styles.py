import streamlit as st
import base64
import os

def get_base64_image(image_path):
    """Read and encode an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def inject_custom_css():
    # Define colors for the design
    COLOR_PRIMARY = "#8B0000"  # Dark Red
    COLOR_SECONDARY = "#000000"  # Black
    COLOR_TEXT = "#000000"  # White
    COLOR_BACKGROUND = "#000000"  # Black Background
    COLOR_HEADER = "#000000"  # White Header
    COLOR_CARD = "#FFFFFF"  # White Card


    media_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'media'))
    # Load and encode the background image to base64
    base64_image = get_base64_image(str(os.path.join(media_path, 'fondo.png')))  # Ensure the image path is correct
    
    # Inject CSS into Streamlit app
    st.markdown(f"""
    <style>
    /* App background with fixed position */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: scroll;
        color: {COLOR_TEXT};  /* Set the default text color to white */
    }}

    /* Title colors */
    h1, h2 {{
        color: {COLOR_PRIMARY};
        font-size: 22px;
    }}

    /* Button styling for Streamlit */
    .css-1emrehy.edgvbvh3 {{
        background-color: {COLOR_SECONDARY};
        color: {COLOR_PRIMARY};
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }}
    .css-1emrehy.edgvbvh3:hover {{
        background-color: {COLOR_PRIMARY};
        color: {COLOR_HEADER};
    }}


    /* Links styling */
    a {{
        color: {COLOR_PRIMARY};
    }}

    .custom-subheader-plot {{
        color: {COLOR_TEXT};
        font-size: 24px;
        font-weight: 600;
    }}

    label {{
        color: {COLOR_TEXT} !important;
    }}

    </style>
    """, unsafe_allow_html=True)

