import argparse
import cv2
import numpy as np

# Set video source
parser = argparse.ArgumentParser()
parser.add_argument("--cam_src", help="Set video feed source", required=True)
parser.add_argument("--ir_cam_src", help="IR camera video feed source")
args = parser.parse_args()
ir_src = int(args.ir_cam_src)
src = int(args.cam_src)

# Create a blank function to use for trackbar callbacks
def nothing(x):
    pass

# Set default values for the upper and lower color ranges to detect blue in the HSV color space
upper_blue = np.array([130, 255, 255])
lower_blue = np.array([110, 50, 50])

# Create a window for the video feed
cv2.namedWindow('Video Feed')

# Start the video feed
cap = cv2.VideoCapture(src)

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create numpy arrays for the upper and lower color values
    upper_color = np.array([upper_blue[0], upper_blue[1], upper_blue[2]])
    lower_color = np.array([lower_blue[0], lower_blue[1], lower_blue[2]])

    # Create a mask by applying the upper and lower color values to the frame
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Apply a Gaussian blur to the mask to reduce noise
    mask_blur = cv2.GaussianBlur(mask, (5,5), 0)

    # Detect circles in the mask using the HoughCircles function
    circles = cv2.HoughCircles(mask_blur, cv2.HOUGH_GRADIENT, dp=1, minDist=100,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    # Create a copy of the original frame to draw on
    frame_copy = frame.copy()

    # Draw circles on the copy of the original frame
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame_copy, (x, y), r, (0, 255, 0), 2)

    # Display the video feed and mask
    cv2.imshow('Video Feed', frame_copy)
    cv2.imshow('Mask', mask)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
