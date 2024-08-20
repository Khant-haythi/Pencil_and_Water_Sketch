import streamlit as st
import numpy as np
from PIL import Image
import io
from draw import convert_to_sketch, color_sketch

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
    
    # Generate color sketch
    colored_sketch = color_sketch(img_array, sketch)
    
    st.subheader("Colored Sketch")
    st.image(colored_sketch, use_column_width=True)
    
    # Option to download the pencil sketch
    buf_sketch = io.BytesIO()
    Image.fromarray(sketch).save(buf_sketch, format="PNG")
    byte_im_sketch = buf_sketch.getvalue()
    st.download_button(
        label="Download Pencil Sketch",
        data=byte_im_sketch,
        file_name="pencil_sketch.png",
        mime="image/png"
    )
    
    # Option to download the colored sketch
    buf_colored = io.BytesIO()
    Image.fromarray(colored_sketch).save(buf_colored, format="PNG")
    byte_im_colored = buf_colored.getvalue()
    st.download_button(
        label="Download Colored Sketch",
        data=byte_im_colored,
        file_name="colored_sketch.png",
        mime="image/png"
    )