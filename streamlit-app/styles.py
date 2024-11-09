import streamlit as st
import base64

def get_base64_image(image_path):
    """Read and encode an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def inject_custom_css():
    # Define colors for the design
    COLOR_PRIMARY = "#4A90E2"
    COLOR_SECONDARY = "#50E3C2"
    COLOR_TEXT = "#333333"
    COLOR_BACKGROUND = "#3A668D"
    COLOR_HEADER = "#FFFFFF"
    COLOR_CARD = "#FFFFFF"
    
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

    }}

    /* Title colors */
    h1, h2 {{
        color: {COLOR_PRIMARY};
    }}

    /* Button styling for Streamlit */
    .css-1emrehy.edgvbvh3 {{
        background-color: {COLOR_SECONDARY};
        color: {COLOR_HEADER};
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
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }}

    /* Links styling */
    a {{
        color: {COLOR_PRIMARY};
    }}

    /* Text container with transparent background */
    .stTextContainer {{
        background-color: rgba(255, 255, 255, 0.75);  /* 50% transparency */
        padding: 20px;
        border-radius: 10px;
        color: {COLOR_TEXT};
        max-width: 1250px;
        margin: 20px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        font-size: 18px;
    }}

    .custom-subheader-plot {{
        color: white;
        font-size: 24px;
        font-weight: 600;
    }}

    label {{
            color: white !important;
    }}

    </style>
    """, unsafe_allow_html=True)
