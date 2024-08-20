import cv2
import numpy as np

def convert_to_sketch(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    

    
            

     # Invert the grayscale image
    inverted_img = 255 - gray_image
    
    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)


       # Apply bilateral filter to reduce noise while keeping edges sharp
    filtered_image = cv2.bilateralFilter(blurred_img, d=9, sigmaColor=75, sigmaSpace=75)



     # Invert the blurred image
    inverted_blurred_img = 255 - filtered_image
    
    # Invert the image to get a pencil sketch effect
    sketch = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)

    
    return sketch