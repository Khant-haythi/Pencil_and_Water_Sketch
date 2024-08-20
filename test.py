import cv2
import numpy as np

def convert_to_sketch(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    

    
            
    
    # # Combine the edge-enhanced image with the original grayscale image
    # edge_enhance = cv2.addWeighted(gray_image, 0.7, line_image[:,:,0], 0.3, 0)

     # Invert the grayscale image
    inverted_img = 255 - gray_image
    
    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)


       # Apply bilateral filter to reduce noise while keeping edges sharp
    filtered_image = cv2.bilateralFilter(blurred_img, d=9, sigmaColor=75, sigmaSpace=75)

     # Detect edges using Canny edge detection
    edges = cv2.Canny(filtered_image, threshold1=30, threshold2=100)
    
     # Enhance edges using line detection
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 255, 255), 1)


     # Invert the blurred image
    inverted_blurred_img = 255 - line_image[:,:,0]
    
    # Invert the image to get a pencil sketch effect
    sketch = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)

    
    return sketch