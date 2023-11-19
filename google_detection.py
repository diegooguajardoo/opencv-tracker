'''
This script is used to detect changes in the camera feed and save the frames when changes are detected.
This script was used to detect when the Google Coral Dev Board was taken out of its box and turned on.
The detection is based on the absolute difference between two consecutive frames.
The script also adds a timestamp to the current frame and saves the frame as an image.
'''


import cv2
import numpy as np
import datetime
import matplotlib.pyplot as plt

# Function to check if two images are different
def images_are_different(img1, img2, threshold=10_000_000):
    diff = cv2.absdiff(img1, img2)
    diff_sum = np.sum(diff)
    return diff_sum > threshold



# Set up video capture
cap = cv2.VideoCapture(0)  # Change the argument to the camera index if you have multiple cameras

# Initialize variables
prev_frame = None

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Initialize prev_frame on the first iteration
    if prev_frame is None:
        prev_frame = gray
        continue

    # Check if the current frame is different from the previous one
    if images_are_different(prev_frame, gray):
        # Add a date label to the current frame
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, f"Date: {current_date}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        # Save the current frame with a timestamp
        timestamp = datetime.datetime.now().strftime("%Y %m %d_%H %M %S")
        filename = f"change_{timestamp}.png"
        cv2.imwrite(filename, frame)
        print(f"Change detected! Image saved as {filename}")

        # Update prev_frame
        prev_frame = gray

    # Display the current frame (optional)
    cv2.imshow("Camera Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
