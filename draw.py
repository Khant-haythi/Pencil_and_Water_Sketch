
import cv2
import numpy as np
from io import BytesIO
import math

def convert_to_sketch(image):
   # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
    
    # Blur the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)
    
    # Create the pencil sketch effect
    sketch = cv2.divide(gray_image, 255 - blurred_image, scale=256.0)
    
    # Apply Laplacian for edge detection
    laplacian = cv2.Laplacian(gray_image, cv2.CV_8U, ksize=3)
    
    # Invert Laplacian to make edges white on black
    laplacian_inverted = cv2.bitwise_not(laplacian)
    
    # Combine the sketch with the inverted Laplacian
    sketch_with_edges = cv2.multiply(sketch, laplacian_inverted, scale=1/256.0)
    smoothed_sketch = cv2.bilateralFilter(sketch_with_edges, d=10, sigmaColor=20, sigmaSpace=20)
    
    return smoothed_sketch
    



def convert_watercolor(inp_img, ksize=31):
    # Convert the image to HSV color space
    img_hsv = cv2.cvtColor(inp_img, cv2.COLOR_BGR2HSV)

    # Adjust the value (brightness) channel
    adjust_v = (img_hsv[:, :, 2].astype("uint")+5)*2
    adjust_v = ((adjust_v > 255) * 255 + (adjust_v <= 255) * adjust_v).astype("uint8")
    img_hsv[:, :, 2] = adjust_v

    # Convert the image back to RGB color space
    img_soft = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # Apply Gaussian blur to the image
    img_soft = cv2.GaussianBlur(img_soft, (ksize, ksize), 0)

    # Convert the image to grayscale and apply histogram equalization
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.equalizeHist(img_gray)

    # Create a sketch-like effect
    invert = cv2.bitwise_not(img_gray)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(img_gray, invertedblur, scale=265.0)
    sketch = cv2.merge([sketch, sketch, sketch])

    # Combine the soft and sketch effects
    img_water = ((sketch / 255.0) * img_soft).astype("uint8")

    return img_water

