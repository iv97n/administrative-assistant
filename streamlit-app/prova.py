import streamlit as st
import os

# Check if the image file exists to help debug
background_image_path = "media/fondo.png"
if not os.path.exists(background_image_path):
    st.error(f"Background image not found: {background_image_path}")
else:
    st.write("image found")


# Add custom CSS for the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("file://{os.path.abspath(background_image_path)}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Streamlit App with Local Background Image")

# Some text content
st.write("This is a Streamlit app with a local background image applied.")
st.write("You can put any other content here as needed.")
