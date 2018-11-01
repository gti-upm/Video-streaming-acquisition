# Libraries
import cv2  # opencv-python package must be installed.

# Video source selection: camera.
cap = cv2.VideoCapture(0)

# Loop: capture frames from video camera.
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Example of image processing: gray scale conversion.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture object and windows.
cap.release()
cv2.destroyAllWindows()