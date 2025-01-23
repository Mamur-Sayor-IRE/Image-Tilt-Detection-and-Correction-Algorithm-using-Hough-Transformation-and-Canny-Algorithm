# Tilt Detection and Correction with OpenCV

This repository contains a Python script to detect and correct the tilt of images using OpenCV's edge detection and Hough Line Transformation. It is particularly useful for processing images where horizontal alignment is important, such as license plates, scanned documents, or rotated photographs.

---

## Features
1. **Tilt Detection**:  
   The script identifies the tilt angle of an image by analyzing the horizontal lines using the Hough Line Transformation.
   
2. **Tilt Correction**:  
   If the detected tilt exceeds a specified threshold, the image is automatically rotated to correct the tilt.

3. **Batch Processing**:  
   Processes multiple images listed in the `image_paths` array and displays both the original and corrected images.

4. **Error Handling**:  
   The script checks for invalid file paths or images and provides appropriate error messages.

---

## Dependencies
To use this script, ensure the following Python libraries are installed:
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Google Colab Patches (`cv2_imshow` for displaying images in Google Colab)

Install the required libraries using:
```bash
pip install opencv-python-headless numpy
