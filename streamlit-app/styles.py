import streamlit as st
import base64

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
    
    # Load and encode the background image to base64
    base64_image = get_base64_image("media/fondo.png")  # Ensure the image path is correct
    
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

    /* Card container styling */
    .card {{
        background-color: {COLOR_CARD};
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.8);
        margin-bottom: 20px;
    }}

    /* Links styling */
    a {{
        color: {COLOR_PRIMARY};
    }}

    /* Text container with transparent white background */
    .stTextContainer {{
        background-color: rgba(255, 255, 255, 0.4);  /* 40% transparency with white */
        padding: 20px;
        border-radius: 10px;
        color: {COLOR_TEXT};
        max-width: 1250px;
        margin: 20px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.8);
        font-size: 18px;
    }}

    .custom-subheader-plot {{
        color: {COLOR_TEXT};
        font-size: 24px;
        font-weight: 600;
    }}

    label {{
        color: {COLOR_TEXT} !important;
    }}

    /* Streamlit markdown text styling */
    .stMarkdown {{
        background-color: rgba(255, 255, 255, 0.9);  /* 40% transparency with white */
        padding: 20px;
        border-radius: 10px;
        color: {COLOR_TEXT};
        max-width: 1250px;
        margin: 20px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }}
    .stColumn {{
        background-color: rgba(255, 0, 0, 0.2);  /* Example: Light red with transparency */
        padding: 20px;
        border-radius: 10px;
    # }}

    </style>
    """, unsafe_allow_html=True)
