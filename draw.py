
import cv2
import numpy as np

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
    
    return sketch_with_edges