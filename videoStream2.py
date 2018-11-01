import cv2

str = "http://streaming3.webcam.nl:80/n325/n325.stream/playlist.m3u8"
str = "rtmp://streaming3.webcam.nl:80/n302/n302.stream"
str = "https://youtu.be/WPrH_ivypZ8"
str = "http://streaming3.webcam.nl:80/n325/n325.stream/playlist.m3u8"
cap = cv2.VideoCapture(str)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.waitKey(5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()