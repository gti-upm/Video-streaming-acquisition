# Dependencies
# streamlink package must be installed.

# Libraries
import cv2  # opencv-python package must be installed.
import subprocess
import time
import os

# Input: video url
video_url = "https://www.youtube.com/watch?v=qGAbuTrm_bI" # Youtube

# Create output folder if necessary
output_dir = './tmp/';
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Clean existing file
subprocess.call(['del', '.\\tmp\\tmp.mp4'], shell=True) # shell=True needed in Windows to find operating commands

# Captured video stream.
subprocess.call(["streamlink", video_url, "best", "-o", "./tmp/tmp.mp4"])
#subprocess.Popen(["streamlink", video_url, "best", "-o", "./tmp/tmp.mp4"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
time.sleep(5)

# Open captured video
cap = cv2.VideoCapture("./tmp/tmp.mp4")
counter = 0
while cap.isOpened():
    # Read frame from video
    ret, frame = cap.read()
    # Show one frame out of 100 from video
    if 0 == counter % 100 and ret:
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('frame', frame)
        else:
            print("No images")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    counter += 1
    time.sleep(0.025)

# Release memory
cv2.destroyAllWindows()