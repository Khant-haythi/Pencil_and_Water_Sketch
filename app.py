import cv2
import streamlit as st
import numpy as np
from PIL import Image
import io

from numpy.ma.core import divide

from draw import convert_to_sketch, convert_watercolor

# Set page configuration
st.set_page_config(page_title="PicSketch", layout="centered")

# Custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        background-color: #E0FFFF;
    }

    .title {
        text-align: center;
        color: #D2691E;
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        margin-top: 30px;
        #text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
   
    .caption {
        color: #FFF;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #FFF;
        margin-top: 50px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .radio-button {
        background: linear-gradient(to right, #4CAF50, #2196F3);
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
    }
    .radio-button:hover {
        background: linear-gradient(to right, #45a049, #1976D2);
    }
    .radio-button.active {
        background: linear-gradient(to right, #388E3C, #1565C0);
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='title'>🎨 PicSketch</h1>", unsafe_allow_html=True)
st.markdown("""
🪄Transform your images into beautiful pencil sketches or watercolor painting with ease!
""")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Radio button container
    st.subheader( "_Choose an effect_ ✨:", divider="rainbow")
   # st.markdown("<h2 class='subheader'>Choose an effect✨:</h2>", unsafe_allow_html=True)
    effect = st.radio("", ("Original Image", "Pencil Sketch", "WaterColor Painting"), index=0, key="effect")

    if effect == "Original Image":
        st.image(image, caption="Original Image", use_column_width=False)

    elif effect == "Pencil Sketch":
        sketch = convert_to_sketch(img_array)

        if sketch is not None:
            st.image(sketch, caption="Pencil Sketch", use_column_width=False)

            # Option to download the pencil sketch
            buf_sketch = io.BytesIO()
            Image.fromarray(sketch).save(buf_sketch, format="PNG")
            byte_im_sketch = buf_sketch.getvalue()
            st.download_button(
                label="Download Pencil Sketch",
                data=byte_im_sketch,
                file_name="pencil_sketch.png",
                mime="image/png")
        else:
            st.error("Error processing the Pencil Sketch.")

    elif effect == "WaterColor Painting":
        ksize_watercolor = st.slider("Select kernel size for Watercolor Effect (must be odd)", min_value=1, max_value=51, value=31, step=2)
        color_sketch = convert_watercolor(img_array, ksize=ksize_watercolor)

        if color_sketch is not None:
            st.image(color_sketch, caption="Watercolor Painting", use_column_width=False)
            # Option to download the colored sketch
            buf_colored = io.BytesIO()
            Image.fromarray(color_sketch).save(buf_colored, format="PNG")
            byte_im_colored = buf_colored.getvalue()
            st.download_button(
                label="Download Watercolor Painting",
                data=byte_im_colored,
                file_name="watercolor.png",
                mime="image/png"
            )

        else:
            st.error("Error processing the Watercolor Painting.")

