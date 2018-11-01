# Dependencies
# streamlink package must be installed.

# Libraries
import matplotlib.pyplot as plt
import cv2  # opencv-python package must be installed.
import sh # sh package must be installed.
import time

sh.rm(["-f", "/tmp/caca.mp4"])
#p = sh.streamlink(["https://www.youtube.com/watch?v=RtU_mdL2vBM", "best", "-o", "/tmp/caca.mp4"], _bg=True)
p = sh.streamlink(["https://www.youtube.com/watch?v=wwMDvPCGeE0", "best", "-o", "/tmp/caca.mp4"], _bg=True)


time.sleep(5)
cap = cv2.VideoCapture("/tmp/caca.mp4")
counter = 0
while True:
    ret, frame = cap.read()
    if 0 == counter % 100 and ret:
        plt.imshow(frame)
        plt.show()
    counter += 1
    time.sleep(0.025)
p.kill()