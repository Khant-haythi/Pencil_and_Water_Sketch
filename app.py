import streamlit as st
import numpy as np
from PIL import Image
import io
from draw import convert_to_sketch

st.title("Image to Pencil Sketch Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    st.subheader("Original Image")
    st.image(image, use_column_width=True)
    
    sketch = convert_to_sketch(img_array)
    
    st.subheader("Pencil Sketch")
    st.image(sketch, use_column_width=True)
    
    # Option to download the sketch
    buf = io.BytesIO()
    Image.fromarray(sketch).save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download Sketch",
        data=byte_im,
        file_name="pencil_sketch.png",
        mime="image/png"
    )