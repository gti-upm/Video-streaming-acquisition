# Libraries
import cv2  # opencv-python package must be installed.

# Input: video url.
url_video = "./data/big_buck_bunny.mp4"

# Video source selection: file.
cap = cv2.VideoCapture(url_video)
# Loop: capture frames youtube video.
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if frame is not None:
        # Example of image processing: gray scale conversion.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', gray)
    else:
        print("No images")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture object and windows.
cap.release()
cv2.destroyAllWindows()
