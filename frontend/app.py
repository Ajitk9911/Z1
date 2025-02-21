import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.title("Image Resizer & Publisher")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Send image to FastAPI backend
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{BACKEND_URL}/resize/", files=files)

    if response.status_code == 200:
        st.success("Images resized successfully!")
        st.write(response.json())
    else:
        st.error("Error processing the image.")
