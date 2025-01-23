import cv2
import numpy as np
from google.colab.patches import cv2_imshow



def detect_tilt_and_correct(image, threshold=2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)
    if lines is None:
        print("No significant lines detected. Assuming image is not tilted.")
        return image, 0

    # Extract angles, converting from radians to degrees
    angles = []
    for line in lines:
        rho, theta = line[0]
        # Convert to degrees
        angle = (theta - np.pi / 2) * (180 / np.pi)
        if -45 <= angle <= 45:  # Consider mostly horizontal lines
            angles.append(angle)

    if not angles:
        print("No valid lines detected for tilt correction.")
        return image, 0

    # Use median for stability
    median_angle = np.median(angles)

    if abs(median_angle) > threshold:
        print(f"Tilt detected with angle: {median_angle-.5:.2f} degrees. Correcting...")
        corrected_image = tilt_image(image, median_angle-.5)
        return corrected_image, median_angle-.5
    else:
        print("Image is not tilted.")
        return image, 0

# List of image paths
image_paths = ['/content/bplt.PNG', '/content/tilted_5.png', '/content/tilted_20.png']

# Process each image
for path in image_paths:
    print(f"\nProcessing image: {path}")
    image = cv2.imread(path)

    if image is None:
        print(f"Error: Unable to load image from {path}. Please check the file path.")
        continue

    # Detect and correct tilt
    corrected_image, detected_tilt_angle = detect_tilt_and_correct(image)

    # Display results
    if detected_tilt_angle == 0:
        print(f"Image {path} is not tilted.")
        cv2_imshow(image)
    else:
        print(f"Image {path} was tilted by {detected_tilt_angle:.2f} degrees. Corrected.")
        print("Showing the tilted image:")
        cv2_imshow(image)  # Show tilted image
        print("Showing the corrected image:")
        cv2_imshow(corrected_image)  # Show corrected image
